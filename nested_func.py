#!/usr/bin/python

def parent():
    print("Printing from the parent() function.")

    def first_child():
        print("Printing from the first_child() function.")

    def second_child():
        print ("Printing from the second_child() function.")


    first_child()
    second_child()


parent()
'''
1)
 IF U CALL FIRST_CHILD OR SECOND_CHILD HERE. IT WONT BE CALLED.
 SINCE THEY ARE NOT DEFINED IN GLOBAL SCOPE. THEY ARE INSIDE THE
 PARENT FUNCTION.

2) ALSO TRY CALLING THE PARENT FUNCTION WITH COMMENTING first_child()
and second_child() AND WITHOUT COMMENTING the 2 functions and see the 
difference.

''' 
