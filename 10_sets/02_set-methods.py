'''
• Set Methods
• Sets in python work more or less the sameway as sets in mathematics
• We can perform operations like union and intersection on the sets just like sets in mathematics

• union()
• update()
• intersection()
• intersection_update()
• difference()
• difference_update()
• symmectric_difference()
• symmetric_difference_update()
• isdisjoint()
• issuperset()
• issubset()
• add()
• remove()
• discard()
• pop()
• copy()
• clear()
'''

'''
• union()
• A ∪ B
• union of two sets (group all unique items)
• returns a new set
'''
s1 = {'apple', 'banana', 'mango'}
s2 = {'apple', 'guava', 'mango'}

s3 = s1.union(s2)
print(s3)  # {'guava', 'banana', 'apple', 'mango'}
print(s1)  # {'banana', 'apple', 'mango'}


'''
• update()
• union of two sets
• updates the original set
'''
s1 = {'apple', 'banana', 'mango'}
s2 = {'apple', 'guava', 'mango'}

s3 = s1.update(s2)
print(s3)  # None
print(s1)  # {'guava', 'banana', 'apple', 'mango'}


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• intersection()
• A ∩ B
• intersection of two sets (group similar items only)
• returns a new set
'''
s1 = {'apple', 'banana', 'mango'}
s2 = {'apple', 'guava', 'mango'}

s3 = s1.intersection(s2)
print(s3)  # {'mango', 'apple'}
print(s1)  # {'mango', 'apple', 'banana'}


'''
• intersection_update()
• intersection of two sets (group similar items only)
• updates the original set
'''
s1 = {'apple', 'banana', 'mango'}
s2 = {'apple', 'guava', 'mango'}

s3 = s1.intersection_update(s2)
print(s3)  # None
print(s1)  # {'apple', 'mango'}


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• difference()
• {A - B}
• returns a new set
'''
s1 = {'apple', 'banana', 'mango'}
s2 = {'apple', 'guava', 'mango'}

s3 = s1.difference(s2)
print(s3)  # {'banana'}
print(s1)  # {'banana', 'mango', 'apple'}


'''
• difference_update()
• {A - B}
• updates the original set
'''
s1 = {'apple', 'banana', 'mango'}
s2 = {'apple', 'guava', 'mango'}

s3 = s1.difference_update(s2)
print(s3)  # None
print(s1)  # {'banana'}


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• symmectric_difference()
• {(A ∪ B) - (A ∩ B)} or {(A - B) ∪ (B - A)}
• returns a new set
'''
s1 = {'apple', 'banana', 'mango'}
s2 = {'apple', 'guava', 'mango'}

s3 = s1.symmetric_difference(s2)
print(s3)  # {'banana', 'guava'}
print(s1)  # {'apple', 'mango'}


'''
• symmetric_difference_update()
• updates the original set
'''
s1 = {'apple', 'banana', 'mango'}
s2 = {'apple', 'guava', 'mango'}

s3 = s1.symmetric_difference_update(s2)
print(s3)  # None
print(s1)  # {'banana', 'guava'}


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• isdisjoint()
• returns true if sets have no common item, false if contain common item
'''
s1 = {'F-35 Lightning II', 'F-22 Raptor', 'F Super Hornet', 'F-15 Eagle'}
s2 = {'Lamborghini Centenario', 'Koenigsegg One:1', 'Bugatti Chiron', 'McLaren Senna'}

s3 = s1.isdisjoint(s2)
print(s3)  # True


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• issuperset()
• returns true if set is a superset, false if not a supeprset
'''
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2}
s3 = {1, 6}

print(s1.issuperset(s2))  # True
print(s1.issuperset(s3))  # False


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• issubset()
• returns true if set is a subset, false if not a subset
'''
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2}
s3 = {1, 6}

print(s2.issubset(s1))  # True
print(s3.issubset(s1))  # False


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• add()
• add an element in the set
'''
s1 = {1, 2, 3, 4, 5}

s1.add(33)
print(s1)  # {1, 2, 3, 4, 5, 33}


print('-------------------------------------------------------------------------------------------------------------------------')

'''
• remove()
• remove raise an error if element to be removed not in set
'''
s1 = {1, 2, 3, 4, 5}

s1.remove(3)
print(s1)  # {1, 2, 4, 5}

# s1.remove(33) # KeyError: 33


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• discard()
• discard does not raise error if item not present in set
'''
s1 = {1, 2, 3, 4, 5}

s1.discard(33)
print(s1)  # {1, 2, 3, 4, 5}

s1.discard(3)
print(s1)  # {1, 2, 4, 5}


print('-------------------------------------------------------------------------------------------------------------------------')

'''
• pop()
• removes the last element from the set, but we dont know which is the last element as sets are unordered
'''
s1 = {1, 2, 3, 4, 5}

pop = s1.pop()
print(s1)  # {2, 3, 4, 5}
print(pop)  # 1


print('-------------------------------------------------------------------------------------------------------------------------')

'''
• copy()
• returns a shallow copy of the set
'''
s1 = {1, 2, 3, 4, 5}

s2 = s1.copy()

print(s1, id(s1))  # {1, 2, 3, 4, 5} 1929203424320
print(s2, id(s2))  # {1, 2, 3, 4, 5} 1929203424768


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• clear()
• empties the set
'''
s1 = {'hello', 'world'}

s1.clear()
print(s1)  # set()


print('-------------------------------------------------------------------------------------------------------------------------')
