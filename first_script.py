start = (6*60+52)*60
easy = (8*60+15)*2
fast = (7*60+12)*3
finish_hour = (start + easy + fast)/(60*60.0)
finish_floored = (start + easy + fast)//(60*60)  
finish_minute  = (finish_hour - finish_floored)*60
print ('Finish time was %d:%d' % (finish_hour,finish_minute))

def print_twice(meg):
    print(meg)
    print(meg)

print_twice('lucy')

def right_justify(monty):
    space = " "*(70-len(monty))
    print(space + monty)

right_justify('hellen')

def do_twice(f, arg):
    f(arg)
    f(arg)

do_twice(print_twice, 'spam')

def print_spam():
    print('spam')

def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

do_four(print_twice, 'spam')

def draw_box():
    line = ' - '
    row = '+'+line*4
    rows = row*2+'+'
    # column = '|'+len(rows)
    print(rows)
    do_twice(print_twice, '|')
    print(row*2+'+')
    do_twice(print_twice, '|')
    print(row*2+'+')

draw_box()
