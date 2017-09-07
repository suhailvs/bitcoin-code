###########################################################################
# TestNet Address sample
# bitaddress.org/?testnet=true Brainwallet, Passphrase: suhail412_vahee1910
wifPrivateKey = '92ZmNRZfL8jFE3yQUZGwDEkKu5owWT6Kgu4UuxM9e4PsPJCVshd'
address = 'mrf14nvLzxeXtkMjEpYPK225bbtUXJQXaV'
###########################################################################

# transaction
import txnUtils,utils

# OP_DUP OP_HASH160 xx OP_EQUALVERIFY OP_CHECKSIG
addrToScriptPubkey = lambda x:  '76a914' + utils.base58CheckDecode(x).encode('hex') + '88ac'

# wifToPrivateKey
p = utils.base58CheckDecode(wifPrivateKey)
privateKey=p.encode('hex')

# To Address --> android testnet wallet
to_address = 'miD4PnSDWC2M725hvFBoBhNn8fbowoHnnS'

signed_txn = txnUtils.makeSignedTransaction(privateKey,
        "115a6b923c759f3eddfb5720ea53cdd2003af1074924ea6b5c7b74005a08dedf", # output (prev) transaction hash
        0, # sourceIndex
        addrToScriptPubkey("mrf14nvLzxeXtkMjEpYPK225bbtUXJQXaV"), # has balance 0.01btc
        [[900000, #satoshis .009btc
        addrToScriptPubkey(to_address)]]
        )
    
print 'SIGNED TXN', signed_txn

# Broadcast this transaction at:
# https://testnet.blockexplorer.com/tx/send