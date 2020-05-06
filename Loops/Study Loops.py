# Just a little study guide for different loops

# How to itterate through a number
enum = 2468
string = "string"
list1 = [1,2,3,4]
#print(list1[-1])
for x in range(1, len(list1) - 1):
    print(x)

for i in enumerate(str(enum)):
    print(i)

for i, j in enumerate(str(enum)):
    print(i, j)

for x in range(1,5):
    print(x)

s1 = "string1"
s2 = "string2"
s3 = s1 + s2
print(s3)

word = "word"
wlist = list(word)
print(list(word))
print(word)

table = {}
li = [list(word), set(list(word)), word]

print(wlist.index('o'))
wlist.insert(wlist.index('r') + 1, 'l')
print(wlist)
print(li)

exDict = {'e': 1, 'a': 1, 't': 1}
listDict = [{'e':1,'a':1,'t':1}]

a = 'hcqopoei'
print(''.join(sorted(a)))

count = 13
print(count%2)
print(count//2)
count //= 2
print(count)

# simplifying if else stmts
rootleft = True

if rootleft:
    left = rootleft
else:
    left = 0
# is equivalent to
left = rootleft if rootleft else 0

llist = [[1,2],[0,1]]
for i in llist:
    print(i)