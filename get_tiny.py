#!/usr/bin/env python3
#
# Name: get_tiny.py
# Description: Gets HTTP response from redirection of tinyurl link.
# Generated link has 7 alphanumeric characters, cap-insensitive
# 26
import requests, random, string
from bs4 import BeautifulSoup

def randomString(stringLength=6):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def failed(test_url):
    with open('failed.log', 'a') as n:
        n.write(test_url + "\n")
    return

def main():
    base = "http://tinyurl.com/"

    while True:

        # Create extension at random.
        # It will be between 1 - 6 characters long
        num_of_chars = random.randint(1,6)
        extension = randomString(num_of_chars)

        test_url = base + extension
        print(" {} - ".format(test_url), end='-')

        try:
            r = requests.get(test_url, allow_redirects=True)

        except requests.exceptions.ConnectionError:
            failed(test_url)
            continue
                    
        if (r.status_code == 200):
            soup = BeautifulSoup(r.text, 'html.parser')
            title = soup.title
            print("Success! {}".format(r.status_code))
            filename = extension + ".html"
            with open(filename, 'wb') as f:
                f.write(r.content)
            with open('tinyurl.log', 'a') as w:
                w.write(test_url + "\n")
        elif (r.status_code == 502):
            soup = BeautifulSoup(r.text, 'html.parser')
            title = soup.title
            print("Disrupted Connection! {}".format(r.status_code))
            print("Title: {}".format(title.text))
            filename = extension + ".html"
            with open(filename, 'wb') as f:
                f.write(r.content)
            with open('tinyurl.log', 'a') as w:
                w.write(test_url + "\n")

        else:
            print("Failed - {}".format(r.status_code))
            failed(test_url)
            continue

    return



if __name__ == "__main__":
    main()

