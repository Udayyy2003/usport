from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/events')
def events():
    return render_template('events.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/pricing')
def pricing():
    return render_template('pricing.html')


@app.route('/ecommerce')
def ecommerce():
    return render_template('ecommerce.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
