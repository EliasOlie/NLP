from flask import Flask, render_template, request
from processamento import Natural_Language
import json
import os

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True

@app.route('/', methods=['GET', 'POST'])
def sayhi():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        data = request.form['phrase']
        back_res = Natural_Language.NLP(data).process
        back_res = json.loads(back_res)

        pretty_msg = f'{back_res["Mensagem"].capitalize()}, com aproximadamente {back_res["Confidence"]} de certeza.'

        return render_template('phrase.html', phrase=pretty_msg)

@app.route('/phrase', methods=['POST'])
def phrase_api():
    #Pegar bytestream de bytes (obvio) e transformar eles em str
    data = request.get_data(as_text=True)
    #Transformar em objeto para simplificar
    data = json.loads(data)
    frase = data["phrase"] #Atribuir a variável frase a frase vinda da requisição
    
    #Instanciar a frase 
    back_res = Natural_Language.NLP(frase).process   
    
    return back_res

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)