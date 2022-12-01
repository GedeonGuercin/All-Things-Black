#!/usr/bin/env python

#-----------------------------------------------------------------------
# database.py
# Author: Gedeon, Yenet, Donald
#-----------------------------------------------------------------------

import sys

import alchemy
import sqlalchemy.orm

import database

#-----------------------------------------------------------------------

DATABASE_URL = 'postgres://rmqiknfc:7HnJzw444FmWxxE_2t_OgbVzABcY6en6@castor.db.elephantsql.com/rmqiknfc'

def getData():

    if len(sys.argv) != 1:
        print('Usage: python database.py', file=sys.stderr)
        sys.exit(1)

    try:
        engine = sqlalchemy.create_engine('postgres://',
            creator=lambda: sqlite3.connect(DATABASE_URL, uri=True))

        database.Base.metadata.drop_all(engine)
        database.Base.metadata.create_all(engine)

        with sqlalchemy.orm.Session(engine) as session:

            #-----------------------------------------------------------

            user = database.Book(isbn=123,
                title='The Practice of Programming', quantity=500)
            session.add(book)
            book = database.Book(isbn=234,
                title='The C Programming Language', quantity=800)
            session.add(book)
            book = database.Book(isbn=345,
                title='Algorithms in C', quantity=650)
            session.add(book)
            session.commit()

        engine.dispose()

    except Exception as ex:
        print(ex, file=sys.stderr)
        sys.exit(1)

#-----------------------------------------------------------------------

def deletePost():
    with sqlalchemy.orm.Session(engine) as session:
        session.query(Post).delete()
        session.commit()

if __name__ == '__main__':
    main()

