
# Joc d'enigmes en Python

Aquest projecte permet implementar un joc interactiu d'enigmes utilitzant `pygame`. Està pensat per a usos educatius, especialment en l'aprenentatge de Python i la resolució lògica de problemes mitjançant codificació.

## Enigmes disponibles

Actualment el joc inclou tres tipus d'enigmes implementats:

- **Portes**: escull la porta correcta segons una condició codificada.
- **Password**: resol l’enigma alfanumèric mitjançant pistes de codi.
- **Codi Python**: introdueix codi Python correcte que doni la sortida esperada.

També es poden mostrar pantalles de narrativa/història entre enigmes.

## Fitxer de configuració `conf.py`

Els enigmes del joc es defineixen en el fitxer `conf.py` mitjançant una llista de diccionaris. Cada diccionari representa un enigma i inclou els següents camps:

### Tipus d'enigmes

#### 1. `HISTORIA`
```python
{
    "tipus": "HISTORIA",
    "missatge": "Text narratiu que avança la història..."
}
```

#### 2. `CONTRASENYA`
```python
{
    "tipus": "CONTRASENYA",
    "missatge": "Enunciat amb pistes en codi Python",
    "solucio": "resposta_correcta"
}
```

#### 3. `CODI`
```python
{
    "tipus": "CODI",
    "missatge": "Text de l'enigma",
    "parametres": {
        "nom_variable": "valor",
        ...
    },
    "funcions": {
        "nom_funcio": "definició de la funció (si cal)",
        ...
    },
    "solucio": "sortida_esperada",
    "min_chars_codi": 90,  # opcional
    "paraules_clau": ["if", "print", "=="]  # opcional
}
```

#### 4. `PORTES`
```python
{
    "tipus": "PORTES",
    "missatge": "Text de l'enigma",
    "etiquetes": ["Porta 1", "Porta 2", "Porta 3"],
    "correcta": 2  # Número de la porta correcta
}
```

## Compilació a `.exe`

Pots generar un executable per Windows amb `pyinstaller`:

```bash
pyinstaller --onefile --add-data "assets;assets" main.py
```

## Objectius futurs

- Afegir nous tipus d’enigmes (ex: selecció múltiple, dibuix amb turtle, àudio).
- Implementar sistema de puntuació i temps.
- Guardar progrés del jugador.
- Millorar la navegació i afegir menú d’inici.
