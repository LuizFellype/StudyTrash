def convert_f_2_c():
    temp = float(input("Enter temperature in Fahrenheit: "))
    celsius = (temp - 32) * 5/9
    print(f"{temp} in Fahrenheit is equal to {celsius} in Celsius")
    

convert_f_2_c()