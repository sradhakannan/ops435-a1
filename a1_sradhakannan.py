#!/usr/bin/env python3
'''
OPS435 Assignment 1 - Fall 2019 
Program: a1_sradhakannan.py 
Author: Swarnadharan Radhakannan The python code in this file (a1_sradhakannan.py) is original work written by Swarnadharan Radhakannan. No code in this file is copied from any other source except those provided by the course instructor, including any person, textbook, or on-line resource. I have not shared this python script with anyone or anything except for submission for grading. I understand that the Academic Honesty Policy will be enforced and violators will be reported and appropriate action will be taken.
'''

import sys
import os
import subprocess


def usage():
    
    '''
    usage() function checks the length of the sys.argv and if it is not equal to 4 or 3 then it has to print the usage message :age:',sys.argv[0],'[--step] YYYY/MM/DD +/-n'
    '''
    
    if len(sys.argv) != 4 or len(sys.argv) != 3:
        print('Usage:',sys.argv[0],'[--step] YYYY/MM/DD +/-n')
  

if len(sys.argv) == 4:
    if len(sys.argv[2]) == 10:
        date=sys.argv[2]
        str_year, str_month, str_date=date.split('/')
        year=int(str_year)
        month=int(str_month)
        date=int(str_date)
        days=int(sys.argv[3])
    else:
	    print("Error: wrong date entered")
	    sys.exit()
elif len(sys.argv) == 3:
    if len(sys.argv[1]) == 10:
        date=sys.argv[1]
        str_year, str_month, str_date=date.split('/')
        year=int(str_year)
        month=int(str_month)
        date=int(str_date)
        days=int(sys.argv[2])
    else:
	    print("Error: wrong date entered")
	    sys.exit()
else:
    usage()    
    
def valid_date():
    
    '''
    In valid_date function it checks the number of sys.srgv, if it is 4 then it has to check for date is less than or equal to 31 and month is less than or equal to 12 and length of the sys.argv[2] is equal to      10. Return 'true' if the condition is true else it will return the appropriate error message.
    elseif it is 3 then it has to check for date is less than or equal to 31 and month is less than or equal to 12 and length of the sys.argv[1] is equal to 10. Return 'true' if the condition is true else it        will return the appropriate error message.
    else it will call the usage function.
    '''
    
    if len(sys.argv) == 4:
        if date <= 31 and month <= 12 and len(sys.argv[2]) == 10:
            return 'true'
        else:
            if date > 31:
                a= "Error: wrong day entered"
            elif month > 12:
                a= "Error: wrong month entered"
            elif len(sys.argv[2]) != 10:
                a= "Error: wrong date entered "
            return a 
    elif len(sys.argv) == 3:
        if date <= 31 and month <= 12 and len(sys.argv[1]) == 10:
            return 'true'
        else:
            if date > 31:
                a= "Error: wrong day entered"
            elif month > 12:
                a= "Error: wrong month entered"
            elif len(sys.argv[1]) != 10:
                a= "Error: wrong date entered "
            return a
    else:
        usage()

def leap_year():
    
    '''
    leap_year function checks for valid_date function, if it is 'true' then it checks for (year % 400) == 0 or ((year%4==0 and year%100!=0)) and return True or False. Else it return the valid_date() 
    function
    '''
    
    if valid_date() == 'true':
        if (year % 400) == 0 or ((year%4==0 and year%100!=0)) :
	        return True
        else:
            return False
    else:
        return valid_date()
 
def days_in_month(month):
    
    '''
    days_in_month function will take one argument month as a integer and it checks for valid_date and leap_year function and sets the feb_max value for the mon_max dictionary.
    '''
      
    if valid_date() == 'true':
        if leap_year():
            feb_max=29
        else:
            feb_max=28
        mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        days_m=mon_max[month]
        return days_m
  
   

def after(today):
    
    '''
    after(today) -> str
    after() takes a valid date string in 'YYYY/MM/DD' format and return a 
    date string for the next day in 'YYYY/MM/DD' format.
    e.g. after('2017/12/31') -> '2018/01/01'
    after('2018/01/31') -> '2018/02/01'
    after('2018/02/28') -> '2018/03/01'
    (END)
    '''
    
    if valid_date() == 'true':
        date_a=today
        str_year, str_month, str_date=date_a.split('/')
        year_a=int(str_year)
        month_a=int(str_month)
        date_a=int(str_date)
        temp_date= date_a + 1
        if temp_date > days_in_month(month_a):
            temp_date = 1
            temp_month = month_a+1
            temp_year=year_a
            if temp_month > 12: 
                temp_month = 1
                temp_year=year_a +1
        else:
            temp_month=month_a
            temp_year=year_a 
        next_day=str(temp_year).zfill(4)+'/'+str(temp_month).zfill(2)+'/'+str(temp_date).zfill(2)
        return next_day
    else:
        return valid_date()
          
def before(today):
    
    '''
    before(today) -> str
    before() takes a valid date string in 'YYYY/MM/DD' format and return a 
    date string for the next day in 'YYYY/MM/DD' format.
    e.g. before('2018/01/01') -> '2017/12/31'
    before('2018/02/01') -> '2018/01/31'
    before('2018/03/01') -> '2018/02/28'
    (END)
    '''
    if valid_date() == 'true':
        date_b=today
        str_year, str_month, str_date=date_b.split('/')
        year_b=int(str_year)
        month_b=int(str_month)
        date_b=int(str_date)
        temp_dateb= date_b - 1
        if temp_dateb == 0 :
            temp_monthb = month_b - 1
            if temp_monthb == 0: 
                temp_monthb = 12
                temp_yearb=year_b - 1
            else:
                temp_yearb=year_b
            temp_dateb=days_in_month(temp_monthb)
        else:
            temp_monthb=month_b
            temp_yearb=year_b 
        previous_day=str(temp_yearb).zfill(4)+'/'+str(temp_monthb).zfill(2)+'/'+str(temp_dateb).zfill(2)
        return previous_day
    else:
        return vali_date()


def dbda(result, days):
    
    '''
    dbda() funtion accepts two string arguments result and days and it check for           sys.argv value. if it is 3 and based on the days value it will run the for loop and    return the result
    '''
    
    if len(sys.argv) == 3:
        if int(days)>= 0:
            for one in range(int(days)):
                result=after(result)
            return result
        if int(days) < 0:
            for one in range(abs(int(days))):
                result=before(result)
            return result
    elif  len(sys.argv) == 4:
        if int(days) >= 0:
            for one in range(int(days)):
                result=after(result)
                print(result)
        if int(days) < 0:
            for one in range(abs(int(days))):
                result=before(result)
                print(result)	
     

if __name__ == "__main__":
    
    if len(sys.argv) == 3: 
        print(dbda(sys.argv[1],sys.argv[2]))
    elif (len(sys.argv)==4 and sys.argv[1]== '--step'):
        dbda(sys.argv[2],sys.argv[3])   
    
