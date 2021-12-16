import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from graphene_sqlalchemy_filter import FilterableConnectionField, FilterSet
from models import User as UserModel, Todo as TodoModel

ALL_OPERATIONS = ['eq', 'ne', 'like', 'is_null', 'in', 'not_in', 'lt', 'gt', 'gte', 'range']


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node,)


class Todo(SQLAlchemyObjectType):
    class Meta:
        model = TodoModel
        interfaces = (relay.Node,)


class UserFilter(FilterSet):
    class Meta:
        model = UserModel
        fields = {
            'id': ALL_OPERATIONS,
            'username': ALL_OPERATIONS
        }


class TodoFilter(FilterSet):
    class Meta:
        model = TodoModel
        fields = {
            'id': ALL_OPERATIONS,
            'important': ALL_OPERATIONS,
            'createdAt': ALL_OPERATIONS
        }


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_todos = SQLAlchemyConnectionField(Todo.connection)
    all_users = SQLAlchemyConnectionField(User.connection, sort=None)
    user = FilterableConnectionField(connection=User, filters=UserFilter(), sort=User.sort_argument())
    todo = FilterableConnectionField(connection=Todo, filters=TodoFilter(), sort=Todo.sort_argument())


schema = graphene.Schema(query=Query)
