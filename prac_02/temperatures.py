"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""
from prac_01.temperatures import fahrenheit, celsius

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            fahrenheit = (float(input("Celsius: ")))
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            celsius = f_to_c(float(input("Fahrenheit: ")))
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you.")

    return
def c_to_f(c):
    f = c * 9.0 / 6 + 32
    return f

def f_to_c(f):
    c = 5 / 9 * (f - 32)
    return c

main()