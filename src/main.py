from fastapi import FastAPI
from datetime import datetime


from src.schemas import (
    CreateTransactionPostBody,
    CreateTransactionResponse,
    GetExtractResponse,
)

app = FastAPI()


@app.post("/clients/:id/transacoes", response_model=CreateTransactionResponse)
def create_transaction(id: int, transaction: CreateTransactionPostBody):

    client = {"limit": 100000, "saldo": -900}
    return {
        "limite": client["limit"],
        "saldo": client["saldo"],
    }


@app.get("/clients/:id/extrato", response_model=GetExtractResponse)
def get_extract(id: int):

    client = {"limit": 100000, "saldo": -900, "date": datetime.now().isoformat()}
    return {
        "saldo": {
            "total": client["saldo"],
            "limite": client["limit"],
            "data_extrato": client["date"],
        },
        "ultimas_transacoes": [
            {
                "valor": 100,
                "tipo": "c",
                "descricao": "Salario",
                "realizada_em": datetime.now().isoformat(),
            },
            {
                "valor": 100,
                "tipo": "d",
                "descricao": "Mercado",
                "realizada_em": datetime.now().isoformat(),
            },
        ],
    }
