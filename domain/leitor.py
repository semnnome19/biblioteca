from dataclasses import dataclass 
@dataclass(frozen=true)
class Leitor:
    id: int
    nome: str
    email: str