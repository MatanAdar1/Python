''' Exercise #3. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################
def sum_divisible_by_k(lst, k):
    
    s=0
    for i in range(len(lst)):
       if lst[i]%k==0:
           s+=lst[i]

    return (s)


#########################################
# Question 2 - do not delete this comment
#########################################
def mult_odd_digits(n):
    mul=1
    while n>0:
        if (n%10)%2==1:
           mul*= n%10
        n=n//10

    return (mul)



#########################################
# Question 3 - do not delete this comment
#########################################
def count_longest_repetition(s, c):

    cnt=0
    longestcnt=0
    for i in range(len(s)):
        if s[i]==c:
            cnt+=1
            
        else:
            if cnt>longestcnt:
                longestcnt=cnt
                cnt=0

    if cnt>longestcnt:
        longestcnt=cnt
        cnt=0
    
    return (longestcnt)



#########################################
# Question 4 - do not delete this comment
#########################################
def upper_strings(lst):
    if type(lst)!=list:
        return (-1)
    
    for i in range(len(lst)):
        if type(lst[i])==str:
            lst[i]=lst[i].upper()


#########################################
# Question 5 - do not delete this comment
#########################################
def div_mat_by_scalar(mat, alpha):

    matij=[]
    for i in range(len(mat)):
        mati=[]
        for j in range(len(mat[0])):
            mati.append(mat[i][j]//alpha)
        matij.append(mati)

    return (matij)



#########################################
# Question 6 - do not delete this comment
#########################################
def mat_transpose(mat):
    mattrans=[]
    for i in range(len(mat[0])):
        mati=[]
        for j in range(len(mat)):
            mati.append(mat[j][i])
        mattrans.append(mati)

    return (mattrans)



#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################
if __name__ == '__main__':  # Do not delete this line!
    print(sum_divisible_by_k([3, 6, 4, 10, 9], 3) == 18)
    print(sum_divisible_by_k([45.5, 60, 73, 48], 4) == 108)


    print(mult_odd_digits(5638) == 15)
    print(mult_odd_digits(2048) == 1)
    print(mult_odd_digits(54984127) == 315)


    print(count_longest_repetition('eabbaaaacccaaddd', 'a') == 4)
    print(count_longest_repetition ('cccccc','c') == 6)
    print(count_longest_repetition ('abcde', 'z') == 0)


    vals = [11, 'TeSt', 3.14, 'cAsE']
    upper_strings(vals)
    print(vals == [11, 'TEST', 3.14, 'CASE'])

    vals = [-5, None, True, [1, 'dont change me', 3]]
    upper_strings(vals)
    print(vals == [-5, None, True, [1, 'dont change me', 3]])

    print(upper_strings(42) == -1)
    print(upper_strings('im not a list') == -1)
    print(upper_strings(False) == -1)


    mat1 = [[2, 4], [6, 8]]
    mat2 = div_mat_by_scalar(mat1, 2)
    print(mat1 == [[2, 4], [6, 8]])
    print(mat2 == [[1, 2], [3, 4]])

    print(div_mat_by_scalar([[10,15], [-3,6]], -5) == [[-2, -3], [0, -2]])


    mat = [[1,2],[3,4],[5,6]]
    mat_T = mat_transpose(mat)
    print(mat == [[1, 2], [3, 4], [5, 6]])
    print(mat_T == [[1, 3, 5], [2, 4, 6]])

    mat2 = [[0, 1, 2], [10, 11, 12], [20, 21, 22]]
    mat2_T = mat_transpose(mat2)
    print(mat2_T == [[0, 10, 20], [1, 11, 21], [2, 12, 22]])

# ============================== END OF FILE =================================
