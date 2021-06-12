const express = require('express');
const path = require('path')
const rateLimiter = require("express-rate-limit")

const limiter = rateLimiter({
    windowMs: 15*60*1000, //15 Minutos à cada
    max: 100             // 100 requisições 
})

//Instancia do express
var app = express();

//Area de configurações de middlewares
app.use(express.json());
app.use(express.urlencoded());
app.use(express.static(__dirname + '/pages'));
app.use(limiter);



//Rotas
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '/pages/index.html'))
})

app.post('/phrase', (req, res) =>{

    
    var spawn = require('child_process').spawn
    const phrase = req.body;

    var process = spawn('python', ['./backend/my_script.py', phrase['phrase']]);

    process.stdout.on('data', function (data) {
        
        globalThis.res_value = data.toString();

        res.send(data.toString())

        
    })
    
});

app.listen(process.env.PORT || 8880);