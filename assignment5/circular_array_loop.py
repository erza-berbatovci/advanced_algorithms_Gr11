def circularArrayLoop(nums):
    n = len(nums)

    def next_index(i):
        return (i + nums[i]) % n  # wrap around

    for i in range(n):
        if nums[i] == 0:
            continue
        
        # slow and fast pointers
        slow, fast = i, i
        direction = nums[i] > 0  # True for positive, False for negative
        
        while True:
            # Move slow pointer once
            next_slow = next_index(slow)
            # Move fast pointer twice
            next_fast = next_index(fast)
            next_fast = next_index(next_fast)

            # Check direction consistency and non-zero
            if (nums[next_slow] > 0) != direction or (nums[next_fast] > 0) != direction:
                break
            if nums[next_slow] == 0 or nums[next_fast] == 0:
                break

            # Check if cycle is found
            if next_slow == next_fast:
                if next_slow == next_index(next_slow):  # cycle of length 1
                    break
                return True
            
            slow, fast = next_slow, next_fast

        # Mark all visited nodes as 0 to avoid reprocessing
        j = i
        while nums[j] != 0 and (nums[j] > 0) == direction:
            nxt = next_index(j)
            nums[j] = 0
            j = nxt

    return False

# Test examples
print(circularArrayLoop([2,-1,1,2,2]))  # True
print(circularArrayLoop([-1,-2,-3,-4,-5,6]))  # False
print(circularArrayLoop([1,-1,5,1,4]))  # True
#todo assignment 815