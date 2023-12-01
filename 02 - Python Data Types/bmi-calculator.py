height = input("Enter your height in meters: 6")  # example: 1.75 meter
weight = input("Enter your weight in kilograms: ")  # example: 65 kg

weight_as_int = int(weight)  # integer function
height_as_float = float(height)  # float function
# remember the BMI formula is weight(kg) / height * height
bmi = weight_as_int / height_as_float ** 2  # using exponent **
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)  # integer function for bmi output
print(bmi_as_int)