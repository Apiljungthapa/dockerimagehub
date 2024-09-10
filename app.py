from flask import Flask, render_template_string, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add authentication logic here
        return f'Logged in as {username}'
    return render_template_string(login_html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
