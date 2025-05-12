import sys
import os

# Mides de la finestra
AMPLADA = 1200
ALCADA = 800

TAMANY_LINIA = 30

# Colors
BLANC = (255, 255, 255)
NEGRE = (0, 0, 0)
GRIS = (200, 200, 200)
TERRA_FOSC = (50, 50, 50)
VERD_FOSC = (0, 100, 0)
VERD = (0, 255, 100)
VERMELL = (200, 0, 0)
GRIS_CLAR = (180, 180, 180)
GRIS_FOSC = (50, 50, 50)
TERRA_FOSC = (30, 20, 10)
BLAU_IMPERIAL = (10, 10, 80)

def defineix_tipus_lletra(pygame) :
    return {
        "titol": pygame.font.SysFont('Arial', 104, bold=True),
        "boto": pygame.font.SysFont('Arial', 36),
        "missatges": pygame.font.SysFont('Courier New', 24, bold=True),
        "etiqueta": pygame.font.SysFont('Arial', 20, bold=True),
        "input": pygame.font.SysFont('Arial', 28),
        "gran": pygame.font.SysFont("Arial", 60),
        "normal": pygame.font.SysFont("Arial", 36),
        "petita": pygame.font.SysFont("Arial", 24),
        "terminal": pygame.font.SysFont("Courier New", 40)
    }

def escoltar_events_windows(pygame, retard_text = 50):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Enter
                return 0
            elif event.key == pygame.K_SPACE:  # Espai
                return 0
    return retard_text
            
def dibuixar_caixa_text_lent(pygame, pantalla, tipus_lletres, missatge):
    missatge_amb_salts = dividir_text_en_linies(missatge)
    n_linies = len(missatge_amb_salts.split("\n"))
    caixa_text = pygame.Rect(50, ALCADA - 40 - n_linies*TAMANY_LINIA, AMPLADA - 100, TAMANY_LINIA + TAMANY_LINIA*n_linies)
    pygame.draw.rect(pantalla, (0, 100, 0), caixa_text) # Fons del rectangle
    pygame.draw.rect(pantalla, BLANC, caixa_text, 3) # Borde
    for i, linia in enumerate(missatge_amb_salts.split("\n")):
        escoltar_events_windows(pygame)
        escriu_text_lentament(pygame, pantalla, linia, tipus_lletres["missatges"], BLANC, caixa_text.x + 20, caixa_text.y +20 + i*TAMANY_LINIA)
    pygame.event.clear()

    return caixa_text

def dibuixa_text_amb_borde(pantalla, text, font, x, y, color_text, color_borde):
    text_surface = font.render(text, True, color_text)
    border_offsets = [(1,1), (1,-1), (-1,1), (-1,-1)]
    for ox, oy in border_offsets:
        borde_surface = font.render(text, True, color_borde)
        pantalla.blit(borde_surface, (x+ox, y+oy))
    pantalla.blit(text_surface, (x, y))

def escriu_text_lentament(pygame, pantalla, cadena, font, color, x, y, retard=50):
    text = ""
    for caracter in cadena:
        retard = escoltar_events_windows(pygame, retard)
        text += caracter
        render = font.render(text, True, color)
        # pantalla.fill((30, 30, 30), (x, y, AMPLADA - 100, 100))  # Esborra zona
        pantalla.blit(render, (x, y))
        pygame.display.update()
        pygame.time.delay(retard)
        
# def dividir_text_en_linies(text, max_len=71) :
#     linies = []
#     while len(text) > max_len:
#         # Si el caràcter 71 és un espai, tallem aquí
#         if text[max_len] == ' ':
#             linies.append(text[:max_len])
#             text = text[max_len+1:]
#         else:
#             # Busquem l'espai anterior més proper
#             pos = text.rfind(' ', 0, max_len)
#             if pos == -1:
#                 # Si no hi ha espai, tallem directament
#                 linies.append(text[:max_len])
#                 text = text[max_len:]
#             else:
#                 linies.append(text[:pos])
#                 text = text[pos+1:]
#     # Afegim la resta del text
#     print(linies)
#     if text:
#         linies.append(text)
#     return '\n'.join(linies)
def dividir_text_en_linies(text, max_len=71):
    linies = []
    # Primer, dividim pel salt de línia original
    paragrafs = text.split('\n')
    for paragraf in paragrafs:
        while len(paragraf) > max_len:
            if paragraf[max_len] == ' ':
                linies.append(paragraf[:max_len])
                paragraf = paragraf[max_len+1:]
            else:
                pos = paragraf.rfind(' ', 0, max_len)
                if pos == -1:
                    linies.append(paragraf[:max_len])
                    paragraf = paragraf[max_len:]
                else:
                    linies.append(paragraf[:pos])
                    paragraf = paragraf[pos+1:]
        if paragraf:
            linies.append(paragraf)
    return '\n'.join(linies)


    
def mostra_missatge_central(pygame, pantalla, tipus_lletres, missatge, color=BLANC):
    pantalla.fill(NEGRE)
    x = 100
    y = ALCADA // 2 - 20
    missatge_amb_salts = dividir_text_en_linies(missatge)
    n_linies = len(missatge_amb_salts.split("\n"))
    caixa_text = pygame.Rect(50, 120, AMPLADA - 100, TAMANY_LINIA*(n_linies+1))
    redard_text = 50
    for i, linia in enumerate(missatge_amb_salts.split("\n")):
        retard_text = escoltar_events_windows(pygame, redard_text)
        escriu_text_lentament(pygame, pantalla, linia, tipus_lletres["missatges"], color, caixa_text.x + 20, caixa_text.y +20 + i*TAMANY_LINIA, retard_text)
        
    pygame.event.clear()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return True
            
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)