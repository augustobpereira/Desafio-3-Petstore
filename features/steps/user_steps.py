from behave import given, when, then
from features.impl.user_api import UserAPI

@given("que eu envie uma requisição para criar um usuário")
def step_impl(context):
    context.api = UserAPI()
    context.usuario = {
        "id": 1,
        "username": "Guto",
        "firstName": "Augusto",
        "lastName": "Pereira",
        "email": "guto@example.com",
        "password": "123456",
        "phone": "999999999",
        "userStatus": 1
    }
    response = context.api.criar_usuarios([context.usuario])
    context.response = response

@then("o usuário deve ser criado com sucesso")
def step_impl(context):
    assert context.response.status_code == 200
    assert context.response.json()["message"] == "ok"

@when("eu buscar os dados do usuário")
def step_impl(context):
    response = context.api.obter_usuario(context.usuario["username"])
    context.response = response

@then("os dados retornados devem estar corretos")
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.json()
    assert data["username"] == context.usuario["username"]
    assert data["email"] == context.usuario["email"]

@when("eu atualizar os dados do usuário")
def step_impl(context):
    context.usuario["firstName"] = "Gustavo"
    response = context.api.atualizar_usuario(context.usuario["username"], context.usuario)
    context.response = response

@then("os dados do usuário devem ser atualizados com sucesso")
def step_impl(context):
    assert context.response.status_code == 200

@when("eu deletar o usuário")
def step_impl(context):
    response = context.api.deletar_usuario(context.usuario["username"])
    context.response = response

@then("o usuário deve ser removido com sucesso")
def step_impl(context):
    assert context.response.status_code == 200