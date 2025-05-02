from list import friends #this when we want to import somting from our files
from list import lucky_numbers
friends.extend(lucky_numbers)#this add two list together
print(friends)
friends.append("mgsa2")#this will add another element to the list
print(friends)
friends.insert(0,"mgsa")#this take two parameter the 1st one is the index and the other is the elemnt
print(friends)
friends.remove("mgsa")
#friends.clear()#make it empty list
friends.pop()#this remove the last element in the list
print(friends)
print(friends.index("filo"))#this will tell me the index of element
friends.count("filo")#this will tell us how many time flio appear in the list
friends.sort()#in strlink alpha order in number sort it from low to max
lucky_numbers.reverse()#this will reverse the list element
friends_copy=friends.copy()#this make the list have the same element
