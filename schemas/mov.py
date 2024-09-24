from unicodedata import category
from pydantic import BaseModel
from typing import Optional, List


class MovSchema(BaseModel):
    nome: str = "HalteresRem0001"
    image: str = "halteresRem0001"
    texto: Optional[str] = "Sobe rápido e desce devagar. "
    tipoTrab: str = "Musculacao"
    ParteCorpo: str = "Braços"


class MovBuscaSchema(BaseModel):
    id: Optional[int] = 11
    nome: Optional[str] = "HalteresRem0001"


class MovViewSchema(BaseModel):
    id: int = 11
    nome: str = "HalteresRem0001"
    image: str = "halteresRem0001"
    texto: Optional[str] = "Sobe rápido e desce devagar. "
    tipoTrab: str = "Musculacao"
    ParteCorpo: str = "Ombros"
   
class MovDelSchema(BaseModel):
    mesage: str
    id: int

def apresenta_mov(mov):
    nota_media = 0
     
    return {
        "id": mov.id,
        "image": mov.image,
        "nome": mov.nome,
        "tipoTrab": mov.tipoTrab,
        "ParteCorpo": mov.ParteCorpo,
        "texto": mov.texto,

    }

def atualiza_mov(mov):
    nota_media = 0
     
    return {
        "id": mov.id,
        "image": mov.image,
        "nome": mov.nome,
        "tipoTrab": mov.tipoTrab,
        "ParteCorpo": mov.ParteCorpo,
        "texto": mov.texto,

    }


class MovListaViewSchema(BaseModel):
    movs: List[MovViewSchema]


def apresenta_lista_mov(movs):
    result = []
    for mov in movs:
        result.append(apresenta_mov(mov))
    return {"movs": result}