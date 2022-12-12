const localStrategy = require("passport-local").Strategy
const mongoose = require("mongoose")

//Model de usuário
require("../frontend/model/usuario")
const Usuario = mongoose.model("users")


module.exports = function(passport){
    passport.use(new localStrategy({usernameField: 'mail', passwordField:"senha"}, (email, senha, done) => {
        Usuario.findOne({email: email}).then((usuario) => {
            if(!usuario){
                return done(null, false, {message: "Esta conta não existe"})
            }
            if(senha == usuario.senha){
                return done(null, usuario)
            } else {
                return done(null, false, {message: "Senha incorreta"})
            }
        })
    }))
    //precisa fazer a sessão
    passport.serializeUser((usuario, done) => {
        done(null, usuario.id)
    })
    passport.deserializeUser((id, done) => {
        Usuario.findById(id, (err, usuario) => {
            done(err, usuario)
        })
    })
    
}