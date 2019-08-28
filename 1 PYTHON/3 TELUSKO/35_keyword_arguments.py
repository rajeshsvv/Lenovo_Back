# def person(name,*data):
#
#     print(name)
#     print(data)
#
#
# person("Navin",28,"Mumbai",8151958650)


def person(name,**data):

    print(name)
    # print(data)

    for i,j in data.items():
        print(i,j)

person("Navin",age=28,city="Mumbai",mob=8151958650)