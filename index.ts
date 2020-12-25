const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const session = require("express-session");
const admin = require("./routes/admin");
const app = express();

// Para retornos em json
app.use(express.json());

// entenda json
app.use(bodyParser.json());
// entender parametros
app.use(bodyParser.urlencoded({extended: false}));

// middleware
app.use((req: any, res: any, next: any) => {
    // cors
    app.use(cors());
    next();
})

// Sessao
app.use(session({
    secret: "chave",
    resave: true,
    saveUninitialized: true
}))

//Exemplo rotas
app.use('/', admin);

app.listen(8081, () => {
    console.log("Servidor rodando")
});