import random

numerproby = 0
l = random.randint(0,100)

print("Zgadnij liczbe z zakresu 1-100")


while numerproby < 7:
    liczba = input
    liczba = int(liczba)
   

    numerproby = numerproby + 1
    
    if liczba > l:
        print("mniej")
    elif liczba < l:
        print ("wiecej")    
    elif l == liczba:
        print ("zgadles")
        break
