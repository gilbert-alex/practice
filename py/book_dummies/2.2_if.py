# modules
import datetime as dt

# if statement
print("\nIf Statement:")
total = 100
sales_tax_rate = 0.065
taxable = True
if taxable:
    print(f"Subtotal : ${total:.2f}")
    sales_tax = total * sales_tax_rate
    print(f"Sales Tax: ${sales_tax:.2f}")
    total = total + sales_tax
print(f"Total   : ${total:.2f}")

# else statement
print("\nElse Statement:")
now = dt.datetime.now()
if now.hour > 12:
    print("good morning")
else:
    print("good afternoon")
print("I hope you are doing well")

# elif statement
print("\nElif Statement:")
light_color = "yellow"
if light_color == "green":
    print("Go")
elif light_color == "red":
    print("Stop")
else:
    print("Proceed with caution")
print("This code executes no matter what")

