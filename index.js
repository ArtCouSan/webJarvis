const express = require("express");
const app = express();

app.get("/", (req, res) => {
    res.send("Seja bem vindo")
});

app.get("/:teste", (req, res) => {
    res.send("Parametro: ".concat(req.params.teste))
});


app.listen(8081, () => {
    console.log("Servidor rodando")
});