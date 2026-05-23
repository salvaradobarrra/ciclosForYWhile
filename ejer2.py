import random

try:
    #es algo nuevo
    #otra cosa
    limite_inferior=int(input("Ingrese limite inferior: "))
    limite_superior=int(input("Ingreselimitesuperior: "))

    if limite_inferior > limite_superior:
        print("El limite inferior no puede ser mayor al limite superior")
        exit()
    elif limite_inferior == limite_superior:
        print("El limite inferior no puede ser igual al limite superior")
        exit()
    numero =random.randint(limite_inferior,limite_superior)
    resto=numero %2
    if resto == 1:
        numero=numero+1
    if numero > limite_superior:
        numero = numero - 2
    elif numero < limite_inferior:
        numero = numero + 2
    
    dif1=0
    dif2=0

    intento1=int(input("Intenta adivinar: "))
    if intento1 == numero:
        print("Felicitaciones, pudiste adivinar.")
        exit()
    elif intento1 < numero:
        dif1 = numero-intento1
        print("El numero es mayor")
    elif intento1 > numero:
        dif1 = intento1 - numero
        print("El numero es menor")

    intento2=int(input("Intente de nuevo: "))
    if intento2 == numero:
        print("Felicitaciones, pudiste adivinar.")
        exit()
    elif intento2 < numero:
        dif2 = numero - intento2
        print("El numero es mayor")
        
    elif intento2 > numero:
        dif2 = intento2 -numero
        print("El numero es menor")
       

    print("Te dare una pista")
    print(numero)
    print("dif1",dif1,"dif2 ",dif2)

    if dif1==dif2:
        print("El numero ", intento1, " y el numero ", intento2, "estan a la misma distancia.")
    elif dif1 < dif2:
        print("El numero ", intento1, " está mas cerca que ", intento2,".")
    else:
        print("El numero ", intento2, " está mas cerca que ", intento1,".")
    
    intento3=int(input("Intente la ultima vez: "))
    if intento3 == numero:
        print("Felicitaciones, pudiste adivinar.")
        exit()
    else:
        print("Perdiste")
        print("El numero era: ",numero)

except ValueError:
    print("Ingreso erroneo")