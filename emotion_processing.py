#0 positivo 1 negativo
import json
import sys

with open('nlp_database.json', 'r') as json_file:
    dados = json.load(json_file)

def nlu_instance(phrase):
   
    if type(phrase) == str:
        
        phrase = phrase.lower()
        len_sentimento = []
        unknow_words = []
        
        for word in phrase.split():
            
            total_words = len(phrase.split())
            actual_word = dados.get(word)
            
            if actual_word is not None:
                
                for key, value in actual_word.items():
                    
                    temp = [key,value]
                    len_sentimento.append(temp[1])
            
            else:
                
                unknow_words.append(1)
                len_sentimento.append(0)
            
            
            score = sum(len_sentimento)
    
    if type(phrase) == list:
        
        for single_phrase in phrase:
            
            single_phrase = single_phrase.lower()
            len_sentimento = []
            unknow_words = []

            for word in single_phrase.split():

                total_words = len(single_phrase.split())
                actual_word = dados.get(word)
                
                if actual_word is not None:
                    
                    for key, value in actual_word.items():
                        
                        temp = [key,value]
                        len_sentimento.append(temp[1])

                
                else:
                    
                    len_sentimento.append(0)
                    unknow_words.append(1)

                
                score = sum(len_sentimento)

    
    

    try:
        confidence_index = f'{round(total_words-sum(unknow_words)/score*100)}%'
    except:
        confidence_index = f'Ops! {sys.exc_info()[0]} Nenhuma palavra no banco de dados'



    if score > 0:
         msg = f'\nResultado da análise:Positvo\nScore = {score}\nIndice de confiança: {confidence_index}\nQuantidades de palavras: {total_words}\nPalavras desconhecidas: {sum(unknow_words)}'
    
    elif score == 0:
         msg = f'\nResultado da análise: Neutro\nScore = {score}\nIndice de confiança: {confidence_index}\nQuantidades de palavras: {total_words}\nPalavras desconhecidas: {sum(unknow_words)}'
    
    else:
         msg = f'\nResultado da análise: Negativo\nScore = {score}\nIndice de confiança: {confidence_index}\nQuantidades de palavras: {total_words}\nPalavras desconhecidas: {sum(unknow_words)}'

    return [score, confidence_index, total_words, unknow_words, msg]

analys = nlu_instance('consistente feliz triste abafado')
print(analys[4])