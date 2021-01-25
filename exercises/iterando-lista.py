#Com função RANGE                               
print('#'*20)                                   
print('..Interando listas..')                   
print('#'*20)
lista_one = [10,20,30,40,50,60,70,80,90]        #Declaração de uma lista com elementos numéricos.
for item in range(len(lista_one)):              #Variável ITEM assumirá os valores gerados pela
    lista_one[item] = lista_one[item] + 100     #instrução RANGE. A função RANGE gerará os valores
print(lista_one)                                #conforme indicado pela função LEN. Esta fará a 
                                                #contagem do número de elementos contidos na lista.

#Com função ENUMERATE                           
print('#'*20)
print('..Interando listas..')
print('#'*20)
lista_two = [1000, 2000, 3000, 4000, 5000]      #Declaração de uma lista com elementos numéricos.
for indx, item in enumerate(lista_two):         #A variável INDX armazenará os valores gerados
    lista_two[indx] = lista_two[indx] + 100     #pela função ENUMERATE. Esta irá colocar um índice
print(lista_two)                                #em cada elemento da lista. Já a variável ITEM 
print(item)                                     #guardará o elemento em questão, um por vez para
                                                #cada ciclo da instrução FOR.
