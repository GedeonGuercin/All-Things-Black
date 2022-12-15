#!/usr/bin/env python

#-----------------------------------------------------------------------
# database.py
# Author: Gedeon, Yenet, Donald
#-----------------------------------------------------------------------

import sys
import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative

#-----------------------------------------------------------------------

DATABASE_URL = 'postgresql://rmqiknfc:7HnJzw444FmWxxE_2t_OgbVzABcY6en6@castor.db.elephantsql.com/rmqiknfc'
Base =  sqlalchemy.ext.declarative.declarative_base()

class Post (Base):
    __tablename__ = 'posts'
    title =  sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    body = sqlalchemy.Column(sqlalchemy.String)
    tag = sqlalchemy.Column(sqlalchemy.String)

class User (Base):
    __tablename__ = 'users'
    username =  sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    password = sqlalchemy.Column(sqlalchemy.String)

engine = sqlalchemy.create_engine(url=DATABASE_URL, pool_pre_ping=True)

#-----------------------------------------------------------------------

def get_password(username):
    with sqlalchemy.orm.Session(engine) as session:
        query = session.query(User).filter(User.username==username)
        try:
            row = query.one()
            return row.password
        except sqlalchemy.exc.NoResultFound:
            return None

#-----------------------------------------------------------------------

def getData(type):
    if type == True:
        try:
            posts = []
            engine = sqlalchemy.create_engine(url=DATABASE_URL, pool_pre_ping=True)

            with sqlalchemy.orm.Session(engine) as session:

                query_str = "SELECT title, body, tag FROM posts "
                row  = session.execute(query_str)
                item = row.fetchone()
                
                print(item)
                while item is not None:
                    posts.append(item)
                    print(item[0])
                    item = row.fetchone()

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

            engine.dispose()
        except Exception as ex:
            print(ex, file=sys.stderr)
            sys.exit(1)
        return posts
    else:
        try:
            posts = []
            engine = sqlalchemy.create_engine(url=DATABASE_URL, pool_pre_ping=True)
            with sqlalchemy.orm.Session(engine) as session:

                query_str = "SELECT username, major, classyear FROM users "
                row  = session.execute(query_str)
                item = row.fetchone()
                print(row)
                print(item)
                while item is not None:
                    posts.append(item)
                    item = row.fetchone()

            engine.dispose()


        except Exception as ex:
            print(ex, file=sys.stderr)
            sys.exit(1)
        return posts

#-----------------------------------------------------------------------

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

#-----------------------------------------------------------------------

def delete_post(title):
    with sqlalchemy.orm.Session(engine) as session:
        session.query(Post).filter(Post.title==title).delete()
        session.commit()

if __name__ == '__main__':
    main()

