# Sorprende a tus compañerosi
hobbies=["mi nombre:andreu ciuro fernandez","familia:tengo un hermano de 7 años","edad:11","fortalezas de programacion: celdas, random.randint, input ","debilidades en python:listas y dictionarios","amigos:jero, elias","juego fut en mi escuela, juago tenis","tengo un perro maltipoo llamdo milo"]
import random
while True:
    mode="menu"
    if mode=="menu":
        a=input("que quieres print,add,remove")
        mode=a
    
    if mode=="print":
    
        print(random.choice(hobbies))
        mode="menu"
    if mode=="add":
        b=input("que hobbie quieres agregar")
        hobbies.append(b)
        mode="menu"
    if mode=="remove":
        c=input("que quieres remover")
        if c in hobbies:
            hobbies.remove(c)
            mode="menu"
        else:
            print("no se encontro:(")
            mode="menu"
    
