

def menu():

    print("-------------------------------- \n|1. Serie de Fibonacci            |\n|2. Contador de números naturales | \n|3. Contador de números primos    | \n--------------------------------")
    ans = int(input("Escriba la opcion a seleccionar: "))
   

    if (ans == 1):
        print("\n-------------------------------- \n|1. Serie de Fibonacci            |\n--------------------------------")
        lim1 = int(input("Hasta que fibonacci desea llegar: "))
        fib = (lambda x , x1 = 1, x2 = 0: x2 if x == 0  else fib(x - 1, x1 + x2, x1))
        c = 0
        while c < lim1:
            c += 1
            print(fib(c))
            
        preg()
    elif(ans == 2):
        print("\n-------------------------------- \n|2. Contador de números naturales |\n--------------------------------")
        lim = int(input("Escriba hasta que número desea contar: "))
        x = 0;  
        nat = (lambda k : k + 1)
        while (x < lim):
            x = nat(x)
            print(x)
            
        preg()   
    elif(ans == 3):
        print("\n-------------------------------- \n|3. Contador de números primos    |\n--------------------------------")
        lim2 = int(input("Escriba el limite superior de la lista de números primos a imprimir: "))
        Primlist = range(2, lim2)
        for i in range(2, 10):
            Primlist= list(filter(lambda x: x == i or x % i, Primlist))
        print(Primlist)
        
        preg()
    elif(ans == 4):
        lim3 = int(input("Escriba hasta que número desea contar: ")) 
        x =(lambda x: list(map(print, range(1, x+1))))
        x(lim3)
        
        preg()
        
    else:
        print("El índice que ha indicado no existe")

def preg():
    ans = input("\nDesea volver al menú? s = sí | n = no \n")
    ans = ans.lower()
    if(ans == "s"):
        menu()
    elif(ans == "n"):
        print("Gracias por usar el programa")
        exit()
    else:
        print("La opción que escribió no existe")
    
menu()