from flask import Flask, render_template
from processamento import Natural_Language

app = Flask(__name__)

@app.route('/')
def sayhi():
    return render_template('index.html')


app.run(host='0.0.0.0', debug=True)