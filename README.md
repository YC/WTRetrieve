#Webpage Title Retriever
A small tool for retrieving the title of webpages.

##Dependencies
Python  
**Libraries**: lxml, requests

##Usage
    WTRetrieve.py [-h] [-f file] [--nolinks] [--nonewlines] [<URL>]

###Examples

Retrieve the title for Github

    WTRetrieve.py https://github.com

Retrieve the titles for the links in test.txt

    WTRetrieve.py -f test.txt

Retrieve just the titles for the links in test.txt

    WTRetrieve.py --nonewline --nolinks -f test.txt
