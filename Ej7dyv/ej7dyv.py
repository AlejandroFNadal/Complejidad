##Diseñar un algoritmo de coste en O(n) que dado un conjunto S con n números, y un entero
##positivo k <= n, determine los k números de S más cercanos a la mediana de S

import random
import time
def ncamediana(arr, auxarr,mediana,k,inf,sup):
    if k == 0 or len(arr)==0 or len(arr)==1 or k > len(arr):  #Termina
        print("Terminamos")
        return auxarr
    else:
        if mediana == 0: #Primera ejecucion. se define la mediana
            auxarr=[]
            if (len(arr))%2 == 0: ##Arreglo de longitud par
                mediana=(arr[len(arr)//2]+arr[(len(arr)//2)+1])//2
                inf=len(arr)//2
                sup=len(arr)//2 + 1
                return ncamediana(arr,auxarr,mediana,k,inf,sup)
            else:
                mediana = arr[len(arr)//2]
                inf=len(arr)//2 - 1
                sup=len(arr)//2 + 1
                return ncamediana(arr,auxarr,mediana,k,inf,sup)
        else:
            if mediana-arr[inf] < arr[sup]-mediana or sup> len(arr): #el de la izquierda esta mas cerca
                auxarr.append(arr[inf])
                return ncamediana(arr,auxarr,mediana,k-1,inf-1,sup)
            else:
                auxarr.append(arr[sup])
                return ncamediana(arr,auxarr,mediana,k-1,inf,sup+1)


a=[]
n=int(input("ingresar cantidad de elementos"))
i=0
while len(a)<n:
    aux=random.randrange(10000)
    if aux not in a:
        a.append(aux)
a.sort()
print(a)
aux2=[]
inf=0
sup=0
mediana=0
k=int(input("Ingresar numero de elementos cercanos a la mediana"))
start=time.time()
print(ncamediana(a,aux2,mediana,k,inf,sup))
print(time.time()-start)
#no considero esta parte superior del codigo porque solo genera el conjunto






      
