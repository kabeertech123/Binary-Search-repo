import math
def BinarySearch():
    arr = [ 1, 5, 7, 99, 105, 109, 604, 1011, 9999]
    first_pos = 0
    last_pos = len(arr) - 1 # the len is 8 because an arr always starts at 0 
    print(last_pos)
    user_input = int(input('Enter a number you are trying to find: '))
    loop = True
    counter = 0
    
    while(loop):
       
        half_pos =  math.floor((first_pos + last_pos) / 2)
        
        if arr[half_pos] == user_input:
            print(f'the number {user_input} was in position: {half_pos}')
            ans = True
            break
        
        elif counter > len(arr): # i have to put the stopping condtion above the other elifs becuase if one elif is true, then it will return to the first if statement 
            print(f'{user_input} is not in the arr') 
            loop = False
            
        
        elif(arr[half_pos] < user_input):
            first_pos = half_pos + 1
            print(f'first pos: {first_pos}')
            print(f'last pos: {last_pos}')
            counter += 1
            
        elif(arr[half_pos] > user_input):
            last_pos = half_pos - 1
            print(f'first pos: {first_pos} ')
            print(f'last pos: {last_pos} ')
            counter += 1  

BinarySearch()