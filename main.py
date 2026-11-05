import math
def BinarySearch():
    arr = [ 1, 5, 7, 99, 105, 109, 604, 1011, 9999]
    user_input = int(input('Enter a number you are trying to find: '))
    loop = True
    first_pos = 0
    last_pos = len(arr) - 1
    print(last_pos)
    
    while(loop):
        half_pos =  math.floor((first_pos + last_pos) / 2)
        
        if arr[half_pos] == user_input:
            print(f'the number {user_input} was in position: {half_pos}')
            loop = False
        
        elif(arr[half_pos] < user_input):
            last_pos = half_pos - 1
            print(f'first pos: {first_pos}')
            print(f'last pos: {last_pos}')
            
        elif(arr[half_pos] > user_input):
            first_pos = half_pos + 1
            print(f'first pos: {first_pos} ')
            print(f'last pos: {last_pos} ')
            
    
    print(f'{user_input} does not exist in the arr')
    
    
            
BinarySearch()