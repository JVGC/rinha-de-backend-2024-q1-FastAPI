from datetime import datetime
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.dialects.mysql import DATETIME
from src.database import Base


class Client(Base):
    __tablename__ = "client"

    id: int = Column(Integer, primary_key=True, index=True)
    limit: int = Column(Integer, default=1000)

    created_at: str = Column(DATETIME, default=datetime.now)
    updated_at: str = Column(DATETIME, default=datetime.now, onupdate=datetime.now)


class Transaction(Base):
    __tablename__ = "transaction"

    id: int = Column(Integer, primary_key=True, index=True)
    valor: int = Column(Integer)
    descricao: str = Column(String)
    tipo: str = Column(String)

    created_at: str = Column(DATETIME, default=datetime.now)
    updated_at: str = Column(DATETIME, default=datetime.now, onupdate=datetime.now)

    client_id: str = Column(Integer, ForeignKey("client.id"))
