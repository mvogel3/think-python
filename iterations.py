#  updating the countdown function using a while loop
def countdown(n):
    while n > 0:
        print(n)
        n = n-1

def sequence(n):
    """function that results in a sequence but no one has proven whether it will always terminate"""
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n / 2
        else:
            n = n*3 + 1

def print_n(s, n):
    while n > 0:
        print(s)
        n = n-1
# print_n('hi', 3)

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')