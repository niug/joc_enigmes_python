
import random
enigmes = [
    {
        "tipus": "HISTORIA",
        "missatge": "Any 12 ABY (després de la Batalla de Yavin)\n\nLa galàxia encara tremola sota l'ombra de l'Imperi. Tot i la caiguda de l'Emperador, una nova facció imperial ha ressorgit de les cendres i construeix en secret una nova arma devastadora: l'Estrella Negra.\n\nTu formes part d'un esquadró rebel d'elit. Has estat capturat durant una missió d'infiltració i ara estàs reclòs dins d'una base secreta imperial.\n\nEl teu droide K1T-7 ha aconseguit infiltrar-se al sistema i ha bloquejat els protocols de seguretat… però només temporalment.\n\nTens 45 minuts abans que tornin a activar-se els escuts i siguis detectat. L'única manera d'escapar és superar 10 proves codificades pels enginyers imperials: portes xifrades, mapes estel·lars, droides de vigilància...\n\nLa Força està amb tu... però el codi és l'únic que pot salvar-te.\n\nSupera els enigmes. Troba la sortida. I salva la galàxia.\n\n\nContinuar."
    },
    {
        "tipus": "CONTRASENYA",
        "missatge": "ENIGMA 1:\nEl teu droide K1T-7 ha aconseguit connectar-se a un antic terminal dins la cel·la. Amb accés limitat, només pot enviar-te fragments de codi per ajudar-te a obrir la porta blindada.\n\na = \"13\" + str(22) + \"a\"\nb = \"22\" * 2\nc = 9\npassword = \"a\" + b + str(c)",
        "solucio": "a22229"
    },
    {
        "tipus": "HISTORIA",
        "missatge": "PASSWORD CORRECTE!\n\nHas escapat de la cel·la i pel camí has neutralitzat un soldat imperial. Agafes la seva targeta d'identificació: CT-9012. Arribes a una sala amb un terminal bloquejat. El teu droide K1T-7 detecta que el sistema comprova si l'ID del soldat és autoritzada mitjançant una condició if.\n\nEt diu que la ID mestra que obre totes les portes és: IS342RRT. Només has de modificar el codi perquè el sistema pensi que tens aquesta identificació."
    },
    {
        "tipus": "CODI",
        "missatge": "ENIGMA 2:\nEn el terminal de l'esquerra introdueix el codi de la sentència condicional if que comprovi si la variable soldat_id és igual a IS342RRT. Si és igual ha d'imprimir per pantalla:\nDesbloquejant totes les portes...\nPORTES DESBLOQUEJADES",
        "parametres": {"soldat_id": "IS342RRT", "categoria": "soldat"},
        "funcions": {},
        "solucio": "Desbloquejant totes les portes...\nPORTES DESBLOQUEJADES\n",
        "min_chars_codi": 90,
        "paraules_clau": ["if", "print", "=="]
    },
    {
        "tipus": "HISTORIA",
        "missatge": "CODI CORRECTE!\n\nHas travessat els passadissos de seguretat i arribes a una estació de control on tres portes bloquegen l'accés als túnels de ventilació. Cada porta està protegida per sensors biomètrics que analitzen dues dades: la temperatura corporal i la freqüència cardíaca."
    },
    {
        "tipus": "PORTES",
        "missatge": "ENIGMA 3:\nK1T-7 ha obtingut el codi de validació del sistema:\nif temperatura < 36.5 or pulsacions > 100:\n    porta = \"1\"\nelif temperatura > 38 or pulsacions < 60:\n    porta = \"3\"\nelse:\n    porta = \"2\"\n\nLa teva temperatura és: 36.8 i tens les pulsacions a: 81\nEscull la porta correcta perquè no salti l'alarma!",
        "etiquetes": ["Porta 1", "Porta 2", "Porta 3"],
        "correcta": 2
    },
    {
        "tipus": "HISTORIA",
        "missatge": "PORTA CORRECTA!\n\nDesprés de creuar la porta blindada, accedeixes a una estació de control d'hologrames. Per activar el pont de llum que et permetrà continuar, has d'introduir una ordre que generi un patró d'alineació perfectament simètric: el triangle d'asteriscs imperials.\n\nK1T-7 et xiuxiueja pel comunicador:\n“El sistema necessita veure l'estructura triangular. Si no és exacta, no obrirà pas...”\n\nA la pantalla apareix aquest missatge:\n\n\"Escriu un codi que imprimeixi un triangle d'asteriscs de 6 línies, començant amb 1 asterisc i afegint-ne un més per línia.\""
    },
    {
        "tipus": "CODI",
        "missatge": "ENIGMA 4:\nFes servir un bucle for per imprimir aquest patró exactament com es mostra:\n*\n**\n***\n****\n*****\n******",
        "parametres": {},
        "funcions": {},
        "solucio": "*\n**\n***\n****\n*****\n******\n",
        "min_chars_codi": 30,
        "paraules_clau": ["for", "print", "range"]
    },
    {
        "tipus": "HISTORIA",
        "missatge": "CODI CORRECTE!\n\nTravesses el pont de llum que acabes d'activar. Els teus passos ressonen en una estança ampla i fosca. Al fons, tres portes metàl·liques apareixen il·luminades amb una llum vermellosa. Cadascuna té un petit panell amb un fragment de codi Python projectat sobre la superfície.\n\nK1T-7 s'apropa i xiuxiueja mentre escaneja els codis:\n\n\"Aquestes portes no s'obren amb claus físiques... Són part d'un sistema antic de validació per codi Python.\"\n\"Cada porta té associat un petit bucle for. Només una genera la seqüència correcta per obrir el camí cap al nucli de comandament.\""
    },
    {
        "tipus": "PORTES",
        "missatge": "ENIGMA 5:\n\"Segons els registres antics,\" diu K1T-7, \"el codi correcte ha de mostrar els nombres del 1 al 5... ni més, ni menys.\"",
        "etiquetes": ["for i in range(5):\n    print(i)", "for i in range(6):\n    print(i + 1)", "for i in range(1, 6):\n    print(i)"],
        "correcta": 3
    },
    {
        "tipus": "HISTORIA",
        "missatge": "PORTA CORRECTA!\n\nDesprés d'analitzar el mapa estel·lar, K1T-7 detecta una llançadora imperial operativa. Podries escapar amb ella… però té un sistema antic de seguretat que no accepta cap identificació. Només pots accedir si saps el codi de 3 dígits.\n\n\"És un sistema obsolet\", xiuxiueja K1T-7, \"La força bruta pot funcionar... \"\n\nLa contrasenya pot ser un nombre entre 100 i 999. Cada vegada que introdueixes una combinació, el sistema et diu si has encertat... o no."
    },
    {
        "tipus": "CODI",
        "missatge": "ENIGMA 6:\nEscriu un programa que provi totes les contrasenyes possibles des de 100 fins a 999. La contrasenya correcta està guardada a la variable password. Utilitza un bucle while per anar provant números un a un, fins que trobis la contrasenya correcta. Un cop trobada la contrasenya mostra-la per pantalla. ATENCIÓ: El sistema guarda la contrasenya amb una cadena de text, només així la podràs comparar.",
        "parametres": {"password": 199},
        "funcions": {},
        "solucio": "199\n",
        "min_chars_codi": 30,
        "paraules_clau": ["while", "!="]
    },
    {
        "tipus": "HISTORIA",
        "missatge": "CODI CORRECTE!\n\nLa nau imperial és operativa, però per poder activar els motors i enlairar-te, necessites introduir el codi d'arrencada, un codi secret de 6 caràcters alfanumèrics. K1T-7 connecta el seu port de diagnòstic a la consola i, després d'uns segons, xiuxiueja:\"He trobat fragments del codi... Sembla que cada caràcter del codi té una pista...\""
    },
    {
        "tipus": "CONTRASENYA",
        "missatge": "ENIGMA 7:\nHas de descobrir la contrasenya resolent les següents pistes:\n'int(\"22\" * 2) // 1111'\n'\"Python\"[5]'\n'\"CATALUNYA\"[2]'\n'\"_\"'\n'str(18 // 2)'\n'\"roBOt\".lower()[2]\n",
        "solucio": "2nT_9b"
    },
    {
        "tipus": "HISTORIA",
        "missatge": "CODI CORRECTE!\n\nAmb la llançadora imperial a punt per enlairar-se, el panell central et demana executar una seqüència específica de protocols.\n\nK1T-7 connecta amb el sistema i et mostra una pantalla negra amb un missatge tècnic:\n\n\"Només els qui sàpiguen com cridar ordres específiques podran activar els motors.\"\n\nUna llum vermella comença a parpellejar. El temps s'esgota..."
    },
    {
        "tipus": "CODI",
        "missatge": "ENIGMA 8:\nInvoca les tres següents funcions en l'ordre correcte per arrancar el sistema:\ndef preparar_combustible()\ndef activar_motors()\ndef llancament()",
        "parametres": {},
        "funcions": {"preparar_combustible": lambda: print("Combustible carregat"), "activar_motors": lambda: print("Motors activats"), "llancament": lambda: print("Llançament iniciat... Bon viatge!")},
        "solucio": "Combustible carregat\nMotors activats\nLlançament iniciat... Bon viatge!\n",
        "min_chars_codi": 45,
        "paraules_clau": ["preparar_combustible()", "activar_motors()", "llancament()"]
    },
    {
        "tipus": "HISTORIA",
        "missatge": "CODI CORRECTE!\n\nLa nau es posa en marxa i surts de la nau d'abastament en direcció a l'últim punt segur. Però de sobte, K1T-7 t'avisa:\n\n\"Estem sent perseguits! Sis TIE Fighters venen cap a nosaltres! Hem d'activar el canó làser!\"\n\nT'arribes corrents a la sala de control, però el sistema de seguretat no et deixa entrar directament.\n\nNomés podràs accedir si esculls la porta amb la funció làser correctament programada.\n\nAl panell hi ha tres codis Python. Només una funció és correcta per disparar el làser."
    },
    {
        "tipus": "PORTES",
        "missatge": "ENIGMA 9\n\"Analitza les tres funcions següents. Només una d'elles està ben definida. Selecciona la porta que la conté.",
        "etiquetes": ["def laser():\n    print(\"ACTIVAT!\")", "def laser\n    print(\"ACTIVAT!\")", "def laser():\nprint(\"ACTIVAT!\")"],
        "correcta": 1
    },
    {
        "tipus": "HISTORIA",
        "missatge": "PORTA CORRECTA!\n\nDesprés de programar el sistema de làser, t'adones que els TIE Fighters ja estan molt a prop. Estàs en un compte enrere per disparar i destruir els 6 caçadors. Si falles un cop, els TIE Fighters dispararan i potser et perdràs l'oportunitat de escapar.\n\"D'acord,\" diu K1T-7.\"Per cada dispar, la probabilitat de col·lisió canvia. Has d'enviar els teus trets amb precisió.\"\nEl sistema et mostra la situació, i la teva missió és disparar fins que els 6 TIE siguin destruïts.\n"
    },
    {
        "tipus": "CODI",
        "missatge": "ENIGMA 10:\nHas de programar un bucle while que invoqui la funció disparar(). Cada cop que disparis, el sistema et retornarà True/False si el làser ha impactat en algun dels TIE Fighters. Si impactes els 6, l'objectiu s'haurà completat i podràs continuar el teu viatge. Invoca la funció disparar() fins que no quedi cap TIE.",
        "parametres": {},
        "funcions": {"disparar": lambda: (print("TIE destruit!") or True) if random.randint(1, 6) == 1 else False},
        "solucio": "TIE destruit!\nTIE destruit!\nTIE destruit!\nTIE destruit!\nTIE destruit!\nTIE destruit!\n",
        "min_chars_codi": 45,
        "paraules_clau": ["disparar()", "while"]
    },
    {
        "tipus": "HISTORIA",
        "missatge": "CODI CORRECTE!\n\nEls últims restes dels TIE Fighters esclaten darrere teu en una explosió lluminosa. Els sistemes del carguer comencen a estabilitzar-se mentre el soroll d'alarma s'esvaeix.\nK1T-7 esclata d'alegria pel comunicador:\n\"Objectius eliminats! Bona punteria, pilot! Ara… ara pots fugir. Els motors d'hiperespai estan carregats. Introdueix les coordenades i prepara't per saltar.\"\nEt col·loques al seient del pilot. Davant teu, el teclat espera el codi d'inici d'hiperespai. El droide et dona una última comanda:\nprint(\"Coordenades fixades: Sector 7-G, quadrant 4\")\nprint(\"Salt a l'hiperespai en 3...\")\nprint(\"2...\")\nprint(\"1...\")\nprint(\"Zzzzzzzzzzzzzshhhhhhhhhhhhhh!\")\nprint(\"Has escapat. La galàxia té una oportunitat gràcies a tu.\")"
    },
    {
        "tipus": "HISTORIA",
        "missatge": "FI."
    },
]