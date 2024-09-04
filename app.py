from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulação de banco de dados simples
clients = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', clients=clients)

@app.route('/add_client', methods=['POST'])
def add_client():
    name = request.form['name']
    service = request.form['service']
    date = request.form['date']
    
    client = {
        'name': name,
        'service': service,
        'date': date
    }
    clients.append(client)
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)



