import json

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
    
    

    if score > 0:
        for i in len_sentimento:
            if i == 0:
                len_sentimento.remove(i)
                len_sentimento.append(.33)
    else:
        for i in len_sentimento:
            if i == 0:
                len_sentimento.remove(i)
                len_sentimento.append(-0.33)



    confidence_index = f'{2*abs(score)/(total_words-sum(unknow_words))*100}%'
    if confidence_index ==  '-0.0':
        confidence_index = 'Baseado nos dados já coletados não posso chegar numa conclusão precisa :/' 
    
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

analys = nlu_instance('melhor preço e no preço bom')


print(analys[0]["Mensagem"])