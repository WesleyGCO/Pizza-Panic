from application.models.FaseUm import FaseUm
from application.models.FaseDois import FaseDois
from application.models.FaseTres import FaseTres
from application.models.FaseQuatro import FaseQuatro
from application.models.FaseCinco import FaseCinco
from core.services.fase_service import FaseService


def setar_fase(jogo_model, numero_fase):
    jogo_model.fase_atual = numero_fase
    
def criar_fase(numero_fase, personagem, itens_ruins):
    if (numero_fase == 1):
        return FaseUm(1, personagem, itens_ruins, 30)
    elif (numero_fase == 2):
        return FaseDois(2, personagem, itens_ruins, 45)
    elif (numero_fase == 3):
        return FaseTres(3, personagem, itens_ruins, 60)
    elif (numero_fase == 4):
        return FaseQuatro(4, personagem, itens_ruins, 75)
    elif (numero_fase == 5):
        return FaseCinco(5, personagem, itens_ruins, 90)

def iniciar_fase(jogo_model, jogo_ui, fase_ui, item_service, personagem_service):
    prox_fase = False
    
    rodar_menu_fase = True
    while rodar_menu_fase:
        if (jogo_model.fase_atual == 1):
            fase_um = criar_fase(1, jogo_ui.personagem, jogo_ui.itens_ruins)
            fase_service = FaseService(fase_um, fase_ui, item_service, personagem_service)
            fase_service.iniciar()

            if (fase_um.concluida):
                fase_um.concluir()
                prox_fase = True
                if (prox_fase):
                    numero_fase = 2
                    jogo_ui.rodar_menu_fase(jogo_model, numero_fase)

        if (jogo_model.fase_atual == 2):
            fase_dois = criar_fase(2, jogo_ui.personagem, jogo_ui.itens_ruins)
            fase_service = FaseService(fase_dois, fase_ui, item_service, personagem_service)
            fase_service.iniciar()

            if (fase_dois.concluida):
                fase_dois.concluir()
                prox_fase = True
                if (prox_fase):
                    numero_fase = 3
                    jogo_ui.rodar_menu_fase(jogo_model, numero_fase)

        if (jogo_model.fase_atual == 3):
            fase_tres = criar_fase(3, jogo_ui.personagem, jogo_ui.itens_ruins)
            fase_service = FaseService(fase_tres, fase_ui, item_service, personagem_service)
            fase_service.iniciar()

            if (fase_tres.concluida):
                fase_tres.concluir()
                prox_fase = True
                if (prox_fase):
                    numero_fase = 4
                    jogo_ui.rodar_menu_fase(jogo_model, numero_fase)

        if (jogo_model.fase_atual == 4):
            fase_quatro = criar_fase(4, jogo_ui.personagem, jogo_ui.itens_ruins)
            fase_service = FaseService(fase_quatro, fase_ui, item_service, personagem_service)
            fase_service.iniciar()

            if (fase_quatro.concluida):
                fase_quatro.concluir()
                prox_fase = True
                if (prox_fase):
                    numero_fase = 5
                    jogo_ui.rodar_menu_fase(jogo_model, numero_fase)

        if (jogo_model.fase_atual == 5):
            fase_cinco = criar_fase(5, jogo_ui.personagem, jogo_ui.itens_ruins)
            fase_service = FaseService(fase_cinco, fase_ui, item_service, personagem_service)
            fase_service.iniciar()

            if (fase_cinco.concluida):
                fase_cinco.concluir()
                prox_fase = True
                if (prox_fase):
                    numero_fase = 6
                    setar_fase(jogo_model, numero_fase)

def verificar_conclusao_fase(fase_model):
    if fase_model.pedido == fase_model.pedido_coletado:
        fase_model.concluida = True