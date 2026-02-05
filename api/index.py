from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stealth')
def secure():
    return render_template('stealth.html')

@app.route('/secure')
def secure():
    return render_template('secure.html')

# Add a simple health check or manifest route if needed for PWA
@app.route('/manifest.json')
def manifest():
    return {
        "name": "MyCallCode Pro",
        "short_name": "MyCallCode",
        "display": "standalone",
        "background_color": "#0b0e14",
        "theme_color": "#00f2fe",
        "icons": [] 
    }

if __name__ == '__main__':
    app.run(debug=True)

