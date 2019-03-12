import click
from flask import current_app, g
from flask.cli import with_appcontext
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flaskr.schema import Base


def get_db():
    if 'db' not in g:
        engine = create_engine(current_app.config['DATABASE'])
        Session = sessionmaker(bind=engine)
        g.db = Session()
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    session = get_db()
    Base.metadata.drop_all(session.get_bind())
    Base.metadata.create_all(session.get_bind())

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized database')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)