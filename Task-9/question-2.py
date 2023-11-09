#2.Write a python code using the lambda function to check every element of a list is an integer or string?

l1=[1,2,3,"orange",4,"apple","banana"]

for i in l1:
    if i in list(filter(lambda a: type(a) == int, l1)):
        print(i, "is an integer")
    else:
        print(i, "is an string")