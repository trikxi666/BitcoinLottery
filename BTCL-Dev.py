#!/usr/bin/env python

# Generate bitcoin keys and address
import requests
from bitcoin import *
import time
import sqlite3
import re

# Start timer section
def executeScript():
    
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

	# Get the amount of BTC on the address
	req = requests.get('https://blockchain.info/balance?active='+(addr))

	# Print output to the screen for checking code
	#print req.text

	# Extracting the BTC amount from blockchain.info output
	# text = req.text
	# left = 'final_balance":'
	# right = ',"n_tx'
	# btcamount = str(print(text[text.index(left)+len(left):text.index(right)]))
	
	# Old way of splitting (for archiving purposes)
	pattern = '(?<=final_balance":).+?,'
	result = re.search(pattern, req)
	print(req[result.start():result.end() - 1])
	
	# splitter1=req.text.split(":")[2]
	# btcamount=splitter1.split(",")[0]
	# print ("Amount on address: " + btcamount)
	# Send amount to console for checking code

	# Convert satoshi to BTC
	# SatoshiConvert = float(splitter2) / 100000000.0
	# print ("Amount on address: " + str(SatoshiConvert))
	# BitcoinConvert = str(SatoshiConvert)

	## OUTPUT ##
		
	# Write output to comma separated file
	# text_file = open("BTC.csv", "a+")
	# text_file.write(BitcoinConvert + "," + addr + "," + electrumPKey + "," + priv)
	# text_file.write("\n")
	# text_file.close()

	# Write output to SQLite database
	# conn = sqlite3.connect("lottery.db")
	# c = conn.cursor()
	# c.execute("INSERT INTO addresses (amount,btc_address,electrum_key,private_key) VALUES (?, ?, ?, ?)",(btcamount,addr,electrumPKey,priv))
	# conn.commit()
	# conn.close()

# Timer section part 2
time.sleep(4)

while True:
    executeScript()