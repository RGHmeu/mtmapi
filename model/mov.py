from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from  model import Base


class Mov(Base):
    __tablename__ = 'mov'

    id = Column("pk_mov", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    image = Column(String(140)) 
    texto = Column(String(4000))
    tipoTrab = Column(String(200))
    ParteCorpo = Column(String(200))
    data_insercao = Column(DateTime, default=datetime.now())


    def __init__(self, nome:str, image:str, texto:str, tipoTrab:str,
                 ParteCorpo: str,
                 data_insercao:Union[DateTime, None] = None):
    

        """
        Cria um Movimento

        Arguments:
            nome: nome do movimento.
            image: nome do gif animado
            texto: descrição do movimento.
            tipoTrab: tipo de trabalho muscular.
            ParteCorpo: parte do corpo focalizada.
            data_insercao: data de quando o movimento foi inserido à base
        """
        self.nome = nome
        self.image = image
        self.texto = texto
        self.tipoTrab = tipoTrab
        self.ParteCorpo = ParteCorpo
        if data_insercao:
            self.data_insercao = data_insercao
