import json

with open('nlp_database.json', 'r') as json_file:
    dados = json.load(json_file)

def nlu_instance(phrase):
   

    if type(phrase) == str:
        
        phrase = phrase.lower()
        len_sentimento = []
        unknow_words = []

        
        lista_palavra = phrase.split()
        
        context1 =  lista_palavra.index('gostei') - 1

        for word in lista_palavra:
            
            total_words = len(phrase.split())
            actual_word = dados.get(word)
            
            if actual_word is not None:
                #Não context check
                if actual_word == 'gostei' and lista_palavra[context1]  == 'nao': 
                    len_sentimento.append(-1)
                if actual_word == 'gostei' and lista_palavra[context1] == None:
                    len.append(1)
                else:
                    len_sentimento.append(0)

                
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


    confidence_index = f'{abs(score)/(total_words)*100}' #exeption handle (Zero divisin error)
    
    if float(confidence_index) < 0:
        confidence_index = 'Baseado nos dados já coletados não posso chegar numa conclusão precisa :/' 
    
    if score > 0:
        msg = f'\nFrase: {phrase.capitalize()}\nResultado da análise:Positvo\nScore = {score}\nIndice de confiança: {confidence_index}%\nQuantidades de palavras: {total_words}\nPalavras desconhecidas: {sum(unknow_words)}'
    
    elif score == 0:
        msg = f'\nFrase: {phrase.capitalize()}\nResultado da análise: Neutro\nScore = {score}\nIndice de confiança: {confidence_index}\nQuantidades de palavras: {total_words}\nPalavras desconhecidas: {sum(unknow_words)}'
    
    else:
        msg = f'\nFrase: {phrase.capitalize()}\nResultado da análise: Negativo\nScore = {score}\nIndice de confiança: {confidence_index}\nQuantidades de palavras: {total_words}\nPalavras desconhecidas: {sum(unknow_words)}'

    
    retorno = {
                
                "Score":score,
                "Confidence":confidence_index, 
                "Numero de palavras":total_words, 
                "Palavras desconhecidas":unknow_words, 
                "Mensagem":msg
                
                }
    
    print(lista_palavra[context1]  == 'nao')

    return retorno


analys = nlu_instance('nao gostei do pao')


print(analys["Mensagem"])