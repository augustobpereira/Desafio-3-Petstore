# language: pt
Funcionalidade: Gerenciamento de usuários na PetStore

  Contexto:
    Dado que eu envie uma requisição para criar um usuário

  Cenário: Criar um novo usuário com sucesso
    Então o usuário deve ser criado com sucesso

  Cenário: Obter os dados do usuário
    Quando eu buscar os dados do usuário
    Então os dados retornados devem estar corretos

  Cenário: Atualizar os dados do usuário
    Quando eu atualizar os dados do usuário
    Então os dados do usuário devem ser atualizados com sucesso

  Cenário: Deletar o usuário
    Quando eu deletar o usuário
    Então o usuário deve ser removido com sucesso
