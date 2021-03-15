import json
import unicodedata

with open('backend/nlp_database.json', 'r', encoding='utf-8') as json_file:
    dados = json.load(json_file)


def normalization(word): #Normalização da frase, removendo caracteres especiais e afins
    normalized = unicodedata.normalize('NFD',word)
    return normalized.encode('ascii', 'ignore').decode('utf8').casefold()

def nlu_instance(phrase): #Separação e atribuição de polaridade
   
    len_sentimento = [] #Lista que conterá a polaridade de cada palavra, para posteriormente obter o total, como neutro, positivo ou negativo
    unknow_words = 0 #Palavras desconhecidas é importante sua contagem, pois, dessa forma um indice de confiança fica mais preciso
    know_words = 0 #Palavras conhecidas, mesma razão das palavras desconhecidas

    if type(phrase) == list: #Fazer da lista uma frase
        ' '.join(phrase)

        phrase = normalization(phrase.lower()) #Remove-se toda a acentuação da frase
        
        lista_palavra = phrase.split()

        for word in lista_palavra:
            
            actual_word = dados.get(word)
            
            if actual_word is not None:

                for key, value in actual_word.items():
                    
                    temp = [key,value]
                    len_sentimento.append(temp[1])
                    know_words += 1
                    
            else:
                
                unknow_words += 1
                len_sentimento.append(0)

    if type(phrase) == str:
        
        phrase = normalization(phrase.lower())
        
        lista_palavra = phrase.split()

        for word in lista_palavra:
            
            actual_word = dados.get(word)
            
            if actual_word is not None:

                for key, value in actual_word.items():
                    
                    temp = [key,value]
                    len_sentimento.append(temp[1])
                    know_words += 1
                    
            else:
                
                unknow_words += 1
                len_sentimento.append(0)
            
    else:
        print('Apenas string! ') 
    
    polarity = sum(len_sentimento)  

    # 1° Passo (to-do)
    return [polarity, know_words, unknow_words] # Retorno desse módulo do 1° processo implementar de maneira que as outras funções possam fazer proveito dele

def get_confidenceIndex(phrase_list, know_words):

    #O indíce de confiança é a razão entre as palavras conhecidas e todas as palavras
    #Da frase que se dá pelo cumprimento da frase colocando numa lista
    #Dessa forma podemos avaliar a confiabilidade do nosso modelo, pois, dada a cituação
    #O indice de confiança seria (todas as palavras (TP) - palavras desconhecidas (PD)/ todas as palavras) 
    #Como TP - PD resulta no número de palavras conhecidas o nosso modelo justifica da seguinte forma: 
    #IF (Indice de confiança) = PC (Palavras conhecidas)/TP, sendo assim por estarmos dividindo pelo "espaço
    #Amostral total" que se da pela quantidade total de palavras na frase, o nosso IF não pode dar um valor
    #Maior do que 1 e menor do que zero, em termos de notação temos:

    #IF = PC/TP, onde 1 <= IF >= 0, logo IF fica entre 0 e 1, sendo 1 mais preciso e 0 o contrário

    #Isto é para PC > 0, pois se não conhecermos nenhuma palavra da frase, isso resultaria em 0/TP o que 
    #Daria 0, dessa forma é mais viável em termos de custo operacional checar antes de mais nada se há algum 
    #Valor não nulo em PC, caso haja informar que como nosso modelo desconhece todas as palavras, qualquer 
    #Estimativa seria imprecisa! Dessa forma Acredito que o Big O notation será O(n)


    #Confidence index is the reason between the know words in the phrase and the lenght of the phrase
    #In this way it means that how many know words in the phrase we have, more confidence we will have
    #And how less, less confidence. How it is divided by the total words, it means that we always have for
    #Total words != 0 confidence index (CF)  0 < CF <= 1, that means how close to 1 greater is the confidence
    #and close to zero low confidence. By the fact that we can find a phrase where not a single word is 
    #Counted by our database, we specify that the math reason is just valid for Know_words > 0, else we display
    #A message telling that we can't reach to a precise conclusion based on zero known words 

    if know_words > 0:

        total_words = len(phrase_list.split()) #mover para processos iniciais <-*
        cf =  know_words / total_words  #exeption handle (Zero divisin error) | Função especifica


    else:
        cf = normalization('Baseado nos dados já coletados não posso chegar numa conclusão precisa')

    return cf 

def get_context(phrase_list, overallpolarity):

    score = 0

    negative_context = ['não', 'nao', 'Não', 'Nao']

    phrase_list = phrase_list.split()
    try:
        context1 =  phrase_list.index('gostei') - 1
        if context1 >= 0: #Separar para função isolada
            if 'gostei' in phrase_list and phrase_list[context1] in negative_context:
                score -= 1
            else:
                score += 1
                pass
        else:
            pass
    except:
        pass
     #Separar para isolamento em função separada

    overallpolarity += score


    return overallpolarity

def nutshell(score, cf, tw, uw, msg):
   
    retorno = { # função isolada
            
            "Polaridade":score,
            "Confidence":cf, 
            "Numero de palavras":tw, 
            "Palavras desconhecidas":uw, 
            "Mensagem":msg
            
            }
    return retorno


def processing(phrase):
    
    #Análise da polaridade da frase e atribuição de variáveis úteis
    nluscore = nlu_instance(phrase)
    ukwwords = nluscore[2]
    knowords = nluscore[1]

    #Atualizar o score através das variáveis de contexto
    contextscore = get_context(phrase, nluscore[0])

    #Calcular o índice de confiança
    cf = get_confidenceIndex(phrase, knowords)

    #Criação da mensagem de análise de polaridade sentimental da frase
    if contextscore > 0:
        msg = f'A frase "{phrase}" é positiva' # {phrase}
    elif contextscore == 0:
        msg = f'A frase "{phrase}" é neutra'
    else:
        msg = f'A frase "{phrase}" é negativa'

    nut = nutshell(contextscore, cf, len(phrase.split()), ukwwords, normalization(msg))

    return nut

def display(phrase):
    show = processing(phrase)
    print(show)