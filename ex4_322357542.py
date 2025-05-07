''' Exercise #4. Python for Engineers.'''



#########################################
# Question 1 - do not delete this comment
#########################################

def most_popular_characters(my_string):

    d={}
    for x in my_string:

        count = d.get(x, 0)
        count += 1
        d[x] = count

    m=max(d.values())
    

    lex='z'
    for p in d:
        if d[p]==m:
            if p<lex:
                lex=p
    
    return (lex)
    


#########################################
# Question 2 - do not delete this comment
#########################################

def diff_sparse_matrices(lst):

    d2=lst[0]

    for i in range(1,len(lst)):

        for j in lst[i]:
            
            z = d2.get(j, 0)
            z=z-lst[i][j]
            if z==0:
                del d2[j]
            else:
                d2[j] = z
        

        return (d2)


#########################################
# Question 3 - do not delete this comment
#########################################
def find_substring_locations(s, k):

    d3={}
    for i in range(len(s)-k+1):
        
        l = d3.get(s[i:i+k], [])
        l.append(i)
        d3[s[i:i+k]] = l

    
    return (d3)



#########################################
# Question 4 - do not delete this comment
#########################################
def courses_per_student(tuples_lst):

    d4={}

    for i in range(len(tuples_lst)):

        low0=tuples_lst[i][0]
        low1=tuples_lst[i][1]
        z = d4.get(low0.lower(), [])
        z.append(low1.lower())
        d4[low0.lower()] = z
        

    return (d4)


def num_courses_per_student(stud_dict):

    for k in stud_dict:

        stud_dict[k]=len(stud_dict[k])


#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################

if __name__ == '__main__': #Do not delete this line!
	# Q1
	print(most_popular_characters('gggcccbb') == 'c')

	# Q2
	print(diff_sparse_matrices([{(1, 3): 2, (2, 7): 1}, {(1, 3): 6}]) == {(1, 3): -4, (2, 7): 1})
		
	# Q3
	print(find_substring_locations('TTAATTAGGGGCGC', 2) == {'TT': [0, 4], 'TA': [1, 5], 'AA': [2], 'AT': [3], 'AG': [6], 'GG': [7, 8, 9], 'GC': [10, 12], 'CG': [11]})

	# Q4
	stud_dict = courses_per_student([('Tom', 'Math'), ('Oxana', 'Chemistry'), ('Scoobydoo', 'python'), ('Tom', 'pYthon'), ('Oxana', 'biology')])
		
	print(stud_dict == {'tom': ['math', 'python'], 'oxana': ['chemistry', 'biology'], 'scoobydoo': ['python']})
		
	num_courses_per_student(stud_dict)
	print(stud_dict == {'tom': 2, 'oxana': 2, 'scoobydoo': 1})


# ============================== END OF FILE =================================

