
# Part 1: Functions to convert temperature to different scales (Fahrenheit, Celsius, Kelvin)

def fahrenheit_to_celsius(t):
    """
    A function that converts a temperature in Fahrenheit to Celsius
    """
    t_celsius = (t-32) * (5/9)
    return t_celsius


def fahrenheit_to_kelvin(t):
    """
    A function that converts a temperature in Fahrenheit to Kelvin
    """
    t_kelvin = (t-32) * (5/9) + 273.15
    return t_kelvin


def celsius_to_fahrenheit(t):
    """
    A function that converts a temperature in Celsius to Fahrenheit
    """
    t_fahrenheit = (t * (9/5)) + 32
    return t_fahrenheit


def celsius_to_kelvin(t):
    """
    A function that converts a temperature in Celsius to Kelvin
    """
    t_kelvin = t + 273.15
    return t_kelvin


def kelvin_to_fahrenheit(t):
    """
    A function that converts a temperature in Kelvin to Fahrenheit
    """
    t_fahrenheit = (t-273.15) * (9/5) + 32
    return t_fahrenheit


def kelvin_to_celsius(t):
    """
    A function that converts a temperature in Kelvin to Celsius
    """
    t_celsius = t - 273.15
    return t_celsius

# Part 2: Functions to ask the user to enter a temperature and then convert it to different scales using the
# functions defined in Part 1


def temp_in_fahrenheit(scale_out):
    """
    A function that asks the user to enter a temperature in Fahrenheit and converts it to the scale
    specified by scale_out (Celsius or Kelvin)
    @param scale_out: the scale to convert the temperature to
    """
    answer = input("Enter a temperature in Fahrenheit: ")
    t_fahrenheit = float(answer)
    if scale_out == "C":
        t = fahrenheit_to_celsius(t_fahrenheit)
        print("Celsius: %.2f" % t, "°C")  # print the result with 1 decimal place
    elif scale_out == "K":
        t = fahrenheit_to_kelvin(t_fahrenheit)
        print("Kelvin: %.2f" % t, "K")  # print the result with 1 decimal place
    else:
        print("Error. Fahrenheit can be converted into Celsius or Kelvin.")


def temp_in_celsius(scale_out):
    """
    A function that asks the user to enter a temperature in Celsius and converts it to the scale
    specified by scale_out (Fahrenheit or Kelvin)
    @ param scale_out: the scale to convert the temperature to
    """
    answer = input("Enter a temperature in Celsius: ")
    t_celsius = float(answer)
    if scale_out == "F":
        t = celsius_to_fahrenheit(t_celsius)
        print("Fahrenheit: %.2f" % t, "°F")  # print the result with 1 decimal place
    elif scale_out == "K":
        t = celsius_to_kelvin(t_celsius)
        print("Kelvin: %.2f" % t, "K")  # print the result with 1 decimal place
    else:
        print("Error. Celsius can be converted into Fahrenheit or Kelvin.")


def temp_in_kelvin(scale_out):
    """
    A function that asks the user to enter a temperature in Kelvin and converts it to the scale
    specified by scale_out (Celsius or Fahrenheit)
    @ param scale_out: the scale to convert the temperature to
    """
    answer = input("Enter a temperature in Kelvin: ")
    t_kelvin = float(answer)
    if scale_out == "C":
        t = kelvin_to_celsius(t_kelvin)
        print("Celsius: %.2f" % t, "°C")  # print the result with 1 decimal place
    elif scale_out == "F":
        t = kelvin_to_fahrenheit(t_kelvin)
        print("Fahrenheit: %.2f" % t, "°F")  # print the result with 1 decimal place
    else:
        print("Error. Kelvin can be converted into Celsius or Fahrenheit.")


# Part 3: Function to ask the user to select a temperature scale (Fahrenheit, Celsius, or Kelvin) and
# then convert the input value to the other scale using the functions defined in Part 2


def temp_converter():
    """"
    A function that asks the user to select a temperature scale (Fahrenheit or Celsius)
    and then converts the input value to the other scale
    """
    scale_in = input("Choose your current temperature scale. F for Fahrenheit, C for Celsius, and K for Kelvin: ")
    scale_in = scale_in.upper()  # convert to upper case to avoid case sensitivity

    scale_out = input("Choose the temperature scale you want to convert to. F, C, and K: ")
    scale_out = scale_out.upper()  # convert to upper case to avoid case sensitivity

    if scale_in == "F":  # if the user chooses F, call the function to convert the temperature that is in Fahrenheit
        temp_in_fahrenheit(scale_out)
    elif scale_in == "C":  # if the user chooses C, call the function to convert the temperature that is in Celsius
        temp_in_celsius(scale_out)
    elif scale_in == "K":  # if the user chooses K, call the function to convert the temperature that is in Kelvin
        temp_in_kelvin(scale_out)
    else:  # if the user enters an invalid input, print this message
        print("Invalid input")


# Part 4: Code to keep the program running until the user enters q (short for quit)

while True:
    temp_converter()  # call the function to ask the user to select a temperature scale and desired conversion
    quit_answer = input("To quit the program, press 'q'. To run again press enter:")
    quit_answer = quit_answer.upper()  # convert to upper case to avoid case sensitivity
    if quit_answer == "Q":
        print("Goodbye!")
        break  # break the loop to quit the program
