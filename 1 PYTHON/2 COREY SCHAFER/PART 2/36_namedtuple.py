# namedtuple is lightweight object same as tuple but it as more readable format got it
from collections import namedtuple


# tuple
# colors = (55, 125, 255)
# print(colors[2])

# dictionary
# colors = {"red": 55, "blue": 125, "green": 255}
# print(colors["red"])


# named tuple
Color = namedtuple("Color", ["red", "green", "blue"])
#color = Color(55, 155, 255)
color = Color(red=55, green=155, blue=255)
print(color[0])  # both ways we can print the value
print(color.green)
