document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.form-container form');

    form.addEventListener('submit', function(event) {
        const nome = document.getElementById('nome').value;
        const email = document.getElementById('email').value;

        // Validação simples de preenchimento
        if (nome.trim() === "" || email.trim() === "") {
            alert("Por favor, preencha todos os campos obrigatórios (Nome e E-mail).");
            event.preventDefault(); // Impede o envio do formulário
            return false;
        }

        // Você pode adicionar validações de formato de e-mail mais complexas aqui
        
        // Se tudo estiver OK, o formulário será enviado ao servidor Python/Flask
        // alert("Dados enviados com sucesso!"); // Se você não usasse o preventDefault
    });
});