if __name__ == '__main__':
    # Read the integer n from input
    n = int(input())

    # Read n space-separated integers and convert them to a list of integers
    integer_list = list(map(int, input().split()))

    # Create a tuple from the list of integers
    t = tuple(integer_list)
    
    # Compute and print the hash value of the tuple
    print(hash(t))
