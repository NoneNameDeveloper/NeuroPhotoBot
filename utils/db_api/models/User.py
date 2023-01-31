import peewee
from datetime import datetime
from data import config


database = peewee.PostgresqlDatabase(
    database=config.POSTGRES_DATABASE,
    user=config.POSTGRES_USER,
    host=config.POSTGRES_HOST,
    password=config.POSTGRES_PASSWORD
)


class User(peewee.Model):
    user_id = peewee.BigIntegerField(unique=True, primary_key=True)  # unique telegram user id
    login = peewee.TextField(default="")  # user username ( @username )
    reg_date = peewee.DateTimeField(default=datetime.utcnow())  # time, user registered in bot
    language = peewee.TextField(default='')  # user language

    photo_count = peewee.BigIntegerField(default=0)  # count of processed photos

    class Meta:
        db_table = 'users'
        database = database


User.create_table(True)
