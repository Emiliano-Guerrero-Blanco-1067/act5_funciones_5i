print("Manejo de funciones V1 ")
def hola_mundo():
    print("Hola aqui estoy")
def Mensa(msg):
    print(msg)
def EscribeNC(Nombre, Apellido):
    print(Nombre, Apellido)
    print(f"Tu nombre completo es {Nombre} {Apellido}" )
def suma2numeros(n1,n2):
    s=n1+n2
    return f"la suma de n1+ n2 es de", s


#Llamando a la funcion
hola_mundo()
Mensa("hola Whatsapp") #llama a mensa con un parametro
Mensa("El profe me sorprendio enviando mensajes") #llama a mensa con un parametro
EscribeNC("Emiliano ", "Blanco")
print("Funciones que regresan valor")
print(suma2numeros(7,3))
print(suma2numeros(15,45))


