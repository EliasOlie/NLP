import json
from typing import NewType
import utils

"""
TODO:
• Colocar nome dos metodos em portugues ✔
• Comentar o código (PT-BR) e (EN)
• Integrar com o servidor (JS) ✔
• TypeHints e datatype personalizado ✔
• Refatorar código para não se repetir. Usar comprehensions
• Validar frases e exeption handlers
• Unittest
• Quando o resultado é str (Não teve dados sulficientes) (__indice_de_confianca) ✔
• Aumentar lista de palavras com contexto (__atribuir_contexto)

"""

polaridade = NewType('Polaridade', int)
indice_confianca = NewType('Indice de confianca', [float or str])

with open('./backend/nlp_database.json', 'r', encoding='utf-8') as json_file:
    dados = json.load(json_file)

class NLP(object):
    nlp_instace = NewType('nlp_instace', object)

    """
    (PT-BR) Classe básica. Aceita apenas um argumento que é a frase (do tipo str) a ser processada e retorna
    um JSON com os dados do processamento da frase 

    (EN) Basic class. Accepts only one argument the phrase itself (str type) 
    the phrase is processed and then it returns a JSON with the processed data.
    """

    def __init__(self, frase:str) -> nlp_instace:

        self.frase = utils.normalization(frase)
        self.process = {'resultado': f'{self.__processar()["Mensagem"]}, score: {self.__processar()["Confidence"]}'}
        
    def __separar_frase(self):
        len_sentimento: list = [] #Lista que conterá a polaridade de cada palavra, para posteriormente obter o total, como neutro, positivo ou negativo
        unknow_words: int = 0     #Palavras desconhecidas é importante sua contagem, pois, dessa forma um indice de confiança fica mais preciso
        know_words: int = 0       #Palavras conhecidas, mesma razão das palavras desconhecidas
        
        lista_palavra = self.frase.split()

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

        json_file.close()
        
        polarity: int = sum(len_sentimento)

        return [polarity, know_words, unknow_words]

    def __indice_de_confianca(self, phrase_list: list, know_words: list) -> indice_confianca:
        if know_words > 0:

            total_words = len(phrase_list.split()) #mover para processos iniciais <-*
            cf =  f'{round(know_words / total_words *100)}%'

        else:
            cf = 'Baseado nos dados já coletados não posso chegar numa conclusão precisa'

        return cf

    def __atribuir_contexto(self, phrase_list:list, overallpolarity:int) -> indice_confianca:

        score: int = 0

        negative_context = ['não', 'nao', 'Não', 'Nao']
        palavras_neutras = ['gostei']


        phrase_list = phrase_list.split()
        try:
            context1 =  phrase_list.index(palavras_neutras[0]) - 1
            if context1 >= 0: 
                if palavras_neutras[0] in phrase_list and phrase_list[context1] in negative_context:
                    score -= 1
                else:
                    score += 1
        except:
            pass

        overallpolarity += score


        return overallpolarity

    def __resumo(self,score:int, cf:float, tw:int, uw:int, msg:str) -> object:
   
        retorno: object = {
                
                "Polaridade":score,
                "Confidence":cf, 
                "Numero de palavras":tw, 
                "Palavras desconhecidas":uw, 
                "Mensagem":msg
                
                }

        return retorno


    def __processar(self) -> nlp_instace:
    
        #Análise da polaridade da frase e atribuição de variáveis úteis
        nlp_instance = self.__separar_frase()

        #Atualizar o score através das variáveis de contexto
        contextscore = self.__atribuir_contexto(self.frase, nlp_instance[0])

        #Calcular o índice de confiança
        cf = self.__indice_de_confianca(self.frase, nlp_instance[1])

        #Criação da mensagem de análise de polaridade sentimental da frase
        if contextscore > 0:
            msg = f'A frase "{self.frase}" é positiva'
        elif contextscore == 0:
            msg = f'A frase "{self.frase}" é neutra'
        else:
            msg = f'A frase "{self.frase}" é negativa'

        nut = self.__resumo(contextscore, cf, len(self.frase.split()), nlp_instance[2], utils.normalization(msg))

        return nut


    def __repr__(self) -> str:
        return f'(frase= {self.frase})'

if __name__ == "__main__":
    
    a1 = NLP('Produto péssimo')
    print(a1.process)
 