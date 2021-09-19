from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, InputRequired
from itertools import combinations


class Form(FlaskForm):
    number = IntegerField('number', validators=[InputRequired()])
    submit = SubmitField('Log in')


app = Flask(__name__)
app.secret_key = "secret"


def answer(result):
    lis = [1, 3, 9, 27, 81, -1, -3, -9, -27, -81]
    comb = []
#    print(result)
    for i in range(1, len(lis)+1):
        comb.append(list(combinations(lis, i)))
    for i in comb:
        for j in i:
            if sum(j) == result:
                return list(j)


@ app.route("/form", methods=["GET", "POST"])
def form():
    form = Form()
    if form.validate_on_submit():
        if form.number.data > -121 and form.number.data <= 121:
            ans = answer(int(form.number.data))
            ans.sort(reverse=True, key=abs)
            res = ""
            for i in ans:
                if i > 0:
                    res = res+'+'+str(i)
                else:
                    res += str(i)

            return (f"result = {res[1:]}")
        else:
            return redirect(url_for('denied'))
    return render_template('login.html', form=form)


@ app.route("/denied")
def denied():
    return "<h1>Failed</h1>"


if __name__ == '__main__':
    app.run(debug=True)
