from services.base_api import BaseAPI

class GetUser(BaseAPI):
    def __init__(self, env_config):
        """
        Args:
            env_config (EnvironmentConfig): Конфигурация окружения из фикстуры
        """
        super().__init__(base_url=env_config.reqres_url, api_key=env_config.reqres_api_key)


    def get_user(self, user_id):
        response = self.session.get(f"{self.base_url}/users/{user_id}")
        return response


# {'name': 'John Doe', 'job': 'QA Engineer', 'id': '313',
#  'createdAt': '2026-03-30T15:05:14.099Z',
#  '_meta': {'powered_by': 'ReqRes', 'docs_url': 'https://app.reqres.in/documentation'
# , 'upgrade_url': 'https://app.reqres.in/upgrade',
# 'example_url': 'https://app.reqres.in/examples/notes-app',
#            'variant': 'v1_b',
#            'message': 'Need more than fake data? Projects give you real CRUD + auth in minutes.',
# 'cta': {'label': 'Get started', 'url': 'https://app.reqres.in/upgrade'}, 'context': 'legacy_success'}}



# Реализуй метод get_user(user_id). /api/users/{id}
# Используй self.session.get().
#
# Тест: В tests/test_get_user.py проверь:
# Статус-код: 200 OK.
# Наличие объекта data в JSON.
# Соответствие ID в ответе запрошенному ID.