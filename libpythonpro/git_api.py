import requests


def buscar_avatar(usuario):
    """_summary_ Busca o avatar de um usuário no GitHub

    Args:
        usuario (_type_): _description_
        :param usuario: str com o nome de um usuário no github
        : return: str com o link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    res = requests.get(url)
    return res.json()['avatar_url']

if __name__ == '__main__':
    print(buscar_avatar('jose-ewerton'))