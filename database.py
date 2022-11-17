#!/usr/bin/env python

#-----------------------------------------------------------------------
# database.py
# Author: Gedeon, Yenet, Donald
#-----------------------------------------------------------------------

import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative
import post as postmod

#-----------------------------------------------------------------------

DATABASE_URL = 'postgresql://rmqiknfc:7HnJzw444FmWxxE_2t_OgbVzABcY6en6@castor.db.elephantsql.com/rmqiknfc'

Base = sqlalchemy.ext.declarative.declarative_base()

class Post (Base):
    __tablename__ = 'posts'
    title =  sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    body = sqlalchemy.Column(sqlalchemy.String)
    tag = sqlalchemy.Column(sqlalchemy.String)

engine = sqlalchemy.create_engine(url=DATABASE_URL, pool_pre_ping=True)

#-----------------------------------------------------------------------

def getPost():
    
    posts = []

    with sqlalchemy.orm.Session(engine) as session:
        query = session.query(Post)
        table = query.all()
        for row in table:
            post = postmod.Post(row.title, row.body, row.tag)
            posts.append(post)
    return posts

#-----------------------------------------------------------------------

def addPost(title, body, tag):
    with sqlalchemy.orm.Session(engine) as session:
        row = Post(title=title, body=body, tag=tag)
        session.add(row)
        try:
            session.commit()
            return True
        except sqlalchemy.exc.IntegrityError:
            return False


#-----------------------------------------------------------------------

# For testing:

def write_posts(posts):
    for post in posts:
        print(post.get_title())
        print(post.get_body())
        print(post.get_tag())
        print()

def _test():

    posts = getPost()
    write_posts(posts)

if __name__ == '__main__':
    _test()


