from peewee import *
from constants import *


db = PostgresqlDatabase(DB_NAME,
                        user=DB_USER,
                        password=DB_PASSWORD,
                        host=DB_HOST,
                        port=DB_PORT)


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = db


class Car(BaseModel):
    engine_type_id = BigIntegerField()
    id = BigIntegerField(unique=True)
    mark = CharField()
    model = CharField()
    person_id = BigIntegerField(null=True)
    price = DecimalField(null=True)

    class Meta:
        table_name = 'car'
        primary_key = False


class EngineType(BaseModel):
    id = BigIntegerField(unique=True)
    type_name = CharField()

    class Meta:
        table_name = 'engine_type'
        primary_key = False


class House(BaseModel):
    floor_count = IntegerField()
    id = BigIntegerField(unique=True)
    price = DecimalField(null=True)

    class Meta:
        table_name = 'house'
        primary_key = False


class ParkingPlace(BaseModel):
    house_id = BigIntegerField(null=True)
    id = BigIntegerField(unique=True)
    is_covered = BooleanField()
    is_warm = BooleanField()
    places_count = IntegerField()

    class Meta:
        table_name = 'parking_place'
        primary_key = False


class Person(BaseModel):
    age = IntegerField()
    first_name = CharField()
    house_id = BigIntegerField(null=True)
    id = BigIntegerField(unique=True)
    money = DecimalField()
    second_name = CharField()
    sex = BooleanField()

    class Meta:
        table_name = 'person'
        primary_key = False


class PersonRelationship(BaseModel):
    primary_person_id = BigIntegerField()
    relationship_type = CharField(null=True)
    secondary_person_id = BigIntegerField()

    class Meta:
        table_name = 'person_relationship'
        indexes = (
            (('secondary_person_id', 'primary_person_id'), True),
        )
        primary_key = False


connection = db.connection()
