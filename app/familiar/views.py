from flask import url_for, render_template, flash, redirect
from flask_login import current_user, login_required

from . import familiar_blueprint
from .forms import FamiliarForm, CategoryForm
from .models import Familiar, Category
from .. import db


@familiar_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def data_list():
    familiar = Familiar.query.all()
    return render_template('data_list.html', familiar=familiar)


@familiar_blueprint.route('/add_familiar', methods=['GET', 'POST'])
@login_required
def add_familiar():
    familiar_form = FamiliarForm()
    familiar_form.category.choices = [(category.id, category.familiarity_level) for category in Category.query.all()]
    if familiar_form.validate_on_submit():
        familiar = Familiar(last_name=familiar_form.last_name.data, first_name=familiar_form.first_name.data,
                            phone_number=familiar_form.phone_number.data, gender=familiar_form.gender.data,
                            birth_date=familiar_form.birth_date.data,
                            category_familiar_id=familiar_form.category.data,
                            hobby=familiar_form.hobby.data,
                            user_id=current_user.id)

        db.session.add(familiar)
        db.session.commit()

        return redirect(url_for('familiar.data_list'))
    return render_template('add.html', familiar_form=familiar_form)


@familiar_blueprint.route('/<id>', methods=['GET', 'POST'])
def detail_familiar(id):
    familiar = Familiar.query.get_or_404(id)
    return render_template('detail.html', familiar=familiar)


@familiar_blueprint.route('/delete/<id>', methods=['GET', 'POST'])
def delete_familiar(id):
    familiar = Familiar.query.get_or_404(id)

    if current_user.id == familiar.user_id:
        db.session.delete(familiar)
        db.session.commit()
        return redirect(url_for('familiar.data_list'))

    flash('This is not your post', category='warning')
    return redirect(url_for('familiar.detail_familiar', id=id))


@familiar_blueprint.route('/edit/<id>', methods=['GET', 'POST'])
def edit_familiar(id):
    familiar = Familiar.query.get_or_404(id)
    if current_user.id != familiar.user_id:
        flash('This is not your post', category='warning')
        return redirect(url_for('familiar.detail_familiar', familiar=familiar))

    familiar_form = FamiliarForm()
    familiar_form.category.choices = [(category.id, category.familiarity_level) for category in Category.query.all()]

    if familiar_form.validate_on_submit():
        familiar.last_name = familiar_form.last_name.data
        familiar.first_name = familiar_form.first_name.data
        familiar.phone_number = familiar_form.phone_number.data
        familiar.gender = familiar_form.gender.data
        familiar.birth_date = familiar_form.birth_date.data
        familiar.hobby = familiar_form.hobby.data
        familiar.category_familiar_id = familiar_form.category.data

        db.session.add(familiar)
        db.session.commit()

        flash('Has been update', category='access')
        return redirect(url_for('familiar.detail_familiar', id=id))

    familiar_form.last_name.data = familiar.last_name
    familiar_form.first_name.data = familiar.first_name
    familiar_form.phone_number.data = familiar.phone_number
    familiar_form.gender.data = familiar.gender
    familiar_form.birth_date.data = familiar.birth_date
    familiar_form.hobby.data = familiar.hobby
    familiar_form.category.data = familiar.category_familiar_id

    return render_template('add.html', familiar_form=familiar_form)


@familiar_blueprint.route('/crud_categories', methods=['GET', 'POST'])
def category_crud():
    familiar_form = CategoryForm()

    if familiar_form.validate_on_submit():
        category = Category(familiarity_level=familiar_form.name.data)

        db.session.add(category)
        db.session.commit()
        flash('Category added')
        return redirect(url_for('.category_crud'))

    categories = Category.query.all()
    return render_template('category_crud.html', categories=categories, familiar_form=familiar_form)


@familiar_blueprint.route('/update_category/<id>', methods=['GET', 'POST'])
def update_category(id):
    category = Category.query.get_or_404(id)
    category_form = CategoryForm()
    if category_form.validate_on_submit():
        category.familiarity_level = category_form.name.data

        db.session.add(category)
        db.session.commit()
        flash('Category edited')
        return redirect(url_for('.category_crud'))

    category_form.name.data = category.level
    categories = Category.query.all()
    return render_template('category_crud.html', categories=categories, familiar_form=category_form)


@familiar_blueprint.route('/delete_category/<id>', methods=['GET'])
@login_required
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()

    flash('Category delete', category='access')
    return redirect(url_for('.category_crud'))
