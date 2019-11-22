#!/usr/bin/env python

# Generate bitcoin keys and address
import requests
from bitcoin import *

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
splitter1=req.text.split(":")[2]
splitter2=splitter1.split(",")[0]

# Send amount to console for checking code
#print(splitter2)

# Convert satoshi to BTC
SatoshiConvert = float(splitter2) / 100000000.0
print ("Amount on address: " + str(SatoshiConvert))

# Writing output to comma separated file
text_file = open("BTC.csv", "a+")
text_file.write(str(SatoshiConvert) + "," + addr + "," + electrumPKey + "," + priv)
text_file.write("\n")
text_file.close()

# ================= ADDITIONAL TEST CODE HERE ====================
