from flask_login import UserMixin

from {{ cookiecutter.project_name }}.external import db


roles_users = db.Table('roles_users',
                       db.Column('role_id', db.ForeignKey('role.id',
                                                          ondelete='CASCADE'),
                                 nullable=False),
                       db.Column('user_id', db.ForeignKey('user.id',
                                                          ondelete='CASCADE'),
                                 nullable=False),
                       db.UniqueConstraint('role_id', 'user_id',
                                           name='ux_role_user'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)

