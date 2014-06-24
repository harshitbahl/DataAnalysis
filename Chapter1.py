# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 22:00:19 2014

@author: harshitbahl
"""

def main():
    import json
    path = '../pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
    records = [json.loads(row) for row in open(path)]
    records[0]
    from pandas import DataFrame, Series
    import pandas as pd; import numpy as np
    frame = DataFrame(records)
    frame
    tz_counts = frame['tz'].value_count()
    tz_counts = frame['tz'].value_counts()
    tz_counts[:10]
    clean_tz = frame['tz'].fillna('Missing')
    clean_tz[clean_tz == '']= 'Unknow'
    tz_counts = clean_tz.value.counts()
    tz_counts = clean_tz.value_counts()
    tz_counts[:10]
    tz_counts[:10].plot(kind='barh', rot=0)

    
    





if __name__ == '__main__':
    main()