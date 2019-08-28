# sets 
are unorder list of items and no duplicates in it means it throws the duplicate values and in output it gives unique values k
#strange when we execute each time set its output order will be change strnage right

cs_courses={"History","Math","Physics","ComputerScience"}
print(cs_courses)

cs_courses={"History","Math","Physics","ComputerScience","ComputerScience","Physics"}
print(cs_courses)
print("Math" in cs_courses)	;	print("Path" in cs_courses);

cs_courses={"History","Math","Physics","ComputerScience"}
art_courses={"History","Math","Art","Design"}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))
