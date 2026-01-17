ratings = [1,2,3,4,5,6,7,8,0]

print(ratings)

print(ratings[5])

states = [ 'Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming' ] 

print(states[5])

x = 6
x > 10
print(x)
b = x + 1
print(b)

    
    
city = ['lagos','imo','abia','kano','ogun','osun']
print('cities loop:')

for x in city:
    print('city:' + x)
    
print('\n')

num = [1,2,3,4,5,6,7,8,9,0]

print('x^2 loop:')

for x in num:
    y = x * x

print(str(x) + '*' + str(x) + '=' + str(y))


x = 3
if x < 10:
    print('x below 10')
    


#!/usr/bin/env python3

     
print('2018')

f = x * y
f = (3,4)

print(f)


list2 = [1,3,4,6,4,7,8,2,3]
print(sum(list2))
print(min(list2))
print(max(list2))
print(list2[-1])

ratings = [ 'A','A','B','A','C','A' ]
print(ratings)

x = [3,4,5]
x.append(6)
print(x)
x.append(7)
print(x)
x.pop()
x.pop()
x.pop()
print(x)

x = [3,4,5]
print(x[-1])
print(x[1])

x = [3,6,21,1,5,98,76,50,15,4,24,74,1,6]
x.sort()
x = list(reversed(x))
print(x)

words = ["Be","Car","Always","Door","Eat"]
words.sort()
words = words[::-1]
print(words)


elementx = [(3,6),(4,7),(5,9),(8,4),(3,1)]
elementx.sort()
elementx = elementx[::-1]
print(elementx)
print(elementx[3])

x = list(range(1,51))
print(x)

for i in range(1,12):
    print(i)
    

for i in range(0,25,5):
    print(i)
    
    
x = list(range(1,1001))

print(x)
print(min(x))
print(max(x))


#!/usr/bin/python

words = {}
words["BMP"] = "Bitmap"
words["BTW"] = "By The Way"
words["BRB"] = "Be Right Back"

print(words["BMP"])
print(words["BRB"])
print(words["BTW"])
