import utils
import sys

def render_etiqueta(pantalla, tipus_lletres, etiqueta, x, y):
    linies = etiqueta.split("\n")
    y_offset = 0
    for linia in linies:
        etiqueta = tipus_lletres["etiqueta"].render(linia, True, utils.BLANC)
        pantalla.blit(etiqueta, (x, y + y_offset))
        y_offset += etiqueta.get_height() + 5  # espai entre línies
        
def executar(pygame, pantalla, tipus_lletres, missatge, etiquetesPortes, nPortaCorrecta):
    paret = pygame.image.load(utils.resource_path("assets/grey_bricks.jpg"))
    altura_paret = int(utils.ALCADA * 0.45)
    paret = pygame.transform.scale(paret, (utils.AMPLADA, altura_paret))

    pantalla.blit(paret, (0, 0))
    altura_terra = utils.ALCADA - altura_paret
    pygame.draw.rect(pantalla, utils.TERRA_FOSC, (0, altura_paret, utils.AMPLADA, altura_terra))

    porta_amplada = 220
    porta_alcada = 270
    y_porta = altura_paret - porta_alcada
    portes = {
        "1": pygame.Rect(utils.AMPLADA//6 - porta_amplada//2, y_porta, porta_amplada, porta_alcada),
        "2": pygame.Rect(utils.AMPLADA//2 - porta_amplada//2, y_porta, porta_amplada, porta_alcada),
        "3": pygame.Rect(5*utils.AMPLADA//6 - porta_amplada//2, y_porta, porta_amplada, porta_alcada),
    }

    pygame.draw.rect(pantalla, (122, 115, 110), portes["1"])
    pygame.draw.rect(pantalla, (122, 115, 110), portes["2"])
    pygame.draw.rect(pantalla, (122, 115, 110), portes["3"])

    render_etiqueta(pantalla, tipus_lletres, etiquetesPortes[0], portes["1"].centerx - 100, portes["1"].y + 25)
    render_etiqueta(pantalla, tipus_lletres, etiquetesPortes[1], portes["2"].centerx - 100, portes["2"].y + 25)
    render_etiqueta(pantalla, tipus_lletres, etiquetesPortes[2], portes["3"].centerx - 100, portes["3"].y + 25)

    utils.dibuixar_caixa_text_lent(pygame, pantalla, tipus_lletres, missatge)

    pygame.display.flip()

    espera = True
    while espera:
        for esdeveniment in pygame.event.get():
            if esdeveniment.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif esdeveniment.type == pygame.MOUSEBUTTONDOWN:
                for portaId in portes.keys():
                    if portes[portaId].collidepoint(esdeveniment.pos) :
                        if portaId == str(nPortaCorrecta) :
                            return True
                        else :
                            return False