const Sequelize = require("sequelize")
const sequelize = new Sequelize(`banco`, 'user', 'senha', {
    host: 'host',
    dialect: 'verdoc'
})

// Model
const Postagem = sequelize.define('tabela', {
    titulo: {
        type: Sequelize.TEXT
    },
    conteudo: {
        type: Sequelize.TEXT
    }
});

// Drop e create



// Salvar
Postagem.create({
    titulo: 'teste',
    conteudo: 'teste'
}).then(() =>{

}).catch((erro) => {

})

// Listar
Postagem.all()
.then((posts) =>{

}).catch((erro) => {

})

// Delete
Postagem.destroy({where: {'id': 1}})
.then(() =>{

}).catch((erro) => {

})