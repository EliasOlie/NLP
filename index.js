const express = require('express');
const path = require('path')

var app = express();

app.use(express.json());
app.use(express.urlencoded());
app.use(express.static(__dirname + '/pages'));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '/pages/index.html'))
})

app.post('/phrase', (req, res) =>{

    
    var spawn = require('child_process').spawn
    const phrase = req.body;

    var process = spawn('python', ['./backend/my_script.py', phrase['phrase']]);

    process.stdout.on('data', function (data) {
        
        res.send(data.toString())

        
    })

});

app.listen(process.env.PORT || 8880);