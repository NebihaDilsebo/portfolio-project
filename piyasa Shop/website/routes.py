from flask import render_template
from website import app


# For static HTML pages
@app.route('/contact-us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

# For dynamic pages
@app.route('/')
@app.route('/mens')
@app.route('/womens')
@app.route('/kids')
@app.route('/explore')
def dynamic_page():
    # Fetch data and pass it to the common template as needed
    # ...

    return render_template('index.html', products=products, page_title="Pyasa Fashion")

