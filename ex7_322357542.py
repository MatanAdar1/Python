''' Exercise #5. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################
def rixum(file_name):
    infile= open (file_name, 'r')

    st=infile.read()
    
    
    lst=st.split()

    
    s=0

    for i in lst:
        for j in range(len(i)):
            if i[j:].isdigit():
                s+=int(i[j:])
                break
    


    infile.close()
    return (s)





#########################################
# Question 2 - do not delete this comment
#########################################
def rickounter(f_document, f_rick_identifiers):
    infile1= open (f_document, 'r')
    infile2= open (f_rick_identifiers, 'r')

    lstd=[]
    lsti=[]
    
    for line1 in infile1:
        lstd+=line1.split()

    for line2 in infile2:
        lsti+=line2.split()

    d={}
    for i in lsti:
        d[i]=0

    for j in lstd:
        for i in lsti:
            if i in j:
                for z in range(len(j)):
                    if i in j[z:]:
                        d[i]=d[i]+1

    
    return (d)

    infile1.close()
    infile2.close()

#########################################
# Question 3 - do not delete this comment
#########################################
def twin_pricks(num, out_file_name):

    outfile=open(out_file_name, 'w')
    if num > 0:
        
    
        outfile.write(str(3)+","+str(5))

    num=num-1
    n=7
    flag=True
    p1=5
    p2=5
    while num > 0:
        
        for i in range(2, int(n**0.5)+1):
            
            if (n % i) == 0:
                flag=False
                break
        if flag:
            p2=n
            
            if p2-p1==2:
                a='\n'+str(p1)+","+str(p2)
                outfile.write(a)
                num=num-1

        p1=p2
        flag=True
        n=n+1
        
    outfile.close()
    

#########################################
# Question 4 - do not delete this comment
#########################################
def rickode(in_file):
    infile= open (in_file, 'r')

    st=infile.read()
    decstr=""
    decchar=''
    for i in range(len(st)):
        decchar=st[i]
        if st[i].isalpha():
            
            if ord(st[i])>90:
                if ord(st[i])==121:
                    decchar='a'
                elif ord(st[i])==122:
                    decchar='b'
                else:
                    decchar=chr(ord(st[i])+2)
            else:
                if ord(st[i])==89:
                    decchar='A'
                elif ord(st[i])==90:
                    decchar='B'
                else:
                    decchar=chr(ord(st[i])+2)

    
        decstr=decstr+decchar
    
                
    for x in range(len(in_file)):
        if in_file[len(in_file)-1-x]==".":
            break
    out=in_file[:len(in_file)-1-x]+"_decipherick.txt"

    outfile=open(out, 'w')

    outfile.write(decstr)


    infile.close()
    outfile.close()

    
    return (out)

#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    NO_EXC_MSG="Exception must be raised for this input (NOT pass)."
    WRONG_EXC_MSG="Wrong message in raised exception (NOT pass). \nExpected: {}\nGot: {}\n"
    NOT_PASS_MSG="Unexpected result (NOT pass.)"

    PASS_MSG="Got expected results (pass)."
    EXPECTED_EXC_MSG="Got corrent error and error message (pass)."
    

    print('==== Q1: Basic tests/output====')
    q1_input_file_name = "q1_input_1.txt"
    expected_result=137
    actual_result=rixum(q1_input_file_name)
    print("q1t1:", f'{PASS_MSG if expected_result==actual_result else NOT_PASS_MSG}')
    print("TBD: It is recommended to write here more tests of your own")
    
    print('==== Q2: Basic tests/output====')
    expected_result={'Hello_word9': 0, 'CoolRick11': 1, 'C-137': 2, 'c-132': 1, 'Z0Zo0': 1, 'TestMeRick123': 1}
    actual_result=rickounter("q2_f_document_1.txt", "q2_f_rick_identifiers_1.txt")
    print("q2t1", f"{(PASS_MSG if expected_result==actual_result else NOT_PASS_MSG)}")
    if expected_result!=actual_result:
        print(f'Expected: {expected_result}')
        print(f'Got: {actual_result}')

    print('==== Q3: Basic tests/output====')
    twin_pricks(4, "q3_output_1_res.txt")
    expected_result=open('q3_output_1_sol.txt', 'r').read()
    actual_result=open('q3_output_1_res.txt', 'r').read()
    print("q3t1", f"{(PASS_MSG if expected_result==actual_result else NOT_PASS_MSG)}")
    if expected_result!=actual_result:
        print(f'Expected: \n{expected_result}')
        print(f'Got: \n{actual_result}')
        
    twin_pricks(20, "q3_output_2_res.txt")
    expected_result=open('q3_output_2_sol.txt', 'r').read()
    actual_result=open('q3_output_2_res.txt', 'r').read()
    print("q3t2", f"{(PASS_MSG if expected_result==actual_result else NOT_PASS_MSG)}")
    if expected_result!=actual_result:
        print(f'Expected: \n{expected_result}')
        print(f'Got: \n{actual_result}')

    print('==== Q4: Basic tests/output====')
    q4_input_file_name = "q4_input_1.txt"
    deciphered_text="There's a lesson here, and I'm not going to be the one to figure it out\n\nAnd...\n\nThere'Z a lesson here, and I'm not going to be the one to figure it out!!"
    with open(rickode(q4_input_file_name),'r') as f:
        print(f'{PASS_MSG if f.read() == deciphered_text else NOT_PASS_MSG}')



   

# ============================== END OF FILE =================================
