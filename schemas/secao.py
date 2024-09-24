from unicodedata import category
from pydantic import BaseModel
from typing import Optional, List


class SecaoSchema(BaseModel):
    tempo: str = "012031283"
    latitude: Optional[str] = "8734634705"
    longitude: Optional[str] = "3945394858"


class SecaoBuscaSchema(BaseModel):
    id: Optional[int] = 1
    tempo: Optional[str] = "837447456"


class SecaoViewSchema(BaseModel):
    id: int = 1
    tempo: str = "012031283"
    latitude: Optional[str] = "8734634705"
    longitude: Optional[str] = "3945394858"

class SecaoDelSchema(BaseModel):
    mesage: str
    id: int

def apresenta_secao(secao):
    nota_media = 0
     
    return {
        "id": secao.id,
        "tempo": secao.tempo,
        "latitude": secao.latitude,
        "longitude": secao.longitude,

    }


class SecaoListaViewSchema(BaseModel):
    secaos: List[SecaoViewSchema]


def apresenta_lista_secao(secaos):
    result = []
    for secao in secaos:
        result.append(apresenta_secao(secao))
    return {"secaos": result}