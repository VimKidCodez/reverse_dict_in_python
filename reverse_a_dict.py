# Write a program to reverse a dict in pyhton 

#inialiize a dict

dict_a = {"Q":"A"}
print(dict_a) 

# navigate to a position
for i in dict_a:
    print(i)

# navigate to antother position
for i in dict_a:
    print(dict_a[i])


#now lets reverse the dict and print in the another way
for i in dict_a:
    print(dict_a[i],":",i)

#now lets print it in an dict form
for i in dict_a:
    dict_b = {dict_a[i]:i}
    print(dict_b)


