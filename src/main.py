from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from src.operations import create_client_db, create_transaction_db, get_client_by_id


from src.schemas import (
    CreateTransactionPostBody,
    CreateTransactionResponse,
    GetExtractResponse,
)
from src.database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)


def insert_initial_data():

    db = SessionLocal()
    if get_client_by_id(db, 5):
        return
    create_client_db(db, {"limit": 100000})
    create_client_db(db, {"limit": 80000})
    create_client_db(db, {"limit": 1000000})
    create_client_db(db, {"limit": 10000000})
    create_client_db(db, {"limit": 500000})
    db.close()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

insert_initial_data()


@app.post(
    "/clients/:id/transacoes",
    response_model=CreateTransactionResponse,
    responses={
        404: {
            "description": "Client not found",
            "content": {
                "application/json": {"example": {"detail": "Client not found"}}
            },
        },
    },
)
def create_transaction(
    id: int, transaction: CreateTransactionPostBody, db: Session = Depends(get_db)
):

    client = get_client_by_id(db, id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    create_transaction_db(
        db,
        {
            "client_id": id,
            "valor": transaction.valor,
            "descricao": transaction.descricao,
            "tipo": transaction.tipo,
        },
    )

    return {
        "limite": client.limit,
        "saldo": client.balance,
    }


@app.get("/clients/:id/extrato", response_model=GetExtractResponse)
def get_extract(id: int, db: Session = Depends(get_db)):

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
