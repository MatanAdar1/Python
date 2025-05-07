''' Exercise #1 '''

#########################################
# Question 1 - do not delete this comment
#########################################
S = 50.0
AB = 10
BC = 15
AD = 8
DC = 8
# Write the rest of the code for question 1 below here.

print("Perimeter is:",AB+BC+AD+DC)
EF=(AB+DC)/2
print("Midsegment is:",EF)
print("Height is:",S/EF)

#########################################
# Question 2 - do not delete this comment
#########################################
my_name = 'matan'
# Write the rest of the code for question 2 below here.
print("Hello",my_name[0].upper()+ my_name[1:],":)")



#########################################
# Question 3 - do not delete this comment
#########################################
number  = '49'
# Write the rest of the code for question 3 below here.


if int(number)%7==0:
    print("I am",number,"and I am divisible by 7")

else:
    print("I am",number,"and I am not divisible by 7")    




#########################################
# Question 4 - do not delete this comment
#########################################
text = 'matan'
copies = 4
# Write the rest of the code for question 4 below here.
str1=text[1::2]
str2=text[0::2]
print((str1+str2)*copies)




#########################################
# Question 5 - do not delete this comment
#########################################
name = 'droLtromedloV'
q = 4
# Write the rest of the code for question 5 below here.
sub1=''
sub2=''

if q<0 or q>=len(name) or name=='':
    print("Error: illegal input!")

else:
    sub1=name[:q]
    sub2=name[q:]

    sub1=sub1[::-1]
    sub2=sub2[::-1]

    print(sub1+' '+sub2)


