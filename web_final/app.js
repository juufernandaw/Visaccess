//Carregando módulos
require('dotenv').config()
const express = require('express')
const handlebars = require('express-handlebars')
const bodyParser = require('body-parser')
const app = express()
const path = require('path')
const mongoose = require('mongoose')
require(path.join(__dirname+'/frontend/model/usuario.js'))
const Usuario = mongoose.model("users")
const session = require('express-session')
const flash = require('connect-flash')
const passport = require('passport')
require("./config/auth")(passport)
function ehAutenticado(req, res, next){
    if(req.isAuthenticated()){
        return next()
    }
    req.flash("error_msg", "Você deve estar logado para entrar aqui") //exibir a mensagem
    res.redirect("/")
}


//Configurações
    //Sessão
        app.use(session({
            secret: "SDHSJDAKSDHJD",
            resave: true,
            saveUninitialized: true
        }))
        app.use(passport.initialize())
        app.use(passport.session())
        app.use(flash())
    //Middleware 
        app.use((req,res,next) => {
            res.locals.success_msg = req.flash("sucess_msg")
            res.locals.error_msg = req.flash("error_msg")
            res.locals.error = req.flash("error") //essa msg não tá sendo exibida ainda 
            res.locals.user = req.user || null //armazena os dados do usuário logado em uma varíavel global
            next()
        })
    //Body Parser
        app.use(bodyParser.urlencoded({extended: true}))
        app.use(bodyParser.json())
    //Handlebars
        app.engine('handlebars', handlebars.engine({defaultLayout: 'main'}))
        app.set('view engine', 'handlebars')
    // Public
        app.use(express.static(path.join(__dirname + '/public')))

//Rotas
    app.get('/', (req,res) => {
        res.sendFile(path.join(__dirname+'/frontend/view/index.html'))
    })

    app.get('/inicio', ehAutenticado, function(req, res){
        res.sendFile(path.join(__dirname+'/frontend/view/inicio.html'))  
    })
    
    app.get('/login', function(req, res){
        res.sendFile(path.join(__dirname+'/frontend/view/login.html'))
    })

    app.get('/register', function(req, res){
        res.sendFile(path.join(__dirname+'/frontend/view/register.html'))
    })

    /* app.get('/tela_ranking.html', ehAutenticado, function(req, res){
        res.sendFile(path.join(__dirname+'/frontend/view/tela_ranking.html'))
    }) */

    app.post('/usuarios/cadastrar', function(req, res){
        var erros = []

        if(!req.body.user || typeof req.body.user == undefined || req.body.user == null){
            erros.push({texto: "Nome inválido"})
        }

        if(!req.body.mail || typeof req.body.mail == undefined || req.body.mail == null){
            erros.push({texto: "Email inválido"})
        }

        if(!req.body.senha || typeof req.body.senha == undefined || req.body.senha == null){
            erros.push({texto: "Senha inválida"})
        }

        if(req.body.senha.length < 4){
            req.flash("error_msg", "SENHA CURTA")
            erros.push({texto: "Senha muito curta"})
        }

        if(erros.length > 0){
            console.log(erros)
            //res.render("usuarios/cadastar", {erros: erros})
            //precisamos fazer com que a tela entrar aponte esses erros ao usuario
        } else {
            Usuario.findOne({email: req.body.email}).then((usuario) => {
                if(usuario){
                    req.flash("error_msg", "Já existe um usuário cadastrado com esse email")
                    res.redirect("/register")
                    //exibir a menesagem de erro
                } else {
                    const novoUsuario = new Usuario({
                        nome: req.body.user,
                        email: req.body.mail,
                        senha: req.body.senha 
                    }).save().then(() => {
                        console.log("Usúario salvo com sucesso")
                    }).catch((err) => {
                        console.log("Ocorreu um erro ao salvar o usúario"+err)
                    })
                    req.flash("success_msg", "Usuário logado com sucesso")
                    res.redirect("/login")
                    //exibir a mensagem de sucesso
                }
            }).catch((err) => {
                req.flash("error_msg", "Houve um erro ao cadastrar")
                res.redirect("/register")
                //exibir a mensagem de erro  
            })
        }
    })

    /* app.post('/usuarios/salvarjohns', function(req, res){
        const query = {
            //aqi vai o identificador do usuario, pra buscar na query
        }
        const newEntry = {
            num_johns: req.body.num_johns,
            num_autoclicker: req.body.num_autoclicker,
            num_farm: req.body.num_farm
        }
        Usuario.update(query, newEntry).save().then(() => {
            console.log('Usuario atualizado com  sucesso')
        }).catch((err) => {
            console.log('Ocorreu um erro ao atualizar'+err)
        })
    }) */

    app.post('/usuarios/logar', function(req, res, next){
        passport.authenticate("local", {
            successRedirect: "/inicio",
            failureRedirect: "/login"
            //fazer as mensagens de erro 
        })(req, res, next)
    })

//MongoDB
// Credenciais
    const dbUser = process.env.DB_USER
    const dbPassword = process.env.DB_PASS
    mongoose.Promise = global.Promise
    mongoose.connect(`mongodb+srv://${dbUser}:${dbPassword}@cluster0.2vlgiyx.mongodb.net/?retryWrites=true&w=majority`, {
        useNewUrlParser: true
    }).then(() => {
        console.log("MongoDB Conectado!")
    }).catch((err) => {
        console.log("Houve um erro ao se conectar ao mongoDB"+err)
    })

const PORT = 3000
app.listen(PORT, function(){
    console.log("Servidor rodando!")
})
