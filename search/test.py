i = 0

def print_global():
    global i
    if i == 0:
        print "i",i
        i = i+1
        print "adding i",i
    else:
        i = 1 + i
        print "i",i
