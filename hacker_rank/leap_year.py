#!/usr/bin/python3


def is_leap(year):
    leap = False
   
    for i in year: 
        # Write your logic here 
        if i % 4==0:
           if i % 100 == 0:
              if i % 400 == 0:
                 leap=True
           elif (i % 100 != 0) and (i % 400 != 0):
              leap = True

        print ('Year "{0}" is Leap:- "{1}"'.format(i,leap))

year = [1800,1900,2100,2200,2300,2500,1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
is_leap(year)


