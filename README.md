Manually creating a Transation on Testnet
=========================================

For my experiment I purchased 1300 mBTC from https://testnet.manu.backend.hamburg/faucet for free.
Now my [android_wallet] has 1300 mBTC.

Create Address and PrivateKey:
------------------------------

You can find an example of compressed [graphical address generator here](http://royalforkblog.github.io/2014/08/11/graphical-address-generator/). But i am here using uncompressed address.
You need to install ecdsa library, ie:
```
$ pip install ecdsa
```

Following is the code snippet to generate an address from private key:
```
import ecdsa, hashlib, utils

# Key Creatinon
def privateKeyToPubKey(s):
    sk = ecdsa.SigningKey.from_string(s.decode('hex'), curve=ecdsa.SECP256k1)
    return ('\04' + sk.verifying_key.to_string()).encode('hex')

def pubKeyToAddr(s,p):
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256(s.decode('hex')).digest())
    return utils.base58CheckEncode(p, ripemd160.digest())

def keyToAddr(s,testnet=False):
	# see https://en.bitcoin.it/wiki/List_of_address_prefixes
	# ie: mainnet --> 0 and testnet --> 111
	prefix = 111 if testnet else 0 
	return pubKeyToAddr(privateKeyToPubKey(s),prefix)
```
prefix=111 is used for testnet keys while prefix =0 used for mainnet bitcoin.

Example of address creation using passphase `abcdefghijklmnop`:
```
>>> import hashlib
>>> from keyUtils import keyToAddr
>>> privateKey = hashlib.sha256('abcdefghijklmnop').hexdigest()
>>> print keyToAddr(privateKey,testnet=True)
mpSyb71528U8dQjuTCeDCcJqH8dQTyY13c
```

Transaction
-----------
Send 10 mBTC to that address(`mpSyb71528U8dQjuTCeDCcJqH8dQTyY13c`) from my [android_wallet].
With Transaction [3c24ca820100153fb43434191d10464dd2dcd13f0c9aa07d15f7330e8bcd0596](https://live.blockcypher.com/btc-testnet/tx/3c24ca820100153fb43434191d10464dd2dcd13f0c9aa07d15f7330e8bcd0596/)

Now My goal was to create a transaction to transfer these bitcoins back to my [android_wallet],
`miD4PnSDWC2M725hvFBoBhNn8fbowoHnnS`, subtracting a fee of 1 mBTC bitcoins. 
Thus, the destination address will receive 9 mBTC.


Signing a txn:
--------------

```
  $ python testnetTxn.py
  SIGNED TXN 01000000019605cd8b0e33f7157da09a0c3fd1dcd24d46101d193434b43f15000182ca243c000000008a473044022038499cd167670e9bc0f9e7f7e0ebecee7b16273744ddb20937981468178119ea022038a2fa46223d2d27f9e284448b47267d33a558ad92dcbbf594ab3891e35200940141049a1df75ed6cdccf2da470e55d5d21544ddfd85efd9cfd7b4c3040608211f705efe8d6494558aa6f433f61e0e54392fd0534d38bd14c2ed02769e29f2ed67f3b1ffffffff01a0bb0d00000000001976a9141d85fb26947ea4bfdf14209912a1e27ae4efd20188ac00000000
```

Sending a Transaction: tx
-------------------------
Now broadcast the above signed transaction(ie `01000000019605c...fd20188ac00000000`) over the Bitcoin network at https://testnet.blockexplorer.com/tx/send

Checking this [transaction](https://live.blockcypher.com/btc-testnet/tx/b572828f07197f6e662fd7b3c51b1ebabc19969d75e8d08f7e118d4afb358505/)
showed that my transaction worked. I could also verify the success of this transaction by looking in my Bitcoin wallet and by checking online.

References:
-----------
+ [Bitcoins the hard way: Using the raw Bitcoin protocol](http://www.righto.com/2014/02/bitcoins-hard-way-using-raw-bitcoin.html)
+ [Deconstructing Transactions](http://royalforkblog.github.io/2014/11/20/txn-demo/)
+ [Bitcoin Developer Examples](https://bitcoin.org/en/developer-examples)


[android_wallet]: https://play.google.com/store/apps/details?id=de.schildbach.wallet_test&hl=en "Testnet3 Android Wallet"