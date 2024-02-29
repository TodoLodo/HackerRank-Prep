def insert(arr, index, value):
    arr.insert(index, value)

def remove(arr, value):
    arr.remove(value)

def append(arr, value):
    arr.append(value)

def sort(arr):
    arr.sort()

def pop(arr):
    arr.pop()

def reverse(arr):
    arr.reverse()

def print_arr(arr):
    print(arr)

if __name__ == '__main__':
    N = int(input())
    arr = []
    command_map = {
        'insert': insert,
        'print': print_arr,
        'remove': remove,
        'append': append,
        'sort': sort,
        'pop': pop,
        'reverse': reverse
    }
    
    for _ in range(N):
        command, *args = input().split()
        if command in command_map:
            command_map[command](arr, *map(int, args))
