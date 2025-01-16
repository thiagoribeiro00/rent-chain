from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from web3 import Web3

app = FastAPI()

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID'))

CONTRACT_ADDRESS = ''

CONTRACT_ABI = [
    {
        "inputs": [],
        "name": "cadastrarPropriedade",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_valorAluguel", "type": "uint256"}],
        "name": "cadastrarPropriedade",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "address", "name": "_propriedade", "type": "address"}],
        "name": "reservarPropriedade",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "address", "name": "_propriedade", "type": "address"}],
        "name": "pagarAluguel",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    }
]


contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

class PropriedadeCadastro(BaseModel):
    valorAluguel: int
    address: str

class PropriedadeReserva(BaseModel):
    propriedadeAddress: str
    address: str

class PropriedadePagamento(BaseModel):
    propriedadeAddress: str
    valorPagamento: int
    address: str

@app.post("/cadastrar-propriedade")
async def cadastrar_propriedade(propriedade: PropriedadeCadastro):
    try:
        tx_hash = contract.functions.cadastrarPropriedade(propriedade.valorAluguel).transact({'from': propriedade.address})
        return {"tx_hash": tx_hash}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/reservar-propriedade")
async def reservar_propriedade(propriedade: PropriedadeReserva):
    try:
        tx_hash = contract.functions.reservarPropriedade(propriedade.propriedadeAddress).transact({'from': propriedade.address})
        return {"tx_hash": tx_hash}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/pagar-aluguel")
async def pagar_aluguel(propriedade: PropriedadePagamento):
    try:
        tx_hash = contract.functions.pagarAluguel(propriedade.propriedadeAddress).transact({'from': propriedade.address, 'value': propriedade.valorPagamento})
        return {"tx_hash": tx_hash}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
