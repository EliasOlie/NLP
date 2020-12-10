import json

sentilexpt = open('sentment.txt', 'r')

palavras = {}

# for i in sentilexpt.readlines():
#     pos_ponto = i.find('.')
#     palavra = (i[:pos_ponto])
#     pol_pos = i.find('POL')
#     polaridade = (i[pol_pos+4:pol_pos+9]).replace(';','')
#     palavras[palavra] = polaridade

lista = []

export = {}

for i in sentilexpt.readlines():
    pos_ponto = i.find('.')
    palavra = (i[:pos_ponto])
    palavra = palavra.replace(',',' ')
    palavra = palavra.split()
    palavra_f = palavra[1]
    pol_pos = i.find('POL')
    polaridade = (i[pol_pos+4:pol_pos+9]).replace(';','')
    polaridade = polaridade.replace('=',' ')
    polaridade = polaridade.split()
    polaridade_f = polaridade[1]
    lista.append(palavra_f)
    lista.append(polaridade_f)
    
count = 0 #Index de cada iteração
p = 0
pol = 1

while count < (len(lista)/2):#para cada item na lista final
    
    export[lista[p]] = { 

        'polaridade':int(lista[pol])

    }
    
    pol += 2
    p = pol - 1
    count += 1   


jeisu = json.dumps(export)#vamos montar o json do nosso dicionário export

ex = open('nlp_database.json', 'w')
ex.write(jeisu)#e vamos escreve-lo
print('Feito')
ex.close()
#Fim!

