import logging
import sys
from csv import DictReader, DictWriter
from datetime import datetime
from pathlib import Path

logging.root.setLevel(logging.INFO)
input_headers = [
    "Date","Posted Date","Reference Number","Activity Type","Status","Transaction Card Number","Merchant Category","Merchant Name","Merchant City","Merchant State/Province","Merchant Country","Merchant Postal Code/Zip","Amount","Rewards","Name on Card"
]
lunch_money_headers = [
    'date', 'payee', 'amount', 'currency', 'notes', 'category', 'tags'
]

_, *rest = sys.argv
if not rest:
    logging.error("Missing rogers transaction history csv argument. Try something like: \"python parse.py rogers_transaction_history.csv\"")
    sys.exit(1)
if len(rest) > 1:
    logging.error("Too many arguments. Try something like: \"python parse.py rogers_transaction_history.csv\"")
    sys.exit(1)
rogers_file_path = Path(rest[0])
logging.info("Using rogers transaction history csv: %s", rogers_file_path)
if '~' in rogers_file_path.parts:
    rogers_file_path.expanduser()
if not rogers_file_path.exists():
    logging.error("Specified rogers transaction history csv does not exist.")
    sys.exit(1)
elif not rogers_file_path.is_file():
    logging.error("Specified rogers transaction history csv is not a file.")
    sys.exit(1)

if rogers_file_path.suffix != '.csv':
    logging.warning("Specified rogers transaction history csv might not be a csv file. Are you sure you have the right file?")

with open(rogers_file_path) as input_file:
    now_without_milliseconds = datetime.now().replace(microsecond=0)
    export_filepath = Path(f"lunch_money_export_{now_without_milliseconds.isoformat()}.csv")
    with open(export_filepath, mode='w') as lunch_money_export_file:
        input_reader = DictReader(input_file, fieldnames=input_headers)
        lunch_money_export_file = DictWriter(lunch_money_export_file, fieldnames=lunch_money_headers)
        lunch_money_export_file.writeheader()
        next(input_reader) # skip header row
        row_number = 1
        for row in input_reader:
            row_number += 1
            status = row['Status']
            if status != 'APPROVED':
                logging.warning('Skipping transaction with status %s on row %d', status, row_number)
                continue
            lunch_money_export_file.writerow({
                'date': row['Date'],
                'payee': row['Merchant Name'],
                'amount': row['Amount'],
                'currency': 'CAD',
                # 'notes': row['Merchant Name'],
                # 'category': 'Food',
                # 'tags': ''
            })
    logging.info("Successfully converted rogers transaction history into lunch money csv format. File path: %s", export_filepath.absolute())