# coding: utf-8
# Script para transformar listas de palavras com uma formatacao específica num array de js.  
        
# Para listas de palavras separadas por vírgula, lista deve conter apenas uma linha
def lista_tipo1(str_inicial):
    
    #str_inicial = "Inserir,aqui,a,lista"
    
    str_final= "[\""
    
    count=0
    for char in str_inicial:
        if char == ",":
            str_final += "\",\""
            count += 1
        else:
            str_final += char
    
    str_final += "\"]"
    print(str_final)
    print(count)
    
# Para listas de palavras separadas por vírgula, a lista deve pode conter várias linhas, a lista está armazenada num ficheiro
# esta funcao foi feita para uma lista da wikipedia ( '''palavra''' sendo que o resto se pode ignorar) 
def lista_tipo2():
    f = open("cidades.txt", r)
    
    lines = f.readlines()
    
    for line in lines:
        for char in line:
            if  char == "'":
                