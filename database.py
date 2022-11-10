#!/usr/bin/env python

#-----------------------------------------------------------------------
# database.py
# Author: Gedeon, Yenet, Donald
#-----------------------------------------------------------------------

import sys
import contextlib
import sqlalchemy
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
            creator=lambda: sqlalchemy.connect(DATABASE_URL, uri=True))

        database.Base.metadata.drop_all(engine)
        database.Base.metadata.create_all(engine)

        with sqlalchemy.orm.Session(engine) as session:

            query_str = "SELECT , username, major, classyear FROM users "
            row  = session.execute(query_str)
            while row is not None:
                posts = posts.append(row)

        engine.dispose()

    except Exception as ex:
        print(ex, file=sys.stderr)
        sys.exit(1)

#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()

