def habitación3():
    print("habitación 3")


def habitación2():
    print("habitación 2")


def habitación1():
    print("En la habitación no hay nada, pero ves dos puertas mohosas:")
    print("Una en el este y otra en el oeste")
    direc = input("¿este, oeste o sur?")

    if direc == "oeste":
        habitación2()
    elif direc == "este":
        habitación3()
    else:
        entrada()


    def entrada():
        print("Has entrado")
        print("La norte ves una puerta vieja")
        print("Al sur ves la entrada a la cripta")
    direc = input("¿Norte o Sur?")
    if direc == "norte":
        habitación1()
    else:
        print("MUERTE A LOS COBARDES")

print ("The Quest for Skullhammer")
print ("=========================")
print ("")
print ("La espada Skullhammer ha sido robada por un mago")
print ("La ha escondido en lo profundo de una cripta")
print ("¿Quieres entrar en la cripta del mago?")

respuesta = input("(si/no)")

if respuesta == "si":
             entrada()

else: print("MUERTE A LOS COBARDES")