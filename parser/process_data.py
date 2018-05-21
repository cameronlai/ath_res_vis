"""
This file converts the data into a tmp sql file.
"""

import re
import pandas as pd
import sys
import os
import dateutil.parser as date_parser
import glob
import sqlite3


def transform_to_secs(line):
    if not ':' in line:
        line = '0:' + line
    line = line.replace('.', ':')        
    m, s, ss = [int(i) for i in line.split(':')]
    return 60*m + s + ss * 0.01

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

# Settings
# These keywords are not supposed to appear in athlete search
key_words = ['Position', 'No Mark', 'take part', 'Heat', 
             'DN start', 'Points', 'DQ', 'Final Lane', 
             'DN take part'] 
key_dates = ['Day One', 'Day Two', 'Day Three']
columns = ['Name', 'School', 'Event', 'Sex', 'Result', 'Date', 'IsTrack']

# Parameters
start_search_athlete = False
cur_event = ''
cur_sex = ''
cur_date = ''
cur_track = 0
   
df = pd.DataFrame(columns=columns)

filename_list = glob.glob('data\\*.txt')
#filename_list = ['data\\1112 ath_results_d1.txt']
for filename in filename_list:
    # Open File
    print('\n%s\n' % filename)
    f = open(filename)
    lines = f.readlines()
    f.close()   
        
    # For loop
    for i, line in enumerate(lines):
        line = line.strip('\n')
        # Date checking
        if any(key_date in line for key_date in key_dates):
            m = re.match(r'Day (One|Two|Three): ([A-Za-z0-9\s]+)', line)
            date_string = m.groups()[1]
            cur_date =  date_parser.parse(date_string)  
            print('\n%s\n' % cur_date)
            continue
        
        # Event clear
        if '===' in line:
            cur_event = ''
            start_search_athlete = False
            continue
        elif '---' in line:
            start_search_athlete = True
            continue    
        
        # Event name
        if 'Event' in line and  cur_event == '':
            m = re.match(r'Event [\d]+ ([0-9A-Za-z\s]+) (Girls|Boys)', line)
            group = m.groups()
            cur_event = group[0]
            cur_sex = group[1]
            if 'Girls' in cur_sex:
                cur_sex = 'F'
            elif 'Boys' in cur_sex:
                cur_sex = 'M'
            
            cur_track = hasNumbers(cur_event)
            sys.stdout.write('.')
            continue
        
        # Athelete results parser
        if start_search_athlete and not any(word in line for word in key_words) and not '4x' in cur_event:
            m = re.match(r'[0-9\s]*([A-Za-z\.\-\'\s]+) ([A-Z]+) (\d+[:.\s]+\d+[.]*\d*)', line)
            try:
                group = m.groups()
                
                name = group[0]
                school = group[1]
                result = group[2].replace(' ', '')
                
                if cur_track:
                    result = transform_to_secs(result)
                result = float(result)
                
                df = df.append({'Name': name,
                                'School': school,
                                'Result': result,
                                'Event': cur_event,
                                'Sex': cur_sex,
                                'Date': cur_date,
                                'IsTrack': cur_track}, ignore_index=True)
            except:
                print(line)
                print("Unexpected error:", sys.exc_info()[0])
                raise

db_file = 'tmp_db.sqlite3'
try:
    os.remove(db_file)
except OSError:
    pass
conn = sqlite3.connect(db_file)
df.to_sql('ath_results', conn)
conn.close()