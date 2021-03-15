#  Copyright (c) 2021.  Ioannis E. Kommas. All Rights Reserved.

# Create calculate_insurance_cost() function below:


# Initial variables for Maria
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# Estimate Maria's insurance cost
insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500

print("The estimated insurance cost for Maria is " + str(insurance_cost) + " dollars.")

# Initial variables for Omar
age = 35
sex = 1
bmi = 22.2
num_of_children = 0
smoker = 1

# Estimate Omar's insurance cost
insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500

print("The estimated insurance cost for Omar is " + str(insurance_cost) + " dollars.")