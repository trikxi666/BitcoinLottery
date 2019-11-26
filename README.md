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

## Downloading the BitcoinLottery Python script

Clone or download the code to your computer:

```bash
git clone https://github.com/Willemstijn/BitcoinLottery.git
```

Or download and extract:

https://github.com/Willemstijn/BitcoinLottery/archive/master.zip

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

## Setting up a Telegram bot

Follow the procedure below to create a channel for signalling found Satoshi's:

* Open and login to [Telegram Web interface](https://web.telegram.org).
* Search @ BotFather and send him a "/start" message.
* To create a new bot, send the "/newbot" message.
* Provice the bot a channel name and user name.
* Telegram provides you with a token for accessing the bot though the HTTP API (Keep this token safe!).
* Search your bot (by the link you just got - e.g. t.me/<botname>), press the “Start” button or send a “/start” message.
* Open a new tab with your browser, enter https://api.telegram.org/bot<yourtoken>/getUpdates. 
* Type ``/start`` to start the bot. You should see something like this:

```json
{"ok":true,"result":[{"update_id":846954168,
"message":{"message_id":2,"from":{"id":6XXXXXXXXX,"is_bot":false,"first_name":"YourFirstName","username":"YourUserName","language_code":"nl"},"chat":{"id":6XXXXXXX,"first_name":"YourFirstName","username":"Yourname","type":"private"},"date":15267434115,"text":"/start","entities":[{"offset":0,"length":6,"type":"bot_command"}]}}]}
```

* Look for “id”, for instance, 6xxxxxxx above is the chat id in this case. 
* Use this "id" and your "token" in the BitcoinLottery script.

## Running the script

### Linux

You can run the script in your terminal with this command:

```bash
./BitcoinLottery.py
```

### Windows

Just run the line below in a command prompt in the directory of the script:

```bash
py ./BitcoinLottery.py
```

## SQLite

To quickly find an address with an amount higher than 0, use the following sql statement in the SQLite console:

```sql
SELECT * FROM addresses WHERE  amount > 0;
```

When Satoshi are found, you can find the address in the database with this command:

```sql
SELECT electrum_key, private_key, amount FROM addresses WHERE  btc_address = "<the address found>";
```

## Daemonizing the script in Linux

To run the script as a background service (Daemon) in Linux, do the following:

* Copy the ``BitcoinLottery.sh`` file to ``/etc/init.d/BitcoinLottery.sh``. Check if the directories are valid. 
* Optional: copy the BitcoinLottery.py script to a generic script location (e.g. /usr/local/bin). Note that you have to change the SQLite database location as well.
* Make both files executable with ``sudo chmod 777 ./BitcoinLottery.py /etc/init.d/BitcoinLottery.sh``
* Add the service for autostart when booting with ``sudo update-rc.d /etc/init.d/BitcoinLottery.sh defaults``
* To remove the service from autostart, run ``sudo update-rc.d -f /etc/init.d/BitcoinLottery.sh remove``
* If you change the bash script, you can reload it with the command ``sudo systemctl daemon-reload``

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
