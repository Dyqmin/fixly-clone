from flask import Blueprint

register = Blueprint('register', __name__, template_folder='services')


@register.route('/register/', methods=['GET'])
def register_user():
    return 'register'
