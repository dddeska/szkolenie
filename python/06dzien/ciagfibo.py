def fib(m):
    #wymagania m:
    #1 to musi byc liczba
    #2 liczba >= 2
    
    try:
        if not isinstance(m, int):
                raise Exception("to jest int")
            except Exception:
            print("to jest int")    
           
        if m < 2:
                raise Exception("musi byc wieksza od 1")
            except Exception:
            print ("musi byc wieksza od 1")  


    lista = [1, 0]
    for liczba in range(2, m+1):
        lista.append(lista[liczba - 1] + lista[liczba - 2])
    return lista[m]    


   
print (fib(1))
#print (fib([1,2,3])
#print (fib("tekst"))
