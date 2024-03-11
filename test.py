from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="submit")

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        print(login_form.data)
        if login_form.data['email'] == "example@gmail.com" and login_form.data['password'] == "123456789":
            return render_template('success.html', form=login_form)
        else:
            return render_template("denied.html", form=login_form)
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
