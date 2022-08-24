# slicing = create a substring by extracting elements from another string
#       indexing[] or slice ()
#       [start:stop:step]

#name = "Matt Code"

#first_name = name[0:3]  # first index is inclusive the last is exclusive!
#first_name = name[:3]     # a short way of writing this
#last_name = name[5:]
#funky_name = name [0:8:1] # this one jumps a letter, the 1 will jump every one
#reversed_name = name[::-1]

#print(first_name)
#print(last_name)
#print(funky_name)
#print(reversed_name)


#SLICE FUNCTION

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])