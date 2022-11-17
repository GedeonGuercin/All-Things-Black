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

DATABASE_URL = 'postgresql://rmqiknfc:7HnJzw444FmWxxE_2t_OgbVzABcY6en6@castor.db.elephantsql.com/rmqiknfc'

def getData(type):

    if type == True:
        try:
            posts = []
            engine = sqlalchemy.create_engine(url=DATABASE_URL, pool_pre_ping=True)
            # 'postgresql://',
            #     creator=lambda: engine.connect(DATABASE_URL), uri=True)
            # sqlalchemy.schema.MetaData.bind 

            with sqlalchemy.orm.Session(engine) as session:

                query_str = "SELECT title, body, tag FROM posts "
                row  = session.execute(query_str)
                item = row.fetchone()
                
                print(item)
                while item is not None:
                    posts.append(item)
                    print(item)
                    item = row.fetchone()
                # sqlalchemy.schema.MetaData.drop_all(bind=engine, checkfirst=True)
                # sqlalchemy.schema.MetaData.create_all(bind=engine, checkfirst=True)

            engine.dispose()
        except Exception as ex:
            print(ex, file=sys.stderr)
            sys.exit(1)
        return posts
    elif type == 'beauty':
        try:
            posts = []
            engine = sqlalchemy.create_engine(url=DATABASE_URL, pool_pre_ping=True)
            

            with sqlalchemy.orm.Session(engine) as session:

                query_str = "SELECT * FROM posts WHERE tag = 'Beauty'"
                row  = session.execute(query_str)
                item = row.fetchone()
                
                while item is not None:
                    posts.append(item)
                    print(item)
                    item = row.fetchone()
                # sqlalchemy.schema.MetaData.drop_all(bind=engine, checkfirst=True)
                # sqlalchemy.schema.MetaData.create_all(bind=engine, checkfirst=True)

            engine.dispose()
        except Exception as ex:
            print(ex, file=sys.stderr)
            sys.exit(1)
        return posts
    elif type == 'food':
        try:
            posts = []
            engine = sqlalchemy.create_engine(url=DATABASE_URL, pool_pre_ping=True)
            

            with sqlalchemy.orm.Session(engine) as session:

                query_str = "SELECT * FROM posts WHERE tag = 'Food'"
                row  = session.execute(query_str)
                item = row.fetchone()
                
   
                while item is not None:
                    posts.append(item)
                    print(item)
                    item = row.fetchone()
                # sqlalchemy.schema.MetaData.drop_all(bind=engine, checkfirst=True)
                # sqlalchemy.schema.MetaData.create_all(bind=engine, checkfirst=True)

            engine.dispose()
        except Exception as ex:
            print(ex, file=sys.stderr)
            sys.exit(1)
        return posts
    elif type == 'events':
        try:
            posts = []
            engine = sqlalchemy.create_engine(url=DATABASE_URL, pool_pre_ping=True)
            

            with sqlalchemy.orm.Session(engine) as session:

                query_str = "SELECT * FROM posts WHERE tag = 'Events'"
                row  = session.execute(query_str)
                item = row.fetchone()
         
                while item is not None:
                    posts.append(item)
                    print(item)
                    item = row.fetchone()
                # sqlalchemy.schema.MetaData.drop_all(bind=engine, checkfirst=True)
                # sqlalchemy.schema.MetaData.create_all(bind=engine, checkfirst=True)

            engine.dispose()
        except Exception as ex:
            print(ex, file=sys.stderr)
            sys.exit(1)
        return posts
    else:
        try:
            posts = []
            engine = sqlalchemy.create_engine(url=DATABASE_URL, pool_pre_ping=True)
            # 'postgresql://',
            #     creator=lambda: engine.connect(DATABASE_URL), uri=True)
            # sqlalchemy.schema.MetaData.bind 

            with sqlalchemy.orm.Session(engine) as session:

                query_str = "SELECT username, major, classyear FROM users "
                row  = session.execute(query_str)
                item = row.fetchone()
                print(row)
                print(item)
                while item is not None:
                    posts.append(item)
                    item = row.fetchone()
                # sqlalchemy.schema.MetaData.drop_all(bind=engine, checkfirst=True)
                # sqlalchemy.schema.MetaData.create_all(bind=engine, checkfirst=True)

            engine.dispose()


        except Exception as ex:
            print(ex, file=sys.stderr)
            sys.exit(1)
        return posts

#-----------------------------------------------------------------------

def insetData(title, post, tag):
    # if len(sys.argv) != 1:
    #     print('Usage: python database.py', file=sys.stderr)
    #     sys.exit(1)
    try:
        posts = []
        engine = sqlalchemy.create_engine(url=DATABASE_URL, pool_pre_ping=True)
        # 'postgresql://',
        #     creator=lambda: engine.connect(DATABASE_URL), uri=True)
        # sqlalchemy.schema.MetaData.bind 

        with sqlalchemy.orm.Session(engine) as session:

            query_str = "INSERT INTO posts (title, post, tag) VALUES (?, ?, ?) "
            session.execute(query_str, title, post, tag)
            
            engine.commit()
            # item = row.fetchone()
            # print(row)
            # print(item)
            # while item is not None:
            #     posts.append(item)
            #     print(posts)
            #     item = row.fetchone()
            # sqlalchemy.schema.MetaData.drop_all(bind=engine, checkfirst=True)
            # sqlalchemy.schema.MetaData.create_all(bind=engine, checkfirst=True)

        # engine.dispose()


    except Exception as ex:
        print(ex, file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()

