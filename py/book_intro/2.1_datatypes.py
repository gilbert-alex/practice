''' Working with Numbers, Text and Dates
    Example programs for basic data types in Py
'''

# fig 1-3
# Built in functions for Numbers
pi = 3.14159265358979
x = 128
y = 345.67890987
z = -999.9999

print("Fig 1-3")
print(abs(z))
print(int(z))
print(int(abs(z)))
print(round(pi,4))
print(bin(x))
print(hex(x))
print(oct(x))
print(max(pi,x,y,z))
print(min(pi,x,y,z))
print(type(pi))
print(type(x))
print(type(str(y)))

# fig 1-8
# format strings saved to variables
sales_tax_rate = 0.065
sample1 = f'Sales Tax Rate {sales_tax_rate:.2%}'
sample2 = f"Sales Tax Rate {sales_tax_rate:.2%}"
sample3 = f"""Sales Tax Rate {sales_tax_rate:.2%}"""
sample4 = f'''Sales Tax Rate {sales_tax_rate:.2%}'''

print("Fig 1-8")
print(sample1)
print(sample2)
print(sample3)
print(sample4)

# fig 1-9
# multi line format string saved to a variable
unit_price = 49.95
quantity = 32
sales_tax_rate = 0.065
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax
output=f"""
Subtotal:   ${subtotal:,.2f}
Sales Tax:  ${sales_tax:,.2f}
Total:      ${total:,.2f}
"""
print("Fig 1-9")
print(output)

# fig 1-10
# multi line format string with width aligned
unit_price = 49.95
quantity = 32
sales_tax_rate = 0.065
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax
output=f"""
Subtotal:   ${subtotal:>9,.2f}
Sales Tax:  ${sales_tax:>9,.2f}
Total:      ${total:>9,.2f}
"""
print("Fig 1-10")
print(output)

# fig 1-11
# multi line format string with '$' aligned with number
# (use of string data type)
unit_price = 49.95
quantity = 32
sales_tax_rate = 0.065
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax

# Format amounts to show as string with leading dollar sign
s_subtotal = "$" + f"{subtotal:,.2f}"
s_sales_tax = "$" + f"{sales_tax:,.2f}"
s_total = "$" + f"{total:,.2f}"

# Output the string with dollar sign already attached
output = f"""
Subtotal:   {s_subtotal:>9}
Sales Tax:  {s_sales_tax:>9}
Subtotal:   {s_total:>9}
"""
print('Fig 1-11')
print(output)

# Fig 1-14
# Examples of string operators
s = "Abracadabra Hocus Pocus you're a turtle dove"
# is there a t in s?
print("Fig 1-14")
print("t" in s)
# is there a T in s?
print("T" in s)
# is there no T in s?
print("T" not in s)
# print 15 hyphens
print("-" * 15)  
# print first character in string s
print(s[0])
#print characters 33 - 39 from string x
print(s[33:39])
# print every third character from string x starting at 0
print(s[0:44:3])
# print lowers character in s (string is lowest)
print(min(s))
# print highest character in s
print(max(s))
# where is the first uppercase P?
print(s.index("P"))
# where is the first lowercase O in the latter half of string s
print(s.index("o",22,44))
# how many lowercase letters a are in string s
print(s.count("a"))

# returning ASCII values
print()
print(ord("A"))
print(ord("a"))
print(chr(65))
print(chr(97))
print()

# Fig 1-16
# string functions
s1 = "There is no such word as schmeedledorp."
s2 = "    a b c    "
s3 = "ABC"
print("Fig 1-16")
# capitalize the first letter and the rest lowercase
print(s3.capitalize())
# count the number of spaces in s1
print(s1.count(" "))
# find the dot in s1
print(s1.find("."))
# is s2 all lowercase letters?
print(s2.islower())
# convert s3 to all lowercase
print(s3.lower())
# strip leading characters from s2
print(s2.lstrip())
# strip leading and trailing characters from s2
print(s2.strip())
# swap the case of letters in s1
print(s1.swapcase())
# show s1 in title case
print(s1.title())
# show s1 uppercase
print(s1.upper())