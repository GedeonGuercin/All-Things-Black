#!/usr/bin/env python

#-----------------------------------------------------------------------
# database.py
# Author: Gedeon, Yenet, Donald
#-----------------------------------------------------------------------

import sys

import sqlite3
#import sqlalchemy
#import sqlalchemy.orm

import database

#-----------------------------------------------------------------------

DATABASE_URL = 'file:bookstore.sqlite?mode=rwc'

def main():

    if len(sys.argv) != 1:
        print('Usage: python create.py', file=sys.stderr)
        sys.exit(1)

    try:
        engine = sqlalchemy.create_engine('sqlite://',
            creator=lambda: sqlite3.connect(DATABASE_URL, uri=True))

        database.Base.metadata.drop_all(engine)
        database.Base.metadata.create_all(engine)

        with sqlalchemy.orm.Session(engine) as session:

            #-----------------------------------------------------------

            book = database.Book(isbn=123,
                title='The Practice of Programming', quantity=500)
            session.add(book)
            book = database.Book(isbn=234,
                title='The C Programming Language', quantity=800)
            session.add(book)
            book = database.Book(isbn=345,
                title='Algorithms in C', quantity=650)
            session.add(book)
            session.commit()

            #-----------------------------------------------------------

            author = database.Author(isbn=123, author='Kernighan')
            session.add(author)
            author = database.Author(isbn=123, author='Pike')
            session.add(author)
            author = database.Author(isbn=234, author='Kernighan')
            session.add(author)
            author = database.Author(isbn=234, author='Ritchie')
            session.add(author)
            author = database.Author(isbn=345, author='Sedgewick')
            session.add(author)
            session.commit()

            #-----------------------------------------------------------

            customer = database.Customer(custid='111',
                custname='Princeton', street='114 Nassau St',
                zipcode='08540')
            session.add(customer)
            customer = database.Customer(custid='222',
                custname='Harvard', street='1256 Mass Ave',
                zipcode='02138')
            session.add(customer)
            customer = database.Customer(custid='333',
                custname='MIT', street='292 Main St',
                zipcode='02142')
            session.add(customer)
            session.commit()

            #-----------------------------------------------------------

            zipcode = database.Zipcode(zipcode='08540',
                city='Princeton', state='NJ')
            session.add(zipcode)
            zipcode = database.Zipcode(zipcode='02138',
                city='Cambridge', state='MA')
            session.add(zipcode)
            zipcode = database.Zipcode(zipcode='02142',
                city='Cambridge', state='MA')
            session.add(zipcode)
            session.commit()

            #-----------------------------------------------------------

            order = database.Order(isbn='123', custid='222',
                quantity=20)
            session.add(order)
            order = database.Order(isbn='345', custid='222',
                quantity=100)
            session.add(order)
            order = database.Order(isbn='123', custid='111',
                quantity=30)
            session.add(order)
            session.commit()

        engine.dispose()

    except Exception as ex:
        print(ex, file=sys.stderr)
        sys.exit(1)

#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()

