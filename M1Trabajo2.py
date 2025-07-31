meme_dict = {
"CRINGE": "Algo excepcionalmente raro o embarazoso",
"LOL": "Una respuesta común a algo gracioso",
"ROFL":" una respuesta a una broma",
"SHEESH" :"ligera desaprobación",
"CREEPY": " aterrador, siniestro",
"AGGRO"  :"ponerse agresivo/enojado",

           }
meme_dict["CHEVRE"]="ALGO GENIAL"
del meme_dict["CREEPY"]
print(meme_dict)
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("no se encontro la palabra")
