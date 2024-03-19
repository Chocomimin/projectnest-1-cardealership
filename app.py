from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contactus.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/create_account')
def create_account():
    return render_template('newaccountccode.html')

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgotpassword.html')

@app.route('/car_images')
def car_images():
    return render_template('cars images.html')

@app.route('/car_service')
def car_service():
    return render_template('carsservice.html')

@app.route('/services')
def services():
    return render_template('servicepage.html')

if __name__ == '_main_':
    app.run(debug=True)