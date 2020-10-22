#0 positivo 1 negativo
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
    
    if type(phrase) == list:
        
        for single_phrase in phrase:
            
            single_phrase = single_phrase.lower()
            len_sentimento = []

            for word in single_phrase.split():
                
                actual_word = dados.get(word)
                
                if actual_word is not None:
                    
                    for key, value in actual_word.items():
                        temp = [key,value]
                        len_sentimento.append(temp[1])

                
                else:
                    
                    len_sentimento.append(0)
                
                score = sum(len_sentimento)

    confidence_index = f'{round(total_words-score/sum(unknow_words)*100)}%'


    if score > 0:
        return print(f'Resultado da análise:Positvo\nScore = {score}\nIndice de confiança: {confidence_index}\nQuantidades de palavras: {total_words}\nPalavras desconhecidas: {sum(unknow_words)}')
    elif score == 0:
        return print(f'Resultado da análise: Neutro\nScore = {score}\nIndice de confiança: {confidence_index}\nQuantidades de palavras: {total_words}\nPalavras desconhecidas: {sum(unknow_words)}')
    else:
        return print(f'Resultado da análise: Negativo\nScore = {score}\nIndice de confiança: {confidence_index}\nQuantidades de palavras: {total_words}\nPalavras desconhecidas: {sum(unknow_words)}')



nlu_instance('Eu estou muito feliz hoje, porém, triste com a politica')




# def emotional_calc(lista):

#     bom = mal = 0

#     for i in lista:
#         if i == 0:
#             bom +=1
#         elif i == 1:
#             mal += 1
    

#     if bom > mal:
#         overall = bom/len(lista)
#         print('\nEmotion: Positive')
#         print('Confidence: {}\n'.format(overall))
#     elif bom < mal:
#         overall = mal/(len(lista))
#         print('\nEmotion: Negative\n')
#         print('Confidence: {}\n'.format(overall))
#     elif bom == mal:
#         overall = 1
#         print('\nEmotion: Neutral\n')
#         print('Confidence: {}\n'.format(overall))

# emotional_calc(phare1)
# emotional_calc(phare2)
# emotional_calc(phare3)
# emotional_calc(phare4)
