#!/usr/bin/env python

#-----------------------------------------------------------------------
# database.py
# Author: Gedeon, Yenet, Donald
#-----------------------------------------------------------------------

import sys
import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative

import database

#-----------------------------------------------------------------------

DATABASE_URL = 'postgresql://rmqiknfc:7HnJzw444FmWxxE_2t_OgbVzABcY6en6@castor.db.elephantsql.com/rmqiknfc'
Base =  sqlalchemy.ext.declarative.declarative_base()

class Post (Base):
    __tablename__ = 'posts'
    title =  sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    body = sqlalchemy.Column(sqlalchemy.String)
    tag = sqlalchemy.Column(sqlalchemy.String)

engine = sqlalchemy.create_engine(url=DATABASE_URL, pool_pre_ping=True)

# def getFoodposts():
#     try:
#         posts = []
#         engine = sqlalchemy.create_engine(url=DATABASE_URL, pool_pre_ping=True)
#             # 'postgresql://',
#             #     creator=lambda: engine.connect(DATABASE_URL), uri=True)
#             # sqlalchemy.schema.MetaData.bind 

#         with sqlalchemy.orm.Session(engine) as session:

#             query_str = "SELECT title, body, tag FROM posts WHERE tag = Food"
#             row  = session.execute(query_str)
#             item = row.fetchone()
#             print(row)
#             print(item)
#             while item is not None:
#                 posts.append(item)
#                 print(posts)
#                 item = row.fetchone()
#                 # sqlalchemy.schema.MetaData.drop_all(bind=engine, checkfirst=True)
#                 # sqlalchemy.schema.MetaData.create_all(bind=engine, checkfirst=True)

#             engine.dispose()

#     except Exception as ex:
#             print(ex, file=sys.stderr)
#             sys.exit(1)
#     return posts

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

                query_str = "SELECT title, body, tag FROM posts WHERE tag = 'Beauty'"
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

                query_str = "SELECT title, body, tag FROM posts WHERE tag = 'Food'"
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

                query_str = "SELECT title, body, tag FROM posts WHERE tag = 'Events'"
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

def insetData(title, body, tag):
    # if len(sys.argv) != 1:
    #     print('Usage: python database.py', file=sys.stderr)
    #     sys.exit(1)

    engine = sqlalchemy.create_engine(url=DATABASE_URL, pool_pre_ping=True)

    with sqlalchemy.orm.Session(engine) as session:
        row = Post(title=title, body=body, tag=tag)
        session.add(row)
        try:
            session.commit()
            return True
        except sqlalchemy.exc.IntegrityError:
            return False
    # try:
    #     posts = []
    #     engine = sqlalchemy.create_engine(url=DATABASE_URL, pool_pre_ping=True)
    #     # 'postgresql://',
    #     #     creator=lambda: engine.connect(DATABASE_URL), uri=True)
    #     # sqlalchemy.schema.MetaData.bind 

    #     with sqlalchemy.orm.Session(engine) as session:

    #         query_str = "INSERT INTO posts (title, body, tag) VALUES (?, ?, ?) "
    #         session.execute(query_str, title, post, tag)
            
    #         engine.commit()
    #         # item = row.fetchone()
    #         # print(row)
    #         # print(item)
    #         # while item is not None:
    #         #     posts.append(item)
    #         #     print(posts)
    #         #     item = row.fetchone()
    #         # sqlalchemy.schema.MetaData.drop_all(bind=engine, checkfirst=True)
    #         # sqlalchemy.schema.MetaData.create_all(bind=engine, checkfirst=True)

    #     # engine.dispose()


    # except Exception as ex:
    #     print(ex, file=sys.stderr)
    #     sys.exit(1)

def addPost(title, body, tag):
    with sqlalchemy.orm.Session(engine) as session:
        row = Post(title=title, body=body, tag=tag)
        session.add(row)
        print(row)
        print(row.title)
        print(row.body)
        print(row.tag)
        try:
            session.commit()
            return True
        except sqlalchemy.exc.IntegrityError:
            return False

if __name__ == '__main__':
    main()

