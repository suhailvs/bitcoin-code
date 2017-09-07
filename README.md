Manually creating a Transation on Testnet
=========================================

For my experiment I purchased 1300 mBTC from https://testnet.manu.backend.hamburg/faucet for free.
Now my [android_wallet] has 1300 mBTC.

Create Address and PrivateKey:
------------------------------
Created a testnet address at [Bitaddress](https://bitaddress.org/?testnet=true).
```
  testnet_address = 'mrf14nvLzxeXtkMjEpYPK225bbtUXJQXaV'
  wif_PrivateKey = '92ZmNRZfL8jFE3yQUZGwDEkKu5owWT6Kgu4UuxM9e4PsPJCVshd'
```
Send 10 mBTC to that address(`mrf14nvLzxeXtkMjEpYPK225bbtUXJQXaV`) from my [android_wallet].
With Transaction [115a6b923c759f3eddfb5720ea53cdd2003af1074924ea6b5c7b74005a08dedf](https://live.blockcypher.com/btc-testnet/tx/115a6b923c759f3eddfb5720ea53cdd2003af1074924ea6b5c7b74005a08dedf/)

Now My goal was to create a transaction to transfer these bitcoins back to my [android_wallet],
`miD4PnSDWC2M725hvFBoBhNn8fbowoHnnS`, subtracting a fee of 1 mBTC bitcoins. 
Thus, the destination address will receive 9 mBTC.


Python Usage:
-------------
You need to install ecdsa library.
```
  $ pip install ecdsa
  $ python testnetTxn.py
  SIGNED TXN 0100000001dfde085a00747b5c6bea244907f13a00d2cd53ea2057fbdd3e9f753c926b5a11000000008c49304602210080374d6f4a8b6703abde691794502ed13e97c17906aafda702520de6956df46e022100bf762a284a9ae9747b33b417605309090a6a8f1f3126e6610f6b9d58699ee6ac014104368a50fafd4b88df7bca8d0435374198e8ffc9e8a0005ac5f9dea47f9afa40f8b4fecc6a28948a6cc28d4f19876a864be5f8b6075fc291745fb8e23b586b81a8ffffffff01a0bb0d00000000001976a9141d85fb26947ea4bfdf14209912a1e27ae4efd20188ac00000000
```

Sending a Transaction: tx
-------------------------
Now broadcast the above signed transaction(ie `0100000001dfd...20188ac00000000`) over the Bitcoin network at https://testnet.blockexplorer.com/tx/send

Checking this [transaction](https://live.blockcypher.com/btc-testnet/tx/b0f23fa50606d24e72a23e52f16f66c71cabd2dbdf3b53bd5019d7c5a84b49b2/)
showed that my transaction worked. I could also verify the success of this transaction by looking in my Bitcoin wallet and by checking online.

References:
-----------
+ [Bitcoins the hard way: Using the raw Bitcoin protocol](http://www.righto.com/2014/02/bitcoins-hard-way-using-raw-bitcoin.html)
+ [Deconstructing Transactions](http://royalforkblog.github.io/2014/11/20/txn-demo/)
+ [Bitcoin Developer Examples](https://bitcoin.org/en/developer-examples)


[android_wallet]: https://play.google.com/store/apps/details?id=de.schildbach.wallet_test&hl=en "Testnet3 Android Wallet"