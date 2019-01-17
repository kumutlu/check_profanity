
"""
import urllib.request, urllib.error
import urllib.parse



def read_text():
    quotes = open(r"C:\movie_quotes.txt")
    contents_of_file = quotes.read()
    print (contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):

    connection = urllib.request.urlopen("http://wdylike.appspot.com/?q=" + text_to_check )
    print(connection.read())
    connection.close()


read_text()
"""

from urllib.request import FancyURLopener


def read_text():
    quotes = open(r"C:\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


class MyOpener(FancyURLopener):
    version = "My new User-Agent" # Set this to a string you want for your user agent

    def check_profanity(text_to_check):
        myopener = MyOpener()
        page = myopener.open("http://www.wdylike.appspot.com/?q="+text_to_check)
        output = page.read()
        print(output)

read_text()