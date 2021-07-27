# coding: utf-8
# Script para transformar listas de palavras com uma formatacao específica num array de js.  
        
# Para listas de palavras separadas por vírgula, lista deve conter apenas uma linha
def lista_tipo1():
    
    str_inicial = "Abrantes,Agualva-Cacém,Águeda,Albergaria-a-Velha,Albufeira,Alcácer do Sal,Alcobaça,Alfena,Almada,Almeirim,Alverca do Ribatejo,Amadora,Amarante,Amora,Anadia,Angra do Heroísmo,Aveiro,Barcelos,Barreiro,Beja,Borba,Braga,Bragança,Caldas da Rainha,Câmara de Lobos,Caniço,Cantanhede,Cartaxo,Castelo Branco,Chaves,Coimbra,Costa da Caparica,Covilhã,Elvas,Entroncamento,Ermesinde,Esmoriz,Espinho,Esposende,Estarreja,Estremoz,Évora,Fafe,Faro,Fátima,Felgueiras,Figueira da Foz,Fiães,Freamunde,Funchal,Fundão,Gafanha da Nazaré,Gandra,Gondomar,Gouveia,Guarda,Guimarães,Horta,Ílhavo,Lagoa ,Lagos,Lamego,Leiria,Lisboa,Lixa,Loulé,Loures,Lourosa,Macedo de Cavaleiros,Machico,Maia,Mangualde,Marco de Canaveses,Marinha Grande,Matosinhos,Mealhada,Mêda,Miranda do Douro,Mirandela,Montemor-o-Novo,Montijo,Moura,Odivelas,Olhão,Oliveira de Azeméis,Oliveira do Bairro,Oliveira do Hospital,Ourém,Ovar,Paços de Ferreira,Paredes,Penafiel,Peniche,Peso da Régua,Pinhel,Pombal,Ponta Delgada,Ponte de Sor,Portalegre,Portimão,Porto,Póvoa de Santa Iria,Póvoa de Varzim,Praia da Vitória,Quarteira,Queluz,Rebordosa,Reguengos de Monsaraz,Ribeira Grande,Rio Maior,Rio Tinto,Sabugal ,Sacavém,Samora Correia,Santa Comba Dão,Santa Cruz,Santa Maria da Feira,Santana,Santarém,Santiago do Cacém,Santo Tirso,São João da Madeira,São Mamede de Infesta,São Pedro do Sul,Lordelo,Seia,Seixal,Senhora da Hora,Serpa,Setúbal,Silves,Sines,Tarouca,Tavira,Tomar,Tondela,Torres Novas,Torres Vedras,Trancoso,Trofa,Valbom,Vale de Cambra,Valença,Valongo,Valpaços,Vendas Novas,Viana do Castelo,Vila Baleira,Vila do Conde,Vila Franca de Xira,Vila Nova de Famalicão,Vila Nova de Foz Côa,Vila Nova de Gaia,Vila Nova de Santo André,Vila Real,Vila Real de Santo António,Viseu,Vizela"
    
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
    print("num de palavras: " + str(count+1))
    
lista_tipo1()

# ESTA FUNCAO NAO FUNCIONA  
# Para listas de palavras separadas por vírgula, a lista deve pode conter várias linhas, a lista está armazenada num ficheiro
# esta funcao foi feita para uma lista da wikipedia ( '''palavra''' sendo que o resto se pode ignorar) 
# ESTA FUNCAO NAO FUNCIONA
def lista_tipo2(): # ESTA FUNCAO NAO FUNCIONA
    f = open("cidades.txt", "r")
    i=0
    char="0"
    while (char!='EOF'):
        f.read(1)
        print(i)
        i+=1
        
    str_final = ""
    special_chars=["ç","ã","é","õ","á","à","â","í","ó","ô","ú","-","Á","Ã","Á","Â","É","Í","Ç","Ó","Ô","Ú"]
    
    lines = f.readlines()
    
    
    for line in line:
        city=""
        for char in line:
            if char == "\n":
                str_final += city + ", "
            if char == " " or "\t":
                continue                
            if (ord(char)>64 and ord (char)<123) or char in special_chars:
                city += char
            
    str_final = lista_tipo1(str_final)
    
    print(str_final)
        
    return

#lista_tipo2()