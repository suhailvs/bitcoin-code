import hashlib
import txnUtils
from keyUtils import keyToAddr, addrToScriptPubkey

# From --> one input
privateKey = hashlib.sha256('abcdefghijklmnop').hexdigest() # mpSyb71528U8dQjuTCeDCcJqH8dQTyY13c
from_address= keyToAddr(privateKey,testnet=True)
txn_hash = "3c24ca820100153fb43434191d10464dd2dcd13f0c9aa07d15f7330e8bcd0596"

# To --> android testnet wallet
to_address = 'miD4PnSDWC2M725hvFBoBhNn8fbowoHnnS'

# Sign the Transction
signed_txn = txnUtils.makeSignedTransaction(
	privateKey, txn_hash, 0, addrToScriptPubkey(from_address), # input: has balance 0.01btc
    [[900000,addrToScriptPubkey(to_address)]] # outputs: 0.009btc 
)
    
print 'SIGNED TXN', signed_txn

# Broadcast this transaction at:
# https://testnet.blockexplorer.com/tx/send