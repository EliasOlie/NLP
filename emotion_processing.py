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

            
    else:
        print('Apenas string! ')
    
    

    try:
        confidence_index = f'{2*(score*sum(len_sentimento)/total_words)*100}%'
    except:
        confidence_index = f'Ops! {sys.exc_info()[0]} Nenhuma palavra no banco de dados, ou provavelmente o resultado \ndo índice foi anlunado com 2 palavas positivas e 2 negativas'



    if score > 0:
        msg = f'\nResultado da análise:Positvo\nScore = {score}\nIndice de confiança: {confidence_index}\nQuantidades de palavras: {total_words}\nPalavras desconhecidas: {sum(unknow_words)}'
    
    elif score == 0:
        msg = f'\nResultado da análise: Neutro\nScore = {score}\nIndice de confiança: {confidence_index}\nQuantidades de palavras: {total_words}\nPalavras desconhecidas: {sum(unknow_words)}'
    
    else:
        msg = f'\nResultado da análise: Negativo\nScore = {score}\nIndice de confiança: {confidence_index}\nQuantidades de palavras: {total_words}\nPalavras desconhecidas: {sum(unknow_words)}'

    
    return [{"Score":score,
    "Confidence":confidence_index, 
    "Numero de palavras":total_words, 
    "Palavras desconhecidas":unknow_words, 
    "Mensagem":msg,}]

analys = nlu_instance('Esta muito abafado hoje')


print(analys[0]["Mensagem"])