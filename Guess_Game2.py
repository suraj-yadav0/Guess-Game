# Lets Make a Guess Game Part 2


def guess():
    low = 1
    high = 100
    
    while(low <= high):
        mid = (low + high)//2
        target = input(f"Is {mid} your number? (yes/no): ")
        if target =="yes":
            print("Hooray! I guessed the number.")
            return
        elif target == "no":
            target = input(f"Is the number less than {mid}? (yes/no): ")
            if target == "yes":
                high = mid - 1
            else:
                low = mid + 1
                
                


guess()

