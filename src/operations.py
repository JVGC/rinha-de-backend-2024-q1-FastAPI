from sqlalchemy.orm import Session
from src.models import Client, Transaction


def get_client_by_id(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()


def create_transaction_db(db: Session, data: dict):
    transaction = Transaction(**data)
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction


def create_client_db(db: Session, data: dict):
    client = Client(**data)
    db.add(client)
    db.commit()
    db.refresh(client)
    return client
