#!/usr/bin/env python

## ===== IMPORT MODULES ===== ##
import requests
from bitcoin import *
import time
import sqlite3
import re
import requests

## ===== BTC ADDRESSES GENERATING ===== ##
# Generating keys
def create_addr():
	priv = random_key()
	pub = privtopub(priv)
	addr = pubtoaddr(pub)
	electrumPKey = encode_privkey(priv, 'wif')
	return addr, priv, electrumPKey

addr,priv,electrumPKey = create_addr()

## ===== CHECK BALANCE ===== ##
# Get the amount of BTC on the address
# Address below is a checking address
# addr = '3Bmb9Jig8A5kHdDSxvDZ6eryj3AXd3swuJ'
addr = '3Bmb9Jig8A5kHdDSxvDZ6eryj3AXd3swu'
req = requests.get('https://blockchain.info/balance?active='+(addr))

# Converting url into text
text = req.text


print("=====================")
print("Received string: \n" + req.text)
print("=====================")


if text == 'Invalid Bitcoin Address':
	print ('Invalid Bitcoin Address found')
	addr = 'Invalid Bitcoin Address found'
	priv = 'Invalid Bitcoin Address found'
	electrumPKey = 'Invalid Bitcoin Address found'
	btcamount = '0'
	btcamountinteger = int(btcamount)
	print (btcamountinteger)
else:
	btcamount = re.search('final_balance":(.+?),"n_tx', text).group(1)
	btcamountinteger = int(btcamount)
	# Print keys to console (for checking code)
	print("BTC Address: " + addr)
	print("Private Key: " + priv)
	print("Electrum Import Key: " + electrumPKey)
	print ("btcamount: " + btcamount)
	print (btcamountinteger)

