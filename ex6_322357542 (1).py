''' Exercise #6. Python for Engineers.'''

######################################
# Question 1.a - do not delete this comment
#########################################


def four_bonacci_rec(n):
    if n<4:
        return (n)

    return (four_bonacci_rec(n-1)+four_bonacci_rec(n-2)+four_bonacci_rec(n-3)+four_bonacci_rec(n-4))



#########################################
# Question 1.b - do not delete this comment
#########################################
def four_bonacci_mem(n, memo=None):
    if n<4:
        return (n)
    if memo==None:
        memo={}
    if n not in memo:
        memo[n]=four_bonacci_rec(n-1)+four_bonacci_rec(n-2)+four_bonacci_rec(n-3)+four_bonacci_rec(n-4)

    return memo[n]


#########################################
# Question 2 - do not delete this comment
#########################################
def climb_combinations_memo(n, memo=None):
    if n<0:
        return (0)
    if n==0:
        return (1)

    if memo==None:
        memo={}
    if n not in memo:
        memo[n]=climb_combinations_memo(n-1)+climb_combinations_memo(n-2)

    return memo[n]




#########################################
# Question 3 - do not delete this comment
#########################################


def catalan_rec(n,memo=None):
    if n<=1:
        return 1



    if memo==None:
        memo={}

    
    if n not in memo:
        s=0
        for i in range(n):
                
            if i not in memo:
                if n-i-1 not in memo:
                    
                    s+=(catalan_rec(i)*catalan_rec(n-i-1))
                    
                else:
                    s+=(catalan_rec(i)*memo[n-i-1])
            else:
                s+=(memo[i]*catalan_rec(n-i-1))

        memo[n]=s
        
    return memo[n]


#Question 4.a - do not delete this comment
#########################################
def find_num_changes_rec(n, lst):
    if n<0:
        return 0
    if n==0:
        return 1
    else:
        if len(lst)==0:
            return 0 
    return find_num_changes_rec(n-lst[0], lst)+find_num_changes_rec(n, lst[1:])
    




#########################################
# Question 4.b - do not delete this comment
#########################################
def find_num_changes_mem(n, lst, memo=None):
    if n<0:
        return 0
    if n==0:
        return 1
    else:
        if len(lst)==0:
            return 0 
    
    if memo==None:
        memo={}
    if n not in memo:
        memo[(n,tuple(lst))]=find_num_changes_mem(n-lst[0], lst)+find_num_changes_mem(n, lst[1:])

    return memo[(n,tuple(lst))]




#########################################
# Question 5 - do not delete this comment
##########################################
def count_subseq(s, subseq, memo=None):

    if len(subseq)>len(s):

        return 0
    if len(subseq)==0:
        return 1
    else:
        if len(s)==0:
            return 0
            
    
        
    
    if memo==None:
        memo={}
    if subseq not in memo:
        if s[0]==subseq[0]:
            a=count_subseq(s[1:],subseq[1:])
            
        else:
            a=0
        memo[(s,subseq)]=a+count_subseq(s[1:],subseq)
    
    return memo[(s,subseq)]



#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################

if __name__ == "__main__":
    #Question 1.a tests - you can and should add more    
    
    print(four_bonacci_rec(0) == 0)
    print(four_bonacci_rec(5) == 12)
    print(four_bonacci_rec(8) == 85)
    
    #Question 1.b tests - you can and should add more
    
    print(four_bonacci_mem(0) == 0)
    print(four_bonacci_mem(5) == 12)
    print(four_bonacci_mem(8) == 85)
    
    #Question 2 tests - you can and should add more
    
    print(climb_combinations_memo(7) == 21)

    
    #Question 3 tests - you can and should add more
    
    cat_list = [1,1,2,5,14,42,132,429]
    for n,res in enumerate(cat_list):
        print(catalan_rec(n) == res)
    
    #Question 4.a tests - you can and should add more
    
    print(find_num_changes_rec(5,[1,2,5,6]) == 4)
    print(find_num_changes_rec(4,[1,2,5,6]) == 3)
    print(find_num_changes_rec(0,[1,2,5,6]) == 1)
    print(find_num_changes_rec(105,[1,105,999,100]) ==3)
    
    #Question 4.b tests - you can and should add more
    
    print(find_num_changes_mem(5,[1,2,5,6]) == 4)
    print(find_num_changes_mem(4,[1,2,5,6]) == 3)
    print(find_num_changes_mem(105,[1,105,999,100]) ==3)
    
    #Question 5 tests - you can and should add more
    
    print(count_subseq("0010", "01") == 2)
    print(count_subseq("ABBABBABBABBA", "AB") == 20)
    print(count_subseq("PyCharm", "Charm") == 1)
    print(count_subseq("PyCharm", "PY") == 0)
    print(count_subseq("Cool", "") == 1)
    
    
# ============================== END OF FILE =================================
