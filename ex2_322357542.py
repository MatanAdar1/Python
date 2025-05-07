""" Exercise #2. Python for Engineers."""


#########################################
# Question 1 - do not delete this comment
#########################################

a = 5
lst = [2,3,5,10,6]

index=-1

for i in range(len(lst)):
    if lst[i]%a==0:
        index=i
        break
    
print (index)


#########################################
# Question 2 - do not delete this comment
#########################################
lst2 = ['hi', 'my', 'name', 'is', 'matan','adar']
# Replace the assignment with other lists of strings (str) to test your code.


# Write the code for question 2 using a for loop below here.
s1=0
for i in range(len(lst2)):
    s1+=len(lst2[i]) 
    
avg1=s1/len(lst2)
cntt1=0
for i in range(len(lst2)):
    if len(lst2[i])<avg1:
        cntt1+=1

print("The number of strings shorter than the average is:",cntt1)
# Write the code for question 2 using a while loop below here.
s2=0
i=0
while i<len(lst2):
    s2+=len(lst2[i]) 
    i+=1
avg2=s2/len(lst2)
cntt2=0
i=0
while i<len(lst2):
    
    if len(lst2[i])<avg2:
        cntt2+=1
    i+=1
print("The number of strings shorter than the average is:",cntt2)


# End of code for question 2



#########################################
# Question 3 - do not delete this comment
#########################################

lst3 = [2, 4, 5, 1, 7]

# Write the rest of the code for question 3 below here.
mul=1
if len(lst3)!=1:
    for i in range(len(lst3)-1):
        mul*=lst3[i]+lst3[i+1]    

    print (mul)
else:
    print(lst3[0])

# End of code for question 3

#########################################
# Question 4 - do not delete this comment
#########################################

lst4 = [2,5,10,13,22]  # Replace the assignment with other lists to test your code.

# Write the rest of the code for question 4 below here.
gap=0

lstg=[lst4[0]]



for i in range(1,len(lst4)):
    if abs(lst4[i]-lstg[-1])>gap:

        gap=abs(lst4[i]-lstg[-1])
        lstg.append(lst4[i])
        
print(lstg)

# End of code for question 4



#########################################
# Question 5 - do not delete this comment
#########################################

my_string = 'manakkkkahhhhaa'  # Replace the assignment with other strings to test your code.
k = 4  # Replace the assignment with a positive integer to test your code.

# Write the rest of the code for question 5 below here.

cnt=1
sidra=''
if len(my_string)==0:
    print ("Didn't find a substring of length", k)
elif len(my_string)==1:
    if k==1:
        print ("For length "+str(k)+", found the substring "+my_string+"!")
    else:
        print("Didn't find a substring of length", k)        
else:
    
    for i in range(1,len(my_string)):
        
        if my_string[i]==my_string[i-1]:
            cnt+=1
        else:
            cnt=1

        if cnt==k:
            
            sidra=my_string[i]*k
            print("For length "+str(k)+", found the substring "+sidra+"!")
            break
        
    if sidra=='':
        print ("Didn't find a substring of length", k)

# End of code for question 5
