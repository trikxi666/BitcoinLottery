# BitcoinLottery
Python script to generate BTC adresses in the hope one with actual btc will be found

## Requirements

### Linux

The following packages have to be installed to make the lottery work:

* sudo apt install python-pip
* pip install blockstack
* pip install bitcoin
* sudo apt install sqlite3
* sudo apt install sqlitebrowser
* apt-get install screen

### Windows

The following software has to be installed on Windows 10 for this script to work

* Download and install the latest stable [Python3 for Windows](https://www.python.org/downloads/windows/)(Current stable version is 3.8.0).
* py -m pip install requests
* py -m pip install bitcoin
* Download SQLite from the [download page of the SQlite official website](https://www.sqlite.org/download.html). Follow the instructions on the [Download & Install SQLite tools](https://www.sqlitetutorial.net/download-install-sqlite/) page.

## Create a SQLite database for storing found keys
Create the database with the following commands

```bash
# Create new database in the directory
sqlite3 lottery.db

# Create table in the database
CREATE TABLE addresses ( 
amount INT NOT NULL, 
btc_address VARCHAR(50), 
electrum_key VARCHAR(70), 
private_key VARCHAR(80), 
PRIMARY KEY (btc_address) );

# Show the tables with
.tables

# Show the table schema with
.schema addresses

# Quit sqlite
.quit
```

## Running the script 

### Linux

For now I use this quick and dirty method of runing the script in the background.

```bash
# Create a new virtual terminal
screen -dmS btcl

# Connect to the virtual screen
screen -r btcl

# Run the script
./BitcoinLottery.py
```

Close your terminal screen. The BitcoinLottery PID belongs to the virtual terminal and keeps running.  
To check the script, run ''screen -r btcl'' again

### Windows

No background process yet. Just run the line below in a command prompt in the directory of the script:

```
py ./BitcoinLottery.py
```

## SQLite

To quickly find an address with an amount higher than 0, use the following sql statement in the SQLite console:

```
SELECT * FROM addresses WHERE  amount > 0;
```