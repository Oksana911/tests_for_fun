from peewee import *
from tests.conftest import db


class BaseModel(Model):
    class Meta:
        database = db


class House(BaseModel):
    floor_count = AutoField(column_name='floor_count')
    price = DecimalField(column_name='price')

    class Meta:
        table_name = 'House'


class Person(BaseModel):
    first_name = CharField(column_name='first_name')
    second_name = CharField(column_name='second_name')
    age = AutoField(column_name='age')
    sex = BooleanField(column_name='sex')
    money = DecimalField(column_name='money')
    house_id = ForeignKeyField(House.id, related_name='houses')

    class Meta:
        table_name = 'Person'


class EngineType(BaseModel):
    type_name = CharField(column_name='type_name')

    class Meta:
        table_name = 'EngineType'


class Car(BaseModel):
    mark = CharField(column_name='mark')
    model = CharField(column_name='model')
    price = DecimalField(column_name='price')
    engine_type_id = ForeignKeyField(EngineType.id, related_name='engines')
    person_id = ForeignKeyField(Person.id, related_name='persons')

    class Meta:
        table_name = 'Car'
