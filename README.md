<p align="center">
  <img src="https://user-images.githubusercontent.com/63745733/120118412-cc1acc80-c168-11eb-9655-e5c6d8aef02d.gif">
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/63745733/120118443-ec4a8b80-c168-11eb-9369-a2ac4bb30ba7.png">
</p>

<p align="center">
  <img src="https://sonarcloud.io/api/project_badges/measure?project=EliasOlie_NLP&metric=alert_status">
  <img src="https://sonarcloud.io/api/project_badges/measure?project=EliasOlie_NLP&metric=sqale_rating">
  <img src="https://sonarcloud.io/api/project_badges/measure?project=EliasOlie_NLP&metric=reliability_rating">
  <img src="https://sonarcloud.io/api/project_badges/measure?project=EliasOlie_NLP&metric=security_rating">
  <img src="https://sonarcloud.io/api/project_badges/measure?project=EliasOlie_NLP&metric=sqale_index">
  <img src="https://sonarcloud.io/api/project_badges/measure?project=EliasOlie_NLP&metric=code_smells">
  <img src="https://sonarcloud.io/api/project_badges/measure?project=EliasOlie_NLP&metric=vulnerabilities">
</p>

<h1>NLP Brasil</h1>

## Motivação

Cada vez mais tem se monstrado a necessidade de um modelo de processamento natural de linguagem, esse repositorio e API tem como motivação
justamente solucionar de forma simples e prática, com um modelo estatistico essa necessidade!

### Status: Em desenvolvimento ⚠

# Como usar

🤓 Antes de colocar a mão na prática sugiro a leitura completa para o entendimento de como funciona e como as palavras são classificadas

Esse repositório está sendo servido pelo Heroku pelo link: https://nlp-brasil.herokuapp.com/phrase ⚠ Não temos (ainda) interface gráfica (frontend) ⚠ então a
única forma de consumir essa api é através de bibliotecas como requests (python) e programas como insominia (gif inicial) e postman

Esse endpoint https://nlp-brasil.herokuapp.com/phrase só aceita o método POST na forma de application/json e a estrutura do objeto json deve ser a seguinte:

```json
{
"phrase":"Chamada de api"
}
```

# Exemplos práticos:

* gif do inicio do rep (Usando o insominia e mandando para o endpoint)

* Requests (biblioteca em python) 

<p align="center">
  <img src="https://user-images.githubusercontent.com/63745733/120118781-ab537680-c16a-11eb-8a61-d49681a8a93f.gif">
</p>

### Código:

```python
import requests
import json

data = {"phrase":"Chamada de api"}

h={"Content-Type":"application/json"}

resposta = requests.post('https://nlp-brasil.herokuapp.com/phrase', data=json.dumps(data), headers=h,verify=True)

print(resposta.text)
```
O formato de saída da api é:


```json
{
"resultado": "a frase 'chamada de api' e neutra", 
"score": "33%"
}
```

A API também pode ser consumida por qualquer biblioteca que funcione de maneira análoga ao requests em python:

*  XMLHttpRequest (Javascript)
* JAXB (Java)
* Entre outros

# Casos reais:

Em breve!

# Desafios enfrentados

Atualmente o maior desafio se dá pelo léxico que muitas vezes classifica uma palavra positiva como negativa ou neutra e vice e versa, o que quando acontece faz com que 
o indice de confiança saia baixo e ou a polaridade da frase venha errada, um método para atualizar o léxico já está em desenvolvimento

# Como funciona

A classe NLP consome um léxico que foi transformado num json gigantesco que contem a palavra e a polaridade dela Ex:

```json
"pesaroso": {
        "polaridade": -1
    },
```
Então para cada palavra na frase o algoritmo soma a polaridade (-1 negativa, 0 neutra ou 1 positiva) e atribui a uma variável de polaridade que é então modificada pelo 
contexto, um bom exemplo de como o contexto pode mudar completamente a polaridade de uma frase é justamente quando encontramos a palavra "gostei" que a primeira 
vista é uma palavra 1 positiva, porém, se eu disse "eu não gostei muito desse pão" a palvra "gostei" se torna na verdade um amplificador para o não que é (nesse contexto)
negativo.
Depois de passar por essa atribuição de contexto o algoritmo calcula o indice de confiança, que é semelhante a notação erro relativo estatistico
básicamente para se ter uma porcentagem do quão certo o modelo está nós temos a seguinte notação:

C (Confiança) = PC (Palavras conhecidas) / PD (Palavras desconhecidas) * 100

Já que nós estamos dividindo o nosso espaço amostral pelas palavras que o algoritmo não entendende (que pode no máximo ser todas e retornar 0) sempre teremos
um numero que corresponderá a porcentagem, por isso multiplicamos por 100 para poder obter a porcentagem

### Código:

```python
if know_words > 0: #O algorimo só processerá se houver alguma palavra conhecida caso o contrário receberemos 0 (0/1)

            total_words = len(phrase_list.split()) #Onde total_words = PC, cf = C e know_words = PC 
            cf =  f'{round(know_words / total_words *100)}%'

        else:
            cf = 'Baseado nos dados já coletados não posso chegar numa conclusão precisa' #Caso não haja palavras conhecidas

        return cf
```
Então uma vez que temos todos os dados o nosso objeto json é criado onde conterá todos os dados da frase como palavras desconhecidas e etc. Porém, apenas
a mensagem de resumo "A frase 'frase' é 'polaridade'

O formato final do json é:

```json
{
"resultado": "a frase 'chamada de api' e neutra", 
"score": "33%"
}
```
