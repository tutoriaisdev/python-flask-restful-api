from flask_restful import abort, request, Resource

USERS = {
    'usuario1': {'nome': 'Joao'},
    'usuario2': {'nome': 'Maria'},
}

def abort_if_user_doesnt_exist(user_id):
    if user_id not in USERS:
        abort(404, message="Usuário {} não existe.".format(user_id))

class User(Resource):
    def get(self, user_id):
        abort_if_user_doesnt_exist(user_id)
        return USERS[user_id]

    def delete(self, user_id):
        abort_if_user_doesnt_exist(user_id)
        del USERS[user_id]
        return '', 204

    def put(self, user_id):
        json_data = request.get_json()
        USERS[user_id] = json_data
        return json_data, 201

class UserList(Resource):
    def get(self):
        return USERS

    def post(self):
        json_data = request.get_json()
        user_id = int(max(USERS.keys()).lstrip('usuario')) + 1
        user_id = 'usuario%i' % user_id
        USERS[user_id] = json_data
        return USERS[user_id], 201
