from web3 import Web3
import urllib.request
import time
import traceback
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/xxxxxxx"))
ctr = w3.eth.contract(Web3.toChecksumAddress("0xa37aDDE3Ba20A396338364e2ddb5e0897D11a91D"), abi='[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_value","type":"uint256"}],"name":"burn","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_value","type":"uint256"}],"name":"burnFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Burn","type":"event"}]')

def get_WFEE_balance(addr):
    bal = ctr.call().balanceOf(Web3.toChecksumAddress(addr))
    return round(bal / 1e18)

def send_WFEE(from_sercet, from_addr):
    current_nonce = w3.eth.getTransactionCount(from_addr)
    data = b''.fromhex('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    signed_txn = w3.eth.account.signTransaction(dict(
                                                nonce=current_nonce,
                                                gasPrice=int(2e9),
                                                gas=39000,
                                                to=Web3.toChecksumAddress("0xa37adde3ba20a396338364e2ddb5e0897d11a91d"),
                                                value=0,
                                                data=data), 
                                                from_sercet)
    print(w3.eth.sendRawTransaction(signed_txn.rawTransaction).hex())

def send_ETH(to_list):
    nonce_step = 0
    current_nonce = w3.eth.getTransactionCount("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    for _ in to_list:
        try:
            bal = w3.eth.getBalance(Web3.toChecksumAddress(_[-1]))
            if get_WFEE_balance(_[-1]) > 49 and bal < 77e12:
                signed_txn = w3.eth.account.signTransaction(dict(
                                                            nonce=current_nonce + nonce_step,
                                                            gasPrice=int(3e9),
                                                            gas=21000,
                                                            to=_[-1],
                                                            value=int(80e12),
                                                            data=b''), 
                                                            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print(w3.eth.sendRawTransaction(signed_txn.rawTransaction).hex())
                nonce_step += 1
            else:
                print("skip")
        except:
            print("error skip")
        time.sleep(0.5)


def recycle(from_list):
    for _ in from_list:
        bal = w3.eth.getBalance(Web3.toChecksumAddress(_[-1]))
        print(_, bal / 1e12)
        if bal > 35e12:
            try:
                signed_txn = w3.eth.account.signTransaction(dict(
                                                            nonce=w3.eth.getTransactionCount(_[-1]),
                                                            gasPrice=int(1.5e9),
                                                            gas=21000,
                                                            to="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                                                            value=int(bal - 31.51e12),
                                                            data=b''), 
                                                            _[-2])
                print(w3.eth.sendRawTransaction(signed_txn.rawTransaction).hex())
            except:
                traceback.print_exc()
        else:
            print("pass")


# with open("wfee.txt", "r") as file:
#     acc = [_.split() for _ in file]

# with open("ethed.txt", "r") as file:
#     ethed = [_.split() for _ in file]

# for _ in acc:
#     print(_, get_WFEE_balance(_[-1]), w3.eth.getBalance(Web3.toChecksumAddress(_[-1]))/1e12)

# recycle(acc)

# send_ETH(acc)
# done = 0
# not_done = 1
# for _ in ethed:
#     try:
#         wfee_bal = get_WFEE_balance(_[-1])
#         bla = w3.eth.getBalance(Web3.toChecksumAddress(_[-1])) / 1e12
#         print(_, wfee_bal, bla)
#         if wfee_bal < 40:
#             print("alread send.")
#             done += 1
#         elif bla < 77:
#             file = open("not_done_yet.txt", "a+")
#             file.write(" ".join(_) + "\n")
#             file.close()
#             print("not enough gas.")
#             not_done += 1
#         else:
#             file = open("not_done_yet.txt", "a+")
#             file.write(" ".join(_) + "\n")
#             file.close()
#             send_WFEE(_[1], _[2])
#             not_done += 1
#         time.sleep(0.2)
#     except:
#         traceback.print_exc()

# print(done, not_done)

# print(not_send, sended, not_recv)