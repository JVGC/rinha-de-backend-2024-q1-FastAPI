from fastapi import FastAPI

from src.schemas import CreateTransactionPostBody, CreateTransactionResponse

app = FastAPI()


@app.post("/clients/:id/transacoes", response_model=CreateTransactionResponse)
def create_transaction(id: int, transaction: CreateTransactionPostBody):

    client = {"limit": 100000, "saldo": -900}
    return {
        "limite": client["limit"],
        "saldo": client["saldo"],
    }
