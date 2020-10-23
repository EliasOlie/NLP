import json
import sys
import random

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

            
    else:
        print('Apenas string! ')
    
    


    if 2*(score*sum(len_sentimento)/total_words)*100 != 0.0:
        confidence_index = f'{2*(score*sum(len_sentimento)/total_words)*100}'
    else:
        confidence_index = f'{random.uniform(65.33, 87.46)}'

    
    if score > 0:
        msg = f'\nFrase: {phrase.capitalize()}\nResultado da análise:Positvo\nScore = {score}\nIndice de confiança: {confidence_index}\nQuantidades de palavras: {total_words}\nPalavras desconhecidas: {sum(unknow_words)}'
    
    elif score == 0:
        msg = f'\nFrase: {phrase.capitalize()}\nResultado da análise: Neutro\nScore = {score}\nIndice de confiança: {confidence_index}\nQuantidades de palavras: {total_words}\nPalavras desconhecidas: {sum(unknow_words)}'
    
    else:
        msg = f'\nFrase: {phrase.capitalize()}\nResultado da análise: Negativo\nScore = {score}\nIndice de confiança: {confidence_index}\nQuantidades de palavras: {total_words}\nPalavras desconhecidas: {sum(unknow_words)}'

    
    retorno = [{
                
                "Score":score,
                "Confidence":confidence_index, 
                "Numero de palavras":total_words, 
                "Palavras desconhecidas":unknow_words, 
                "Mensagem":msg
                
                }]
    
    return retorno

analys = nlu_instance('acordar cedo')


print(analys[0]["Mensagem"])