#!/usr/bin/python

def math_func(*args, **kwargs):
    print ('TYPE OF ARGS...',type(args), ' * ARGS CONTAINS....', args)
    for i in args:
        print (i)
    print ('TYPE OF KWARGS...',type(kwargs), ' * KWARGS CONTAINS....', kwargs)
    for i in kwargs.items():
        print (i)


math_func(2,3,4,5,'numbers',x='55',y='yak')

# FOLLOWING FUNC CALL WILL FAIL AS THE ORDER OF ARGS AND KWARGS IS REVERESED
# X='55' IS KWARGS WHICH IS PASSED BEFORE 2,3,4,5 WHICH ARE ARGS
#math_func(x='55,y='yak',2,3,4,5,'numbers')
    
