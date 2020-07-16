#! python3
# a_joke_telling_program.py - The program will tell you a random joke from https://jokes.lol/

import bs4
import requests
import sys

print('Would you like to hear a joke?')
while True:
    hear_joke = 'y' #  input('y or n').lower()
    if hear_joke == 'y':
        res = requests.get('https://jokes.lol/random-jokes/')
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        jokes = soup.select('.query-field')
        print(jokes[0].text)

        #for i in range(0, len(jokes)):
        #    print(jokes[i])


    #elif hear_joke == 'n':
    #    sys.exit()
    sys.exit()