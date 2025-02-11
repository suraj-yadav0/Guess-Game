# Lets Make a Guess Game Part 2


def guess():
    low = 1
    high = 100
    count = 1
    
    while(low <= high):
        mid = (low + high)//2
        target = input(f"Is {mid} your number? (yes/no): ")
        if target =="yes":
            print("Hooray! I guessed the number in ", count, "attempts")
            return
        elif target == "no":
            count += 1
            
            target = input(f"Is the number less than {mid}? (yes/no): ")
            if target == "yes":
                high = mid - 1
            else:
                low = mid + 1
                
                


guess()

