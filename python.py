from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para armazenar temporariamente os dados dos clientes
# Em uma aplicação real, você usaria um banco de dados (SQLite, PostgreSQL, etc.)
clientes = []
id_contador = 1

@app.route('/')
def index():
    # Renderiza a página principal, passando a lista de clientes para exibição
    return render_template('cadastro.html', clientes=clientes)

@app.route('/cadastrar', methods=['POST'])
def cadastrar_cliente():
    global id_contador
    if request.method == 'POST':
        # 1. Captura os dados do formulário
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        
        # 2. Cria um dicionário com os dados do novo cliente
        novo_cliente = {
            'id': id_contador,
            'nome': nome,
            'email': email,
            'telefone': telefone
        }
        
        # 3. Adiciona o novo cliente à lista e incrementa o contador
        clientes.append(novo_cliente)
        id_contador += 1
        
        # 4. Redireciona o usuário de volta para a página inicial (que exibirá o novo cliente)
        return redirect(url_for('index'))

if __name__ == '__main__':
    # Inicializa o servidor Flask
    # O 'debug=True' permite que o servidor reinicie automaticamente após alterações
    app.run(debug=True)