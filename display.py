#!/usr/bin/env python

#-----------------------------------------------------------------------
# display.py
# Author: Bob Dondero
#-----------------------------------------------------------------------

import os
import sys
import psycopg2

#-----------------------------------------------------------------------

def main():

    if len(sys.argv) != 1:
        print('Usage: python display.py', file=sys.stderr)
        sys.exit(1)

    try:
        database_url = os.getenv('DATABASE_URL')

        with psycopg2.connect(database_url) as connection:

            with connection.cursor() as cursor:

                print('-------------------------------------------')
                print('books')
                print('-------------------------------------------')
                cursor.execute("SELECT * FROM user")
                row = cursor.fetchone()
                while row is not None:
                    print(row)
                    row = cursor.fetchone()

    except Exception as ex:
        print(ex, file=sys.stderr)
        sys.exit(1)

#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()