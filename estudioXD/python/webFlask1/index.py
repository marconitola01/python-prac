from flask import Flask, render_template
app = Flask(__name__)


#home route
@app.route('/')
def home():
    return render_template('home.html')
#about route
@app.route('/about')
def about():
    return render_template('about.html')

#establecemos que esta es mi clase principal
if __name__ == "__main__":
    app.run(debug=True)

