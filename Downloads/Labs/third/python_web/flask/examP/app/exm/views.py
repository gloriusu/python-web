from flask import Flask, g, request, jsonify
from functools import wraps
from ..familiar.models import Familiar
from .. import db

from . import familiar_api

api_username = 'admin'
api_password = 'password'


def protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == api_username and auth.password == api_password:
            return f(*args, **kwargs)
        return jsonify({'message': 'Authentication failed!'}), 403

    return decorated


@familiar_api.route('/familiars', methods=['GET'])
@protected
def get_familiars():
    familiars = Familiar.query.all()
    return_values = [{"id": familiar.id,
                      "last_name": familiar.last_name,
                      "first_name": familiar.first_name,
                      "phone_number": familiar.phone_number,
                      "gender": familiar.gender.value,
                      "birth_date": familiar.birth_date,
                      "hobby": familiar.hobby,
                      "category_familiar_id": familiar.category_familiar_id,
                      "user_id": familiar.user_id} for familiar in familiars]

    return jsonify({'Familiars': return_values})


@familiar_api.route('/familiar/<int:id>', methods=['GET'])
@protected
def get_familiar(id):
    familiar = Familiar.query.get_or_404(id)
    return jsonify({"id": familiar.id,
                    "last_name": familiar.last_name,
                    "first_name": familiar.first_name,
                    "phone_number": familiar.phone_number,
                    "gender": familiar.gender.value,
                    "birth_date": familiar.birth_date,
                    "hobby": familiar.hobby,
                    "category_familiar_id": familiar.category_familiar_id,
                    "user_id": familiar.user_id})


@familiar_api.route('/familiar', methods=['POST'])
def add_familiar():
    familiar_date = request.get_json()

    familiar = Familiar(
        last_name=familiar_date['last_name'],
        first_name=familiar_date['first_name'],
        phone_number=familiar_date['phone_number'],
        gender=familiar_date['gender'],
        birth_date=familiar_date['birth_date'],
        hobby=familiar_date['hobby'],
        category_familiar_id=familiar_date['category_familiar_id'],
        user_id=familiar_date['user_id']
    )

    db.session.add(familiar)
    db.session.commit()
    return jsonify({"id": familiar.id,
                    "last_name": familiar.last_name,
                    "first_name": familiar.first_name,
                    "phone_number": familiar.phone_number,
                    "gender": familiar.gender.value,
                    "birth_date": familiar.birth_date,
                    "hobby": familiar.hobby,
                    "category_familiar_id": familiar.category_familiar_id,
                    "user_id": familiar.user_id})


@familiar_api.route('/familiar/<int:id>', methods=['PUT', 'PATCH'])
@protected
def edit_familiar(id):
    familiar = Familiar.query.get(id)
    if not familiar:
        return jsonify({"Message": "Familiar does not exist"})

    update_familiar = request.get_json()

    familiar.last_name = update_familiar['last_name']
    familiar.first_name = update_familiar['first_name']
    familiar.phone_number = update_familiar['phone_number']
    familiar.gender = update_familiar['gender']
    familiar.birth_date = update_familiar['birth_date']
    familiar.hobby = update_familiar['hobby']
    familiar.category_familiar_id = update_familiar['category_familiar_id']
    familiar.user_id = update_familiar['user_id']

    db.session.add(familiar)
    db.session.commit()

    return jsonify({"id": familiar.id,
                    "last_name": familiar.last_name,
                    "first_name": familiar.first_name,
                    "phone_number": familiar.phone_number,
                    "gender": familiar.gender.value,
                    "birth_date": familiar.birth_date,
                    "hobby": familiar.hobby,
                    "category_familiar_id": familiar.category_familiar_id,
                    "user_id": familiar.user_id})


@familiar_api.route('/familiar/<int:id>', methods=['DELETE'])
@protected
def delete_institution(id):
    familiar = Familiar.query.get_or_404(id)
    db.session.delete(familiar)
    db.session.commit()

    return jsonify({'Message': 'The familiar has been deleted!'})