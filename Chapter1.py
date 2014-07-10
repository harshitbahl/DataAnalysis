# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 22:00:19 2014

@author: harshitbahl
"""

class vehicles:
    count = 0
    def __init__(self, value):
        self.value = value
        vehicles.count += 1
    def getval(self):
        return self.value
    def getcount(cls):
        return vehicles.count
    counter = classmethod(getcount) 



def main():
    v1 = 'car'
    v2 = 'Bus'
    v3 = 'bikes'
    type1 = vehicles(v1)
    type2 = vehicles(v2)
    type3 = vehicles(v3) 
    print type1.getval(), type2.getval(), vehicles.counter(), type2.getcount()


    
    





if __name__ == '__main__':
    main()