# rogers_transaction_history_csv_formatter
Convert the [Rogers Bank](https://rogersbank.com) transaction history csv format into a https://lunchmoney.app csv format.

### Usage
1. [Visit this link](https://github.com/yawhide/rogers_transaction_history_csv_formatter/archive/main.zip) to download the code in this repository.
1. Extract the main.zip file and go into the folder.
1. Open your terminal and `cd` into this folder you just extracted above.
1. Run the following:
```
python parse.py path/to/rogers-transaction-history-csv
```

Example
```
python parse.py "~/Downloads/Transaction History_2023-10-06.csv"
```

This program will output a csv called `lunch_money_export_{timestamp}.csv`. Example: `lunch_money_export_2023-11-06T15:54:24.csv`

### Notes
Ensure you wrap the file path in double quotes as Rogers Bank by default has spaces in the transaction history csv file name.