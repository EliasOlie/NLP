const { json } = require('body-parser');
const express = require('express');

var app = express();

app.use(express.json());

app.post('/phrase', (req, res) =>{
    
    var spawn = require('child_process').spawn
    const phrase = req.body;

    var process = spawn('python', ['./backend/my_script.py', phrase['phrase']]);

    process.stdout.on('data', function (data) {
        
        //data é um object -> typeof(data) = object
        
        res.send(data);
        
    })

});

app.listen(process.env.PORT || 8880);