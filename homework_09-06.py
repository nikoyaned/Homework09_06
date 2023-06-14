#starts_with()

def starts_with(x,y) :
    
    if x[0] == y[0]:
        print ("true")
    else:
        print("false")

starts_with('abcdef','ghijk')








#ends_with():

def ends_with(x,y):
    if x [len(x)-1] == y [len(y)-1]:
        print ("true")
    else:
        print("false")
ends_with('abcd','efgh')









#swap_strings()

def swap_strings(x,y):
    
    c = str
    c = x
    x = y
    y = c
    print ( "first str" , x)
    print ("second str", y)
swap_strings("x","y")








#find_last_not_of()

def find_last_not_of(sequence, character):
    i = len(sequence) - 1
    while i >= 0:
        isEqual = False
        for z in character:
            if sequence[i] == z:
                isEqual = True
                break
        if isEqual == False:
            print(sequence[i])
            break
        else:
            i -= 1
        
            
find_last_not_of("abcdefghi", ['a', 'b', 'c'])








#convert_to_int()

def convert_to_int(x):
    s = x
    for i in s:
        print(i)

convert_to_int(b'sasdfg')









#rotate_by()

def rotate_by(numbers,count):
    while count != 0:
        x = numbers [count-1] 
        numbers [count-1] = numbers[len(numbers)-count]
        numbers[len(numbers)-count] = x
        count -= 1
    print(numbers)
        



rotate_by ([1,2,3,4,5,6,7,8,9,10],8)