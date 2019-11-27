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
	for i in range(0, 10):
		# Generating keys
		def create_addr():
			priv = random_key()
			pub = privtopub(priv)
			addr = pubtoaddr(pub)
			electrumPKey = encode_privkey(priv, 'wif')
			return addr, priv, electrumPKey

		addr,priv,electrumPKey = create_addr()

		# Print keys to console (for checking code)
		# print("BTC Address: " + addr)
		# print("Private Key: " + priv)
		# print("Electrum Import Key: " + electrumPKey)

	## ===== CHECK BALANCE ===== ##
		# Get the amount of BTC on the address
		# Address below is a checking address
		# addr = '3Bmb9Jig8A5kHdDSxvDZ6eryj3AXd3swuJ'
		req = requests.get('https://blockchain.info/balance?active='+(addr))

		# Converting url into text
		text = req.text

		# Old code do not remove yet
		# # Extracting the BTC amount from blockchain.info output
		# try:
		#     btcamount = re.search('final_balance":(.+?),"n_tx', text).group(1)
		# except:
		# 	btcamount = None
		# # 		btcamount = 'no balance found' # apply your error handling here
		
		# New error handling code here
		# try:
		# 	btcamount = re.search('final_balance":(.+?),"n_tx', text).group(1)
		# except ValueError:
		# 	print("Try #{} failed with ValueError: Sleeping for 2 secs before next try:".format(i))
		# 	time.sleep(2)
		# 	continue
		# break

	if text == 'Invalid Bitcoin Address':
		print ('Invalid Bitcoin Address found')
		addr = 'Invalid Bitcoin Address found'
		priv = 'Invalid Bitcoin Address found'
		electrumPKey = 'Invalid Bitcoin Address found'
		btcamount = '0'
		btcamountinteger = int(btcamount)
		# print (btcamountinteger)
	else:
		btcamount = re.search('final_balance":(.+?),"n_tx', text).group(1)
		btcamountinteger = int(btcamount)
		# Print keys to console (for checking code)
		print("BTC Address: " + addr)
		print("Private Key: " + priv)
		print("Electrum Import Key: " + electrumPKey)
		print ("btcamount: " + btcamount)
		# print (btcamountinteger)

	print ("==================================================================================")
	
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