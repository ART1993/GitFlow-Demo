# En este programa creamos uan serie de números primos que 
# después formaran un triangulo de altura determinada por 
# el usuario
#import time
numero_s=int(input("Introduce altura triangulo"))
#inicio=time.time()
#Tras crear la altura creamos un range de donde se sacarán los 
#números primos que necesitamos
p_lista=list(range(2,10*numero_s))
primos=[1,2]# suponemos ya que 1 y 2 son números primos ya que
#solo ontenemos un numero entero dividiendolos entre si o por 1

#En este paso eliminamos todos los números pares
del(p_lista[::2])
#inicio el bucle
i=0
# El motivo por el cual uso while y no for es porque voy eliminando
# valores a la lista, por tanto podría producirse un salto no
# deseado y que se me colaran numeros primos o saltarmelos
while True:
    #guardo el valor de la lista en la posición actual
    #en caso de que el valor p_lista[i] cambie
    save=p_lista[i]
    #Añadimos el nuevo valor en la lista de números primos
    primos.append(p_lista[i])
    #En caso de que tengamos todos los números primos 
    # que queremos detenemos la ejecución
    if len(primos)==numero_s:
        break
    #Variables introducidas para iniciar el nuevo bucle
    #el motivo por el que 
    k=1
    pm=p_lista[i]
    while k<len(p_lista):
        #voy multiplicando el valor por k para ir eliminando 
        #valores que puedan ser dividibles por pm
        save2=pm*k
        if (save2 not in p_lista):
            k=k+2
            continue
            # En caso de que no exista en el bucle simplemente 
            # da un salto
        if (save2>max(p_lista)):
            #si pm*k es mayor que el máximo valor de la lista
            #entonces finalizará el bucle
            break
        # En este apartado elimino de p_lista el numero primo 
        # y sus múltiplos
        p_lista.pop(p_lista.index(save2))
        k=k+2
        # En caso de que haya obtenido la cantidad de números
        # primos deseados
    if len(primos)==numero_s:
        break
    #si el valor guardado es menor que el nuevo valor de p_lista[i]
    #el valor de i no variará, en caso contrarío aumentará
    #del modo que he creado el bucle es posible que este paso 
    # es inecesario pero creo que esta bien mantenerlo visible
    #if (save<p_lista[i]):
    #    continue
    #else:
    #    i=i+1
#fin=time.time()
#print(fin-inicio)

#primos.sort()
#inicio el bucle ccon el string como un string vacio
p=""
for m in primos:
    #Para asegurarnos de que el bucle cierra correctamente
    if(primos.index(m)==numero_s):
        break
    #imprime una linea
    p=str(m) + " " +p
    print(p)
#al finalizar el programa obtendrémos un 
# triangulo rectángulo de altura numero_s
