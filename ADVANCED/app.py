#  Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved.
import math
import time
from datetime import datetime as dt
import calendar


def in_pow():
    print('Γνωρίζουμε ότι: χ^ν = χ * χ * χ.....χ <--- (ν φορές)')
    time.sleep(10)
    print('Αν η Βάση είναι 0 τότε το αποτέλεσμα είναι πάντα 0')
    time.sleep(10)
    print(f'Για Παράδειγμα: Αν χ = 0 και ν = 3 Τότε:  0^3 = 0 * 0 * 0 = {math.pow(0, 3)}')
    print('--------------------------------------------------------------------------------')
    time.sleep(10)
    print(f'Αν ο εκθέτης είναι 0 τότε το αποτέλεσμα είναι πάντα 1')
    time.sleep(10)
    print(f'Για Παράδειγμα: Αν χ = 5 και ν = 0 Τότε: 5^0 = {math.pow(5, 0)}')
    time.sleep(10)
    print('--------------------------------------------------------------------------------')
    print('Τι γίνεται όμως στην περίπτωση που η Βάση έιναι 0 και ο εκθέτης είναι 0 ? 0^0')
    print('Το αποτέλεσμα είναι 0 ή 1 ?')
    print('--------------------------------------------------------------------------------')
    χ = input('Πατήστε ένα Πλήκτρο για να Δούμε την Λύση')
    print('Για να προσεγγίσουμε την απάντηση θα χρειαστεί να παίξουμε με τα όρια "lim"')
    print(f'  1 ^   1 = {math.pow(1, 1)}')
    time.sleep(3)
    print(f'0.9 ^ 0.9 = {math.pow(.9, .9)}')
    time.sleep(3)
    print(f'0.8 ^ 0.8 = {math.pow(.8, .8)}')
    time.sleep(3)
    print(f'0.7 ^ 0.7 = {math.pow(.7, .7)}')
    time.sleep(3)
    print(f'0.6 ^ 0.6 = {math.pow(.6, .6)}')
    time.sleep(3)
    print(f'0.5 ^ 0.5 = {math.pow(.5, .5)}')
    time.sleep(3)
    print(f'0.4 ^ 0.4 = {math.pow(.4, .4)}')
    x = input('ΝΑ ΣΥΝΕΧΙΣΩ Η ΒΡΗΚΑΜΕ ΤΟ ΑΠΟΤΕΛΕΣΜΑ?')
    print(f'0.3 ^ 0.3 = {math.pow(.3, .3)}')
    time.sleep(3)
    print(f'0.2 ^ 0.2 = {math.pow(.2, .2)}')
    time.sleep(3)
    print(f'0.1 ^ 0.1 = {math.pow(.1, .1)}')
    time.sleep(3)
    print(f'0.01 ^ 0.01 = {math.pow(.01, .01)}')
    time.sleep(3)
    print(f'0.0001 ^ 0.0001 = {math.pow(.0001, .0001)}')
    time.sleep(3)
    print(f'0.000001 ^ 0.000001 = {math.pow(.000001, .000001)}')
    time.sleep(3)
    print(f'0.00000000001 ^ 0.00000000001 = {math.pow(.00000000001, .00000000001)}')
    time.sleep(3)
    print(
        f'0.000000000000000000001 ^ 0.000000000000000000001 = {math.pow(.000000000000000000001, .000000000000000000001)}')
    time.sleep(3)
    print(f'Η Απάντηση είναι: Όταν η Βάση και ο εκθέτης είναι 0 το αποτελεσμα είναι πάντα: {math.pow(0, 0)}')


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


