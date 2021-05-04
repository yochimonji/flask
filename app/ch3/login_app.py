from flask import Flask, redirect, request, session
app = Flask(__name__)
app.secret_key = 'm9XE4JH5dB0QK4o4'

USERLIST = {
    'taro': 'aaa',
    'jiro': 'bbb',
    'sabu': 'ccc'
}

@app.route('/')
def index():
    return """
        <html><body>
            <h1>ログインフォーム</h1>
            <form action="/check_login" method="POST">
                ユーザー名：<br>
                <input type="text" name="user"><br>
                パスワード：<br>
                <input type="password" name="pw"><br>
                <input type="submit" value="ログイン">
            </form>
            <p><a href="/private">→秘密のページ</a></p>
        </body></html>
    """

@app.route('/check_login', methods=["POST"])
def check_login():
    user, pw = (None, None)
    if 'user' in request.form:
        user = request.form['user']
    if 'pw' in request.form:
        pw = request.form['pw']
    if (user is None) or (pw is None):
        return redirect('/')

    if not try_login(user, pw):
        return """
            <h1>ユーザー名かパスワードの間違い</h1>
            <p><a href="/">→戻る</a><p>
        """
    return redirect('/private')

@app.route('/private')
def private_page():
    if not is_login():
        return """
            <h1>ログインしてください</h1>
            <p><a href="/">→ログインする</a></p>
        """
    
    return """
        <h1>ここは秘密のページ</h1>
        <p>あなたはログイン中です。</p>
        <p><a href="/">→ログアウト</a></p>
    """

@app.route('/logout')
def logout_page():
    try_logout()
    return """
        <h1>ログアウトしました</h1>
        <p><a href="/">→戻る</a></p>
    """

def is_login():
    if 'login' in session:
        return True
    return False

def try_login(user, password):
    if not user in USERLIST:
        return False
    if USERLIST[user] != password:
        return False
    session['login'] = user
    return True

def try_logout():
    session.pop('login', None)
    return True

if __name__ == '__main__':
    app.run(debug=True)