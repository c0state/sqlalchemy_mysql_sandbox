import sqlalchemy
from sqlalchemy import create_engine, select
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()
engine = None


def create_schema():
    users = Table('users', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('name', String(64)),
                  Column('full_name', String(64)),
                  )

    metadata.create_all(engine)

def get_users():
    return Table('users', metadata, autoload=True, autoload_with=engine)


def print_data():
    users = get_users()
    connection = engine.connect()

    result = connection.execute(select([users]))
    for user in result:
        print(user)


def insert_data():
    users = get_users()

    insert_action = users.insert().values(name='jack', full_name='Jack Jones')
    engine.execute(insert_action)


if __name__ == "__main__":
    print(sqlalchemy.__version__)

    engine = create_engine('mysql+mysqldb://user:user@localhost/sqlalchemy_sandbox', pool_recycle=3600)

    metadata.drop_all(engine)

    create_schema()

    insert_data()

    print_data()
