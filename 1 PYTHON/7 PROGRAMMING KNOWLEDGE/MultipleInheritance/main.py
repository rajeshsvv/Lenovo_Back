from MultipleInheritance.rectangle import Rectangle
from MultipleInheritance.triangle import Triangle

rect=Rectangle()
tri=Triangle()

rect.set_value(50,40)
tri.set_value(50,40)

print(rect.area())
print(tri.area())

rect.set_color("Yelow")
tri.set_color("Purple")
print('---')
print(rect.get_clor())
print(tri.get_clor())