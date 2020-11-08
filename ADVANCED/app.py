#  Copyright (c) 2020.  Ioannis E. Kommas. All Rights Reserved.
import math
import time
from datetime import datetime as dt
import calendar


def cryptography():
    # Public Agreement for (g,p)
    g = 3
    p = 17
    print(f'Alice and Bob Agreed for a Public g = {g} and p= {p}')
    time.sleep(3)
    # Private Numbers
    Alice_private_number = 15
    Bob_private_number = 13
    print('Both Alice and Bob Generated a Private Number that we do not Know')
    time.sleep(3)
    # Public Results
    Alice_public_result = g ** Alice_private_number % p
    print(f'Alice Says in Public:{Alice_public_result}')
    time.sleep(3)
    Bob_public_results = g ** Bob_private_number % p
    print(f'Bob Says in Public: {Bob_public_results}')
    time.sleep(3)
    # KEY
    Alice_key = Bob_public_results ** Alice_private_number % p
    print(f'Alice Listened Bob\'s Public Key and now knows the key: {Alice_key}')
    time.sleep(3)
    Bob_key = Alice_public_result ** Bob_private_number % p
    print(f'Bob Listened Alice\'s Public Key and now he also knows the Key: {Bob_key}')
    time.sleep(3)
    print('Both Alice and Bob keep the Final Key Private... it is the message after all')
    print(f'Now we need to check if both keys are the Same: Alice_key == Bob_key : {Alice_key == Bob_key}')


def leap_year():
    def answer(year):
        yes_or_no = ('Είναι' if calendar.isleap(year) else 'Δεν Είναι')
        print(f'Το Έτος {year} {yes_or_no} Δίσεκτο Έτος')

    answer(dt.now().year)
    answer(2100)

    print('\n\n', calendar.month(dt.now().year, 2))
    print(calendar.month(2100, 2))
