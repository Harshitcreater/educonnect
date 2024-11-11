from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dictionary of users with their username as the key, and a dictionary for password and target page
users = {
    "apeksha": {"password": "apeksha123", "page": "apeksha"},
    "ashwani": {"password": "ashwani123", "page": "ashwani"},
    "neeraj":{"password":"neeraj123","page":"neeraj1"}
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Get username and password from the login form
    username = request.form['username']
    password = request.form['password']

    # Check if the username exists and if the password matches for that username
    if username in users and users[username]['password'] == password:
        # Redirect to the corresponding page for the logged-in user using the function name (not the file)
        return redirect(url_for(users[username]["page"]))
    else:
        # If the username or password is incorrect, show an error message
        return render_template('login.html', error="Invalid username or password!")

@app.route('/apeksha')
def apeksha():
    return render_template('apeksha.html')

@app.route('/ashwani')
def ashwani():
    return render_template('ashwani.html')
@app.route('/neeraj1')
def neeraj1():
    return render_template('neeraj1.html')
@app.route('/aschedule')
def aschedule():
    return render_template('aschedule.html')

@app.route('/atschedule')
def atschedule():
    return render_template('atschedule.html')
@app.route('/awschedule')
def awschedule():
    return render_template('awschedule.html')
@app.route('/athschedule')
def athschedule():
    return render_template('athschedule.html')
@app.route('/afschedule')
def afschedule():
    return render_template('afschedule.html')

if __name__ == '__main__':
    app.run(debug=True)
