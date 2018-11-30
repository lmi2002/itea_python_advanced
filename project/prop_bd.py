from peewee import *
import datetime

database = SqliteDatabase('db_task.db')


class BaseModel(Model):

    class Meta:
        database = database


class Task(BaseModel):
    id = PrimaryKeyField()
    task_name = CharField()
    started_at = DateTimeField(default=datetime.datetime.now)
    finished_at =DateTimeField()
    status = CharField()
    #pid = PrimaryKeyField()


if __name__ == '__main__':

    # Connect to our database
    database.connect()

    # Create the tables
    database.create_tables([Task])