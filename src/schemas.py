from enum import Enum
from pydantic import BaseModel


class TipoEnum(str, Enum):
    credit = "c"
    debit = "d"


class CreateTransactionPostBody(BaseModel):
    valor: int
    tipo: TipoEnum
    descricao: str


class CreateTransactionResponse(BaseModel):
    limite: int
    saldo: int


class Balance(BaseModel):
    total: int
    data_extrato: str
    limite: int


class Transaction(BaseModel):
    valor: int
    tipo: TipoEnum
    descricao: str
    realizada_em: str


class GetExtractResponse(BaseModel):
    saldo: Balance
    ultimas_transacoes: list[Transaction]
