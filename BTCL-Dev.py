#!/usr/bin/env python

## ===== IMPORT MODULES ===== ##
import requests
from bitcoin import *
import time
import sqlite3
import re
import requests

# Start timer section
def executeScript():
    
## ===== BTC ADDRESSES GENERATING ===== ##
	# Generating keys
	def create_addr():
		priv = random_key()
		pub = privtopub(priv)
		addr = pubtoaddr(pub)
		electrumPKey = encode_privkey(priv, 'wif')
		return addr, priv, electrumPKey

	addr,priv,electrumPKey = create_addr()

	# Print keys to console (for checking code)
	print("Electrum Import Key: " + electrumPKey)
	print("Private Key: " + priv)
	print("BTC Address: " + addr)

## ===== CHECK BALANCE ===== ##
	# Get the amount of BTC on the address
	# Address below is a checking address
	# addr = '3Bmb9Jig8A5kHdDSxvDZ6eryj3AXd3swuJ'
	req = requests.get('https://blockchain.info/balance?active='+(addr))

	# Converting url into text
	text = req.text

	# Extracting the BTC amount from blockchain.info output
	try:
	    btcamount = re.search('final_balance":(.+?),"n_tx', text).group(1)
	except AttributeError:
    		btcamount = 'no balance found' # apply your error handling here

	# Convert btcamount to integer for calculation later in script
	btcamountinteger = int(btcamount)

	print ("Amount on address: " + btcamount)
	
## ===== OUTPUT TO DB /FILE ===== ##
		
	# Write output to SQLite database
	conn = sqlite3.connect("lottery.db")
	c = conn.cursor()
	c.execute("INSERT INTO addresses (amount,btc_address,electrum_key,private_key) VALUES (?, ?, ?, ?)",(btcamount,addr,electrumPKey,priv))
	conn.commit()
	conn.close()

	# Else write output to comma separated file
	# text_file = open("BTC.csv", "a+")
	# text_file.write(BitcoinConvert + "," + addr + "," + electrumPKey + "," + priv)
	# text_file.write("\n")
	# text_file.close()

## ===== USE TELEGRAM FOR NOTIFICATION OF FOUND SATOSHI ===== ##
	if btcamountinteger > 0:
		def telegram_bot_sendtext(bot_message):
			
			# Enter your bot token and bot chat ID here for warnings with Telegram
			bot_token = ''
			bot_chatID = ''
			send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

			response = requests.get(send_text)

			return response.json()
			
		# btcamountstring = str(btcamount)
		telegramtext = telegram_bot_sendtext("Found BTC Address: " + addr + " with " + btcamount + " satoshi")
		print(telegramtext)

# Timer section part 2
time.sleep(4)

while True:
    executeScript()