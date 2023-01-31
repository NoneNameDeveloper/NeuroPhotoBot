import peewee
from data import config


database = peewee.PostgresqlDatabase(
    database=config.POSTGRES_DATABASE,
    user=config.POSTGRES_USER,
    host=config.POSTGRES_HOST,
    password=config.POSTGRES_PASSWORD
)


class Chat(peewee.Model):
    chat_id = peewee.CharField(unique=True, primary_key=True)

    chat_name = peewee.TextField(default="")  # chat username ( @chat )
    language = peewee.TextField(default="")  # chat language

    photo_count = peewee.BigIntegerField(default=0)  # count processed photos

    class Meta:
        db_table = 'chats'
        database = database


Chat.create_table(True)
