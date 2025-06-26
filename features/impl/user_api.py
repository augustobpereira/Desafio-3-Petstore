import requests

class UserAPI:
    BASE_URL = "https://petstore.swagger.io/v2"

    def criar_usuarios(self, lista_usuarios):
        return requests.post(f"{self.BASE_URL}/user/createWithList", json=lista_usuarios)

    def obter_usuario(self, username):
        return requests.get(f"{self.BASE_URL}/user/{username}")

    def atualizar_usuario(self, username, dados_atualizados):
        return requests.put(f"{self.BASE_URL}/user/{username}", json=dados_atualizados)

    def deletar_usuario(self, username):
        return requests.delete(f"{self.BASE_URL}/user/{username}")