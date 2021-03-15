#  Copyright (c) 2021.  Ioannis E. Kommas. All Rights Reserved.

# Να γράψετε πρόγραμμα που θα ζητάει την τιμή πώλησης ενός προϊόντος κάποιου καταστήματος και το ποσοστό της έκπτωσης
# που έχει αυτό, υπολογίζοντας και εμφανίζοντας το ποσό της έκπτωσης και το τελικό πληρωτέο ποσό.
# Το ποσοστό θα δίνεται ως ακέραιος αριθμός.

# Είσοδος
sales_price = abs(float(input('Sales Price: ')))
discount = abs(int(input('Discount: ')))

# Επεξεργασία
discount_value = sales_price * (discount /100)
final_sales_price = sales_price - discount_value

# Έξοδος
print(f"""
Sales Price:\t\t : {sales_price} EUR
Discount:\t\t\t : {discount} %
Discount Value:\t\t : {discount_value} EUR
Final Sales Price:\t : {final_sales_price} EUR
""")