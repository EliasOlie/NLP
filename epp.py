import json
import unicodedata

with open('nlp_database.json', 'r', encoding='utf-8') as json_file:
    dados = json.load(json_file)


def normalization(word):
    normalized = unicodedata.normalize('NFD',word)
    return normalized.encode('ascii', 'ignore').decode('utf8').casefold()

def nlu_instance(phrase): #Separação e atribuição de polaridade
   
    len_sentimento = []
    unknow_words = 0
    know_words = 0

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
    
    score = sum(len_sentimento)  

    # 1° Passo (to-do)
    return [score, know_words, unknow_words] # Retorno desse módulo do 1° processo implementar de maneira que as outras funções possam fazer proveito dele

def get_confidenceIndex(phrase_list, know_words):

    if know_words > 0:

        total_words = len(phrase_list.split())
        cf =  know_words / total_words #exeption handle (Zero divisin error) | Função especifica


    else:
        cf = 'Baseado nos dados já coletados não posso chegar numa conclusão precisa'

    return cf 

def get_context(phrase_list):

    score = 0

    negative_context = ['não', 'nao', 'Não', 'Nao']

    phrase_list = phrase_list.split()

    context1 =  phrase_list.index('gostei') - 1 #Separar para isolamento em função separada

    if context1 >= 0: #Separar para função isolada
        if 'gostei' in phrase_list and phrase_list[context1] in negative_context:
            score -= 1
        else:
            score += 1
    else:
        pass

    return score

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
    contextscore = get_context(phrase)

    #Calcular o índice de confiança
    cf = get_confidenceIndex(phrase, knowords)

    #Criação da mensagem de análise de polaridade sentimental da frase
    if contextscore > 0:
        msg = f'A frase {phrase} é positiva'
    elif contextscore == 0:
        msg = f'A frase "{phrase}" é neutra'
    else:
        msg = f'A frase "{phrase}" é negativa'

    nut = nutshell(contextscore, cf, len(phrase.split()), ukwwords, msg)

    print(nut)

processing('Não gostei do pão')