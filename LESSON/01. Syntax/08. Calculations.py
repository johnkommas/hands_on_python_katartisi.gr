#  Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved.
from datetime import datetime
# Εκτυπώστε εδώ το αποτέλεσμα της εξίσωσης:


# Πόσα Χρόνια Έχουν Περάσει από την Προσελλήνωση?
# Για να βρούμε το τρέχων έτος αξιοποιούμε έτοιμη εντολή από την βιβλιοθήκη datetime το "datetime.now().year"
# Η Προσελλήνωση πραγματοποιήθηκε το Έτος 1969
# Χρήσιμες Πληροφορίες:
# Ημερομηνία εκτόξευσης: 16 Ιουλίου 1969, 3:32 μ.μ. GMT+2
# Προσσελήνωση: 20 Ιουλίου 1969, 20:18:04 UTC
# Φορέας: NASA
# Μέλη: Νιλ Άρμστρονγκ, Μάικλ Κόλινς, Μπαζ Όλντριν
current_year = datetime.now().year
test = datetime.now()
# print(test)
# print(type(test))
# print(current_year)
# print(type(current_year))
moon_land_year = 1969
years_from_moon_landing = current_year - moon_land_year
print(f'Έχουν περάσει {years_from_moon_landing} Χρόνια από τότε που πραγματοποιήθηκε η πρώτη προσελλήνωση')
