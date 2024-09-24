from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from  model import Base


class Secao(Base):
    __tablename__ = 'secao'

    id = Column("pk_secao", Integer, primary_key=True)
    tempo = Column(String(140))
    latitude = Column(String(140)) 
    longiude = Column(String(140))

    def __init__(self, tempo:str, latitude:str, longitude:str):
    

        """
        Cria um registro de uso do aplicativo

        Arguments:
            tempo: momento em que foi utilizado.
            latitude: latitude do local do usuário.
            longitude: longitude do local do usuário.

        """
        self.tempo = tempo
        self.latitude = latitude
        self.longitude = longitude
 