# Tutki, miten voit printata teht.18 kaupungit print-metodilla ilman rivinvaihtoa.
# Entä miten lisäät välilyönnin kaupunkien väliin?
# Eng: Find out how you can print prob.18 cities with the print method without line breaks.
# And how do you add a space between cities?

# Solution

list = ["Helsinki", "Stockholm", "Oslo"]
for city in list:
    print(city, end=" ")
