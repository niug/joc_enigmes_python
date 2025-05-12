from utils import dibuixa_text_amb_borde, AMPLADA, ALCADA, BLANC, NEGRE, GRIS, VERD_FOSC

def menu_inicial(pygame, pantalla, fons, tipus_lletres):
    boto_recte = pygame.Rect(AMPLADA // 2 - 100, ALCADA // 2 + 50, 200, 60)
    
    en_menu = True
    while en_menu:
        pantalla.blit(fons, (0, 0))

        # Títol
        pygame.draw.rect(pantalla, NEGRE, (AMPLADA // 4 -50, ALCADA//2-220, AMPLADA // 2 + 130, 300))
        dibuixa_text_amb_borde(pantalla, "Scape Room", tipus_lletres["titol"], AMPLADA // 4 +6, ALCADA//2-200, BLANC, NEGRE)
        dibuixa_text_amb_borde(pantalla, "Programació", tipus_lletres["titol"], AMPLADA // 4 , ALCADA//2-90, BLANC, NEGRE)

        # Dibuixa el botó
        pygame.draw.rect(pantalla, GRIS, boto_recte)
        text_boto = tipus_lletres["boto"].render("Iniciar el joc", True, NEGRE)
        pantalla.blit(text_boto, (boto_recte.x + 25, boto_recte.y + 10))

        for esdeveniment in pygame.event.get():
            if esdeveniment.type == pygame.QUIT:
                pygame.quit()
                #sys.exit()
                return
            elif esdeveniment.type == pygame.MOUSEBUTTONDOWN:
                if boto_recte.collidepoint(esdeveniment.pos):
                    en_menu = False  # Sortim del menú per començar el joc

        pygame.display.flip()