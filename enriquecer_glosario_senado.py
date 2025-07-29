import json
import random

# 1. Cargar palabras desde el archivo .txt
with open("palabras.txt", "r", encoding="utf-8") as f:
    palabras = [line.strip() for line in f if line.strip()]

# 2. Diccionario real (puedes ampliarlo por lote)
diccionario_real = {
    "abrazo": {
        "descripcion": "Acción afectiva de rodear a otra persona con los brazos como muestra de cariño, consuelo o saludo.",
        "seña": "🫂✋🤗 Ambas manos se cruzan sobre el pecho simulando un abrazo. El gesto transmite afecto y cercanía.",
        "emoji": "🫂"
    },
    "azul": {
        "descripcion": "Color asociado al cielo despejado y al mar profundo. Transmite tranquilidad y confianza.",
        "seña": "🔵✋🤚 Mano dominante en forma de 'A' se desliza sobre la palma abierta, simulando el azul sobre una superficie.",
        "emoji": "🔵"
    },
    "familia": {
        "descripcion": "Grupo de personas unidas por vínculos de afecto, crianza o sangre.",
        "seña": "👨‍👩‍👧‍👦✋ Ambas manos se colocan sobre el pecho en forma de semiabrazo, transmitiendo unión y cercanía.",
        "emoji": "👨‍👩‍👧‍👦"
    }
}

# 3. Generador dinámico para contenido simulado
def enriquecer_palabra(palabra):
    palabra_lower = palabra.lower()

    if palabra_lower in diccionario_real:
        data = diccionario_real[palabra_lower]
        return {
            "palabra": palabra,
            "descripcion": data["descripcion"],
            "seña": data["seña"],
            "emoji": data["emoji"]
        }
    else:
        # Descripciones variadas
        descripciones = [
            f"{palabra.capitalize()} representa una noción utilizada en entornos educativos, administrativos o culturales.",
            f"{palabra.capitalize()} hace alusión a una acción, entidad o concepto que aparece en prácticas institucionales.",
            f"{palabra.capitalize()} se emplea comúnmente en contextos sociales, escolares o organizacionales.",
            f"{palabra.capitalize()} identifica un término relevante en áreas de inclusión, participación o acompañamiento.",
            f"{palabra.capitalize()} corresponde a un elemento funcional dentro de procesos comunitarios o académicos."
        ]

        # Señas textuales variadas con emojis
        señas_textuales = [
            f"🧏‍♂️✋ Mano dominante se eleva frente al rostro simulando el gesto característico de '{palabra}', acompañado de expresión neutra.",
            f"🧏‍♂️✋ Movimiento hacia el pecho con dedos extendidos representa simbólicamente el significado de '{palabra}' en contexto accesible.",
            f"🧏‍♂️✋ Se dibuja con la mano dominante una forma alusiva a '{palabra}', destacando su presencia en lenguaje señado institucional.",
            f"🧏‍♂️✋ Ambas manos realizan movimiento semicircular que evoca el uso social de '{palabra}', con intención comunicativa clara.",
            f"🧏‍♂️✋ Gesto lateral que marca el espacio correspondiente a '{palabra}', acompañado de postura firme y ritmo expresivo."
        ]

        return {
            "palabra": palabra,
            "descripcion": random.choice(descripciones),
            "seña": random.choice(señas_textuales),
            "emoji": "🧏‍♂️"
        }

# 4. Procesar todo el corpus por lote
glosario_enriquecido = [enriquecer_palabra(p) for p in palabras]

# 5. Exportar como JSON consultable
with open("glosario_senado.json", "w", encoding="utf-8") as f_out:
    json.dump(glosario_enriquecido, f_out, ensure_ascii=False, indent=2)

print(f"✅ Generadas {len(glosario_enriquecido)} palabras enriquecidas en 'glosario_senado.json'")