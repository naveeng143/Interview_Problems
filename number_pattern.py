"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""

def num_pattern(n):
    num = 1

    for i in range(0, n):

        num = 1

        for j in range(0, i + 1):
            print(num, end=" ")
            num += 1
        print("\r")


num_pattern(5)
