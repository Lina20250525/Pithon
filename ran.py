from flask import Flask,render_template

app = Flask(__name__)

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/zayavka")
def zayavka():
    return render_template('zayavka.html')

@app.route("/information_client")
def information_client():
    return render_template('information_client.html')

@app.route("/data_sdelki")
def data_sdelki():
    return render_template('data_sdelki.html')

@app.route("/instrykc")
def attached_documents():
    return render_template('instrykc.html')

@app.route("/users")
def users():
    return render_template('users.html')

@app.route("/enter")
def enter ():
    return render_template('enter.html')

@app.route("/company")
def company ():
    return render_template('company.html')

@app.route("/feedback")
def feedback ():
    return render_template('feedback.html')

@app.route("/another_user")
def another_user ():
    return render_template('another_user.html')

@app.route("/background_tasks")
def background_tasks ():
    return render_template('background_tasks.html')

@app.route("/users_catocka_dannie")
def users_catocka_dannie ():
    return render_template('users_catocka1.html')

@app.route("/users_catocka_dostup")
def users_catocka_dostup ():
    return render_template('users_catocka2.html')

@app.route("/users_sozdanie")
def users_sozdanie ():
    return render_template('users_sozdanie.html')

if __name__ == '__main__':
    app.run(debug=True)