from pydantic import BaseModel, EmailStr


class leitorCreate(BaseModel)
id: int
nome: str
email: EmailStr

class leitorOut(BaseModel) :
    id: int
    nome: str
    email: EmailStr