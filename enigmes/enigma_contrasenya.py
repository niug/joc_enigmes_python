import pygame
import sys
import utils

def mostrar_text_contrasenya(pygame, pantalla, tipus_lletres, input_rect, max_caracters, contrasenya) :
    pygame.draw.rect(pantalla, utils.GRIS_CLAR, input_rect, border_radius=10)
    text_contrasenya = " ".join(["*" if i < len(contrasenya) else "_" for i in range(max_caracters)])
    text_render = tipus_lletres["gran"].render(text_contrasenya, True, utils.NEGRE)
    pantalla.blit(text_render, (input_rect.centerx - text_render.get_width() // 2, input_rect.centery - text_render.get_height() // 2))

def executar(pygame, pantalla, tipus_lletres, missatge, solucio):
    contrasenya = ""
    max_caracters = 6
    input_rect = pygame.Rect(utils.AMPLADA // 2 - 150, utils.ALCADA // 2 - 40, 300, 80)
    boto_borrar = pygame.Rect(utils.AMPLADA // 2 + 170, utils.ALCADA // 2 - 40, 100, 35)
    boto_enviar = pygame.Rect(utils.AMPLADA // 2 + 170, utils.ALCADA // 2 + 10, 100, 35)
    
    espera = True
    pantalla.fill((30, 30, 30))

    # Dibuixar rectangle d'entrada
    mostrar_text_contrasenya(pygame, pantalla, tipus_lletres, input_rect, max_caracters, contrasenya)

    # Dibuixar botons
    pygame.draw.rect(pantalla, utils.VERMELL, boto_borrar, border_radius=8)
    boto_text = tipus_lletres["petita"].render("Borrar", True, utils.BLANC)
    pantalla.blit(boto_text, (boto_borrar.centerx - boto_text.get_width() // 2, boto_borrar.centery - boto_text.get_height() // 2))

    pygame.draw.rect(pantalla, utils.VERD, boto_enviar, border_radius=8)
    boto_text2 = tipus_lletres["petita"].render("Enviar", True, utils.BLANC)
    pantalla.blit(boto_text2, (boto_enviar.centerx - boto_text2.get_width() // 2, boto_enviar.centery - boto_text2.get_height() // 2))

    # Missatge inferior
    utils.dibuixar_caixa_text_lent(pygame, pantalla, tipus_lletres, missatge)
    pygame.display.flip()

    while espera:
        for esdeveniment in pygame.event.get():
            if esdeveniment.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif esdeveniment.type == pygame.KEYDOWN:
                if esdeveniment.key == pygame.K_BACKSPACE:
                    contrasenya = contrasenya[:-1]
                elif len(contrasenya) < max_caracters and esdeveniment.unicode.isprintable():
                    contrasenya += esdeveniment.unicode
                mostrar_text_contrasenya(pygame, pantalla, tipus_lletres, input_rect, max_caracters, contrasenya)
                pygame.display.flip()
            elif esdeveniment.type == pygame.MOUSEBUTTONDOWN:
                if boto_borrar.collidepoint(esdeveniment.pos):
                    contrasenya = ""
                    mostrar_text_contrasenya(pygame, pantalla, tipus_lletres, input_rect, max_caracters, contrasenya)
                    pygame.display.flip()
                elif boto_enviar.collidepoint(esdeveniment.pos):
                    return contrasenya == solucio
