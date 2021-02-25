from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    username = 'ユウスケ'
    age = 20
    email = 'yusuke@example.com'
    return render_template('card-age.html',
        username=username,
        age=age,
        email=email)

if __name__ == '__main__':
    app.run(debug=True)