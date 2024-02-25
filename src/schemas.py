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
