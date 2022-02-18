from dataclasses import dataclass
from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider('https://eth-goerli.alchemyapi.io/v2/qknyN14j9CAWwRzsZEqoXkEkvjDgQeFL'))

@dataclass
class User:
   def __init__(self, pkey, address):
      self.pkey = pkey
      self.address = address
      self.nonce = w3.eth.get_transaction_count(address)

@dataclass
class Token:
   def __init__(self, address, amount):
      self.address = address
      self.amount = amount

guni_factory_address = '0x0A307EC30E3CE35D2C32725D322224d0F4b076dd'
guni_pool_address = '0x6079C730F633B526edfdeF3629EA1563581D1aCd'
user = '0xF15C3a5C951722D1eD4176a2e153f0c3ba325474'

guni_factory_abi_file = open('../artifacts/contracts/GUniFactory.sol/GUniFactory.json')
guni_factory_abi_json = json.load(guni_factory_abi_file)['abi']

token_a_abi_file = open('./artifacts/@openzeppelin/contracts/__mocks__/MockERC20.sol/MockERC20A.json')
token_a_abi_json = json.load(token_a_abi_file)['abi']

token_b_abi_file = open('./artifacts/@openzeppelin/contracts/__mocks__/MockERC20.sol/MockERC20B.json')
token_b_abi_json = json.load(token_a_abi_file)['abi']

def CreatePool(user, tokenA, tokenB, uniFee, lowerTick, upperTick):
    guni_factory_contract = w3.eth.contract(guni_factory_address, abi=guni_factory_abi_json)

    create_pool_txn = guni_factory_contract.functions.createPool(guni_factory_address,
                                                                 tokenA,
                                                                 tokenB,
                                                                 1,
                                                                 0,
                                                                 1)

def Approve(user, token):
   erc20_contract = w3.eth.contract(token.address, abi=token_a_abi_json)

   approval_txn = erc20_contract.functions.approve(dcex_address, 2**256-1
                              ).buildTransaction({
                                 'chainId': 5,
                                 'gas': 100000,
                                 'maxFeePerGas': w3.toWei('2', 'gwei'),
                                 'maxPriorityFeePerGas': w3.toWei('1.5', 'gwei'),
                                 'nonce': user.nonce
                              })
   signed_txn = w3.eth.account.sign_transaction(approval_txn, private_key=user.pkey)
   w3.eth.send_raw_transaction(signed_txn.rawTransaction)
   txn = w3.toHex(w3.keccak(signed_txn.rawTransaction))
   print(txn)
   return txn

def Deposit(user, token):
   dcex_core_contract = w3.eth.contract(dcex_address, abi=dcex_abi_json)

   dcex_deposit_txn = dcex_core_contract.functions.deposit(user, token.address, token.amount
                                       ).buildTransaction({
                                          'chainId': 5,
                                          'nonce': user.nonce,
                                          'type': 2,
                                          'gas': 100000,
                                          'maxFeePerGas': w3.toWei('2', 'gwei'),
                                          'maxPriorityFeePerGas': w3.toWei('1.5', 'gwei')
                                       })
   signed_txn = w3.eth.account.sign_transaction(dcex_deposit_txn, private_key=user.pkey)
   w3.eth.send_raw_transaction(signed_txn.rawTransaction)
   txn = w3.toHex(w3.keccak(signed_txn.rawTransaction))
   print(txn)
   return txn


if (__name__ == '__main__'):
   userA = User(b'\xcb\x38\xe9\x43\x63\xb2\x01\xda\x20\x84\x1f\x63\x81\x25\x8b\x69\x10\x97\xbc\x6f\xb9\xd4\xbf\x3c\x99\x06\x02\xab\x1b\x1b\x96\xc8',
                 '0x06F19906526deeA97c658dE1FbAba91E3c5d0091'
   )
   userB = User(b'\xea\xa6\x49\x40\xe6\xbb\x66\x8d\x8e\x20\x69\xdc\x48\x38\x9f\xce\x28\x52\xe6\x09\xad\x5b\x46\x29\x74\xa4\xdb\x2e\x14\xcb\x0e\x12',
                 '0x1EBFc01D833709dCdc8D5683cEc41a42FE341D36'
   )
   tokenA = Token(Web3.toChecksumAddress('0x477791737131e8703849f99AFD57c0A154E90A03'), # TOKENA
                  15*10**18
   )
   tokenB = Token(Web3.toChecksumAddress('0xFAC97049dEa2F743b62537b3365fB1dD0Cf29df9'), # TOKENB
                  1*10**18
   )