from services.reqres_in.users.get_user import GetUser
from services.reqres_in.users.post_create import CreateUser

def test_get_user(env_config):
    user_id = CreateUser(env_config).create_user(
        name="Wowa",
        job="Plumber"
    ).json()["id"]
    print(user_id)
    response = GetUser(env_config).get_user(user_id)

    assert response.status_code == 200
    assert "data" in response.json()
    assert  response.json()['id'] == user_id

    # Статус-код: 200 OK.
    # Наличие объекта data в JSON.
    # Соответствие ID в ответе запрошенному ID.
