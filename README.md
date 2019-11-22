# BitcoinLottery
Python script to generate BTC adresses in the hope one with actual btc will be found

## Requirements
The following packages have to be installed to make the lottery work:

* sudo apt install python-pip
* pip install blockstack
* pip install bitcoin
* sudo apt install sqlite3
* sudo apt install sqlitebrowser
* apt-get install screen

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

## Running the script in the background
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
