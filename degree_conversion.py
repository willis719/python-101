# celsius to farenheit
def c_to_f(c_temp):
    f_temp = int(((c_temp * 9 / 5) + 32))
    return f"{f_temp} F"

celsius = int(input("What is the temperature in Celsius? "))

print(c_to_f(celsius))

#farenheit to celsius
def f_to_c(f_temp):
    c_temp = int(((f_temp - 32) * 5/9))
    return f"{c_temp} C"

faren = int(input("What is the temperature in Farenheit? "))
print(f_to_c(faren))






