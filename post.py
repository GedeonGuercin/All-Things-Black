#!/usr/bin/env python

#-----------------------------------------------------------------------
# post.py
# Author: Gedeon Guercin
#-----------------------------------------------------------------------

class Post:

    def __init__(self, title, body, tag):
        self._title = title
        self._body = body
        self._tag = tag

    def get_title(self):
        return self._title

    def get_body(self):
        return self._body
    
    def get_tag(self):
        return self._tag

    def to_tuple(self):
        return (self._title, self._body, self._tag)

#-----------------------------------------------------------------------

def _test():
    post = Post('PBMA Resume Workshop', 'Polish Your Resume with PBMA this Friday!', 'Beauty')
    print(post.to_tuple())


if __name__ == '__main__':
    _test()
