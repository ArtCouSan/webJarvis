const mongoose = require('mongoose');
const Schema = mongoose.Schema;

mongoose.connection("mongodb://localhost/umbancox", {
    useMongoClient: true
})
.then(() => {

}).catch((error) => {
});
mongoose.Promise = global.Promise;

// Model
const UsuariosSchema = new Schema({
    nome: {
        type: String,
        require: false
    },
    date: {
        type: Date,
        default: Date.now()
    }
})

// Drop e create
const Usuario = mongoose.model('usuarios', UsuariosSchema);

// Save
const novoUsuario = {
    nome: 'x',
    date: null
}
new Usuario(novoUsuario)
    .save()
    .then(() => {

    })
    .catch((error) => {
        
    });

// Encontrar
Usuario.find()
.then((usuarios) => {

}).catch((error) => {
});

Usuario.findOne({_id: 1})
.then((usuario) => {

}).catch((error) => {
});
