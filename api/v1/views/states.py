from api.v1.views import app_views
from models.state import State

@app_views.route('/states', strict_slashes=False, methods=['GET','POST'])
@app_views.route('/states/<state_id>', strict_slashes=False, methods=['GET', 'DELETE', 'PUT'])
def state_page(state_id=None):
    print(request.method)
    if request.method == 'GET':
	@@ -21,12 +21,27 @@ def state_page(state_id=None):
                return jsonify(storage.get(State, state_id).to_dict())
            except AttributeError:
                abort(404)

    elif request.method == 'DELETE':
        obj = storage.get(State, state_id)
        storage.delete(obj)
        storage.save()
        return jsonify({}), 200

    elif request.method == 'PUT':
        obj = storage.get(State, state_id)
        for k, v in request.get_json().items():
            setattr(obj, k, v)
        storage.save()
        return jsonify(obj.to_dict()), 200

    elif request.method == 'POST':
        req_dict = request.get_json().items()
        if not req_dict.has_key('name'):
            return 'Missing name', 400
        for req_key, req_value in request.get_json().items():
            for state_obj in storage.all(State).values():
                state_dict = state_obj.to_dict()
                if req_value == state_dict.get(req_key):
                    return jsonify(state_dict), 201
        return '{}', 200