import utils
import io
import contextlib
import sys

def dibuixar_pc(pygame, pantalla):
    # Dibuixa una pantalla de PC amb marc
    pantalla_pc = pygame.Rect(utils.AMPLADA//2 + 20, 80, 500, 320)
    marc_pc = pygame.Rect(pantalla_pc.x - 10, pantalla_pc.y - 10, 520, 340)
    pygame.draw.rect(pantalla, (80, 80, 80), marc_pc)  # Marc de la pantalla
    pygame.draw.rect(pantalla, (0, 30, 0), pantalla_pc)  # Pantalla verda fosca
    pygame.draw.rect(pantalla, utils.BLANC, pantalla_pc, 2)
    return pantalla_pc
 
def mostrar_entrada(pygame, pantalla, input_text, tipus_lletres) :
    caixa_input = pygame.Rect(50, 80, 500, 400)
    pygame.draw.rect(pantalla, (50, 50, 100), caixa_input)
    pygame.draw.rect(pantalla, utils.BLANC, caixa_input, 2)

    input_lines = input_text.split("\n")
    for i, linia in enumerate(input_lines):
        input_surface = tipus_lletres["input"].render(linia, True, utils.BLANC)
        pantalla.blit(input_surface, (caixa_input.x + 10, caixa_input.y + 10 + i * 28))
      
def mostrar_resultat(pygame, pantalla, resultat_execucio, tipus_lletres):
    pantalla_pc = dibuixar_pc(pygame, pantalla)
    resultat_lines = resultat_execucio.split("\n") if resultat_execucio else [""]
    for i, linia in enumerate(resultat_lines):
        render = tipus_lletres["input"].render(linia, True, (0, 255, 0))
        pantalla.blit(render, (pantalla_pc.x + 10, pantalla_pc.y + 10 + i * 28)) 
        
def executar(pygame, pantalla, tipus_lletres, missatge, parametres, funcions, solucio, min_chars_codi, paraules_clau):
    input_text = "Escriu el codi en Python:"
    resultat_execucio = ""
    entrada_activa = True
    boto_play = pygame.Rect(600, 450, 175, 40)
    
    pantalla.fill((30, 30, 30))

    mostrar_entrada(pygame, pantalla, input_text, tipus_lletres)
    mostrar_resultat(pygame, pantalla, resultat_execucio, tipus_lletres)

    pygame.draw.rect(pantalla, utils.GRIS, boto_play)
    play_text = tipus_lletres["input"].render("Executa el codi", True, utils.NEGRE)
    pantalla.blit(play_text, (boto_play.x + 10, boto_play.y + 5))
    
    utils.dibuixar_caixa_text_lent(pygame, pantalla, tipus_lletres, missatge)

    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and entrada_activa:
                if ("Escriu el codi en Python:" == input_text) :
                    input_text = ""
                if event.key == pygame.K_RETURN:
                    input_text += "\n"
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
                mostrar_entrada(pygame, pantalla, input_text, tipus_lletres)
                pygame.display.flip()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boto_play.collidepoint(event.pos):
                    mostrar_resultat(pygame, pantalla, "Carregant...", tipus_lletres)
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    try:
                        output = io.StringIO()
                        with contextlib.redirect_stdout(output):
                            codi_total = ""
                            for k, v in parametres.items():
                                codi_total += str(k) + "=\""+str(v)+"\"\n"
                            codi_total += input_text
                            exec(codi_total, funcions)
                        resultat_execucio = output.getvalue()
                    except Exception as e:
                        resultat_execucio = str(e)
                    mostrar_resultat(pygame, pantalla, resultat_execucio, tipus_lletres)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    
                    if resultat_execucio == solucio:
                        solucioAmbPrint = "print(\"" + solucio + "\")"
                        if input_text != solucioAmbPrint and len(input_text) > min_chars_codi and all(paraula in input_text for paraula in paraules_clau):
                            return True
                        else :
                            print("Falla el segon if::"+str(input_text != solucioAmbPrint)+str(len(input_text) > min_chars_codi)+str(all(paraula in input_text for paraula in paraules_clau)))
                    else :
                        print("Falla el primer if"+str(resultat_execucio == solucio))
                    print("Solució incorrecte:")
                    return False
                    pygame.display.flip()