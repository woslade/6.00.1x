'''
Problem Set 1: Counting Vowels
'''

count = 0
vowels =  ['a', 'e', 'i', 'o', 'u']

for char in s:
    if char in vowels:
        count += 1
print 'Number of vowels: %s' %count
#####################################################################

'''
Problem Set 1: Count Bob's

Input
---
s = 'azcbobobegghakl'


Ouput
---
Number of times bob occurs is: 2
'''
count = 0
result = 0
while count <= len(s)-3:
    if s[count] == 'b' and s[count+1] == 'o' and s[count+2] == 'b':
        result += 1
        count += 1
    else:
        count += 1
     
print 'Number of times bob occurs is: %s' %result
#####################################################################
    
'''
Problem Set 1: Alphabetical substrings

Given a string s, return the substring with the longest stretch of letters in alphabetical order
'''
 
results = {}    
index = 0   
#s: string 

while index < len(s):
    num = 0
    done = False
    results[index] = []
    results[index].append(s[index])
    subset = s[index:]
    while not done:
        try:
            subset[num+1]
            if subset[num] < subset[num+1]:
                results[index].append(subset[num+1])
                num += 1
            else:
                done = True
        except IndexError:
            done = True    
    index += 1


tupleList = [(key, len(results[key])) for key in results.keys()] #create key:len tuples to map length of alphabetic strings
tupleList.sort(key=lambda x: x[1], reverse=True) #sort the list of tuples in descending order by the second value in the tuple

print "Longest substring in alphabetical order is: %r" %results[tupleList[0][0]] #the first item of tupleList, which is the tuple containing the key:value of the longest string.Then, the first item of the tuple, which is the key to the dict 

