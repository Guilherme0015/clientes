from flask import Flask, render_template, request, redirect, url_for

# Lista simples para armazenar os clientes (em um projeto real, você usaria um banco de dados)
clientes = []

app = Flask(__name__)

# Rota para a página inicial (o formulário)
@app.route('/')
def index():
    # Supondo que 'index.html' esteja em uma pasta chamada 'templates'
    return render_template('index.html')

# Rota para receber os dados do formulário
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    if request.method == 'POST':
        # Obtém os dados do formulário
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form.get('telefone', 'Não Informado') # Usa .get para campos opcionais

        novo_cliente = {
            'nome': nome,
            'email': email,
            'telefone': telefone
        }

        # Adiciona o cliente à lista (simulação de salvamento)
        clientes.append(novo_cliente)

        # Log no console do servidor para verificar
        print(f"Cliente Cadastrado: {novo_cliente}")
        
        # Redireciona para uma página de sucesso ou lista
        return f"<h1>Cliente {nome} cadastrado com sucesso!</h1><p><a href='/'>Voltar</a></p>"

if __name__ == '__main__':
    # Para rodar o servidor, você precisa criar uma pasta 'templates' e colocar o 'index.html' dentro dela.
    app.run(debug=True)