import pygame
import utils
import menu
import conf
import sys
from enigmes import enigma_portes, enigma_codi, enigma_contrasenya

# Inicialització de Pygame
pygame.init()

# Configuració de la finestra
# pantalla = pygame.display.set_mode((utils.AMPLADA, utils.ALCADA))
pantalla = pygame.display.set_mode((0,0))
alcada, amplada = pantalla.get_size()

pygame.display.set_caption("ScapeRoom Programació")

# Carreguem el so
pygame.mixer.init()

# Carrega i reprodueix la cançó (loop infinit amb -1)
pygame.mixer.music.load(utils.resource_path("assets/Star_Wars_Main_Theme.mid"))  # O .ogg, .wav
pygame.mixer.music.set_volume(0.5)            # Volum entre 0.0 i 1.0
pygame.mixer.music.play(-1)                   # -1 = loop infinit

fons = pygame.image.load(utils.resource_path("assets/fons_intro.jpg"))
# fons = pygame.transform.scale(fons, (utils.AMPLADA, utils.ALCADA))
fons = pygame.transform.scale(fons, (alcada, amplada))

tipus_lletres = utils.defineix_tipus_lletra(pygame)

menu.menu_inicial(pygame, pantalla, fons, tipus_lletres)

# Definició enigmes
enigmes = conf.enigmes

#Iniciem el joc
for enigma in enigmes:
    if enigma["tipus"] == "HISTORIA":
        utils.mostra_missatge_central(pygame, pantalla, tipus_lletres, enigma["missatge"])
    elif enigma["tipus"] == "CONTRASENYA":
        resposta = enigma_contrasenya.executar(pygame, pantalla, tipus_lletres, enigma["missatge"], enigma["solucio"])
        if not resposta:
            utils.mostra_missatge_central(pygame, pantalla, tipus_lletres, "Has fallat... els soldats imperials t'han trobat...\n\n\nFI!")
            sys.exit()
    elif enigma["tipus"] == "PORTES":
        resposta = enigma_portes.executar(pygame, pantalla, tipus_lletres, enigma["missatge"], enigma["etiquetes"], enigma["correcta"])
        if not resposta:
            utils.mostra_missatge_central(pygame, pantalla, tipus_lletres, "Has fallat... els soldats imperials t'han trobat...\n\n\nFI!")
            sys.exit()
    elif enigma["tipus"] == "CODI":
        resposta = enigma_codi.executar(pygame, pantalla, tipus_lletres, enigma["missatge"], enigma["parametres"], enigma["funcions"], enigma["solucio"], enigma["min_chars_codi"], enigma["paraules_clau"])
        if not resposta:
            utils.mostra_missatge_central(pygame, pantalla, tipus_lletres, "Has fallat... els soldats imperials t'han trobat...\n\n\nFI!")
            sys.exit()
