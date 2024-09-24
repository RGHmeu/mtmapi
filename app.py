from email.mime import base
from sqlalchemy.exc import IntegrityError

from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI
from flask_cors import CORS
from flask import redirect
from model import Session, Mov, Secao
from logger import logger
from schemas import *


info = Info(title="Minha querida API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
mov_tag = Tag(name="Mov", description="Adição, visualização, alteração e remoção de movimentos à base")
secao_tag = Tag(name="Secao", description="Adição de registros de uso do aplicativo à base")


@app.get('/')
def home():
    return redirect('/openapi')


@app.post('/mov', tags=[mov_tag],
          responses={"200": MovViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_mov(form: MovSchema):
    """Adiciona um novo Movimento à base de dados

    Retorna uma representação dos movimentos e comentários associados.
    """
    session = Session()
    mov = Mov(
        nome=form.nome,
        image=form.image,
        texto=form.texto,
        tipoTrab=form.tipoTrab,
        ParteCorpo=form.ParteCorpo
        )
    logger.debug(f"Adicionando movimento de nome: '{mov.nome}'")
    try:
        # adicionando movimento
        session.add(mov)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado movimento de nome: '{mov.nome}'")
        return apresenta_mov(mov), 200
    except IntegrityError as e:
        error_msg = "Movimento de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar movimento '{mov.nome}', {error_msg}")
        return {"mesage": error_msg}, 409
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar movimento '{mov.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/mov', tags=[mov_tag],
         responses={"200": MovViewSchema, "404": ErrorSchema})
def get_mov(query: MovBuscaSchema):
    """Faz a busca por um Movimento a partir do id do movimento

    Retorna uma representação dos movimentos e comentários associados.
    """
    mov_id = query.id
    logger.debug(f"Coletando dados sobre movimento #{mov_id}")
    session = Session()
    mov = session.query(Mov).filter(Mov.id == mov_id).first()
    if not mov:
        error_msg = "Movimento não encontrado na base :/"
        logger.warning(f"Erro ao buscar movimento '{mov_id}', {error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(f"Movimento econtrado: '{mov.nome}'")
        return apresenta_mov(mov), 200


@app.get('/movs', tags=[mov_tag],
         responses={"200": MovListaViewSchema, "404": ErrorSchema})
def get_movs():
    """Lista todos os movimentos cadastrados na base

    Retorna uma lista de representações de movimentos.
    """
    logger.debug(f"Coletando lista de movimentos")
    session = Session()
    movs = session.query(Mov).all()
    print(movs)
    if not movs:
        error_msg = "Movimento não encontrado na base :/"
        logger.warning(f"Erro ao buscar por lista de movimentos. {error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(f"Retornando lista de movimentos")
        return apresenta_lista_mov(movs), 200


@app.delete('/mov', tags=[mov_tag],
            responses={"200": MovDelSchema, "404": ErrorSchema})
def del_mov(query: MovBuscaSchema):
    """Deleta um Movimento a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    mov_id = query.id
    mov_nome = query.nome

    logger.debug(f"Deletando dados sobre movimento #{mov_id}")
    session = Session()

    if mov_id:
        count = session.query(Mov).filter(Mov.id == mov_id).delete()
    else:
        count = session.query(Mov).filter(Mov.nome == mov_nome).delete()

    session.commit()
    if count:
        logger.debug(f"Deletado movimento #{mov_id}")
        return {"mesage": "Movimento removido", "id": mov_id}
    else: 
        error_msg = "Movimento não encontrado na base :/"
        logger.warning(f"Erro ao deletar movimento #'{mov_id}', {error_msg}")
        return {"mesage": error_msg}, 400

@app.put('/mov', tags=[mov_tag],
	responses={"200": MovViewSchema, "404": ErrorSchema})

def atualiza_mov(form: MovSchema):
    """ Altera alguns atributos de um movimento na base

    Retorna mensagem de movimento alterado
    """
    mov_nome  =  form.nome

	# criando conecção com a base
    session = Session()
	# fazendo a busca pelo movimento
    mov = session.query(Mov).filter(Mov.nome == mov_nome).first()

    if not mov:
		# se movimento não encontrado
        error_msg = "Movimento a ser alterado não encontrado na base: /"
        logger.warning(f"Erro ao alterar dados do movimento '{mov_nome}', {error_msg}")

	# atualiza movimento
    mov.nome = form.nome
    mov.texto = form.texto
    mov.image = form.image
    mov.tipoTrab = form.tipoTrab
    mov.ParteCorpo = form.ParteCorpo
	# alterando os dados do produto
    session.commit()
    return apresenta_mov(mov), 200


@app.post('/secao', tags=[secao_tag],
          responses={"200": SecaoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_secao(form: SecaoSchema):
    """Adiciona um novo registro à base de dados

    Retorna uma representação dos dados informados.
    """
    session = Session()
    secao = Secao(
        tempo=form.tempo,
        latitude=form.latitude,
        longitude=form.longitude,
        )
#    logger.debug(f"Adicionando registro de secao")
    try:
#        # adicionando registro de uso do aplicativo
        session.add(secao)
#        # efetivando o camando de adição de novo item na tabela
        session.commit()
#        logger.debug(f"Registro adicionado.")
        return apresenta_secao(secao), 200
#    
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
#        logger.warning(f"Erro ao adicionar registro, {error_msg}")
        return {"mesage": error_msg}, 400
#    print("Put call")
#    print(form.tempo)
#    print(form.latitude)
#    print(form.longitude)
#    return {"data": "teste"}, 200

