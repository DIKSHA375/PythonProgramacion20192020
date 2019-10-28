#si tenemos una lista de listas, con longitud variable las sublistas
#por ejemplo, una biblioteca que contiene libros, y que a su vez cada libro
#tiene el isbn, nombre del libro y un número indeterminado de autores

biblioteca=[]#los pongo "a mano" los libros lo suyo seria tener un menu y que
#los fuera pidiendo
libro1=["3i33isbn","intro a la programación","pepe","juan"]
libro2=["3i4ufisbn","programación en python","vicky","jose","david","laura"]

biblioteca.append(libro1)
biblioteca.append(libro2)

##recorremos e imprimimos la información

for i in range(len(biblioteca)):
    print("================================")
    print ("esta es la información guardada del libro ",i)
    for j in range(len(biblioteca[i])):
        print(biblioteca[i][j])
