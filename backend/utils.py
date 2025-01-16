from web3 import Web3

def conectar_blockchain(url_nodo):
    return Web3(Web3.HTTPProvider(url_nodo))

def enviar_transacao(contract, funcao, args, from_address):
    tx_hash = contract.functions[funcao](*args).transact({'from': from_address})
    return tx_hash

def validar_endereco_ethereum(endereco):
    if len(endereco) != 42 or endereco[:2] != '0x':
        return False
    return True
