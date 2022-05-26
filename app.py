from flask import Flask,render_template, url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user,  current_user 
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt



app = Flask(__name__)
#crée l'instance de base de donées
db  = SQLAlchemy(app)
#je vais utiliser bcrypt pour je puisse hacher les mots de passe
bcrypt = Bcrypt(app)
# connecter mon fichier d'application à ma base de données
app.config['SQLAlchemy_DATABASE_URI'] ='sqlite:///database.db'
# L'ajout d'une clé secrète
app.config['SECRET_KEY']='this is secretkey'



#Cette partie de gestinnaire de connexion va me permettre
#de gérer les choses lors de la connexion
#Chargement des utilisateurs à partir des identifiants
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Ce rappel chargé par l'utilisateurs est utiliser por recharger l'objet utilisateur 
# à partir de l'indentifiant utilisateur stocké dans la session

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    #la colonne id est la colonne d'identité de l'utilisateur
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), 
                           Length(min=4, max=20)], 
                           render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[
                             InputRequired(), 
                             Length(min=8, max=20)], 
                             render_kw={"placeholder": "Password"})
    submit = SubmitField('Register')
# le nom d'utilisateure doit etre unique,autrement dit chaque nom 
# d'utilisateur doit etre différent 
def validate_username(self, username):
    existing_user_username = User.query.filter_by(username=username.data).first()
    if existing_user_username:
        raise ValidationError('That username already exists. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(),
                                     Length(min=4, max=20)], 
                                     render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), 
                                     Length(min=8, max=20)], 
                                     render_kw={"placeholder": "Password"})
    submit = SubmitField('Login')

#je vais emprrunter un itinéraire
@app.route('/')
def home():
    return render_template ('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template ('login.html', form=form)# je vais passer ce formulaire dans mon modèle html

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    #le code pour l'enregistrement
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()#valider les modification
        return redirect(url_for('login'))
        #chaque fois que le formulqire est valide on vas créer 
        #immédiatement une version hachée de ce mdps (pour que le mdps soit crypté)
        #Afin d'avoire un processus d'inscription sécurisé

    return render_template ('register.html', form=form)    




if __name__=="__main__": 
 app.run(debug=True)