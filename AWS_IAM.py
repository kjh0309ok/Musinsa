#!/usr/bin/env python3

from datetime import timedelta
from datetime import datetime
import sys
import os

N = int(sys.argv[1])

names = [y.strip() for y in os.popen("aws iam list-users --output text | awk '{print $NF}'")]
name = names[0]
    
Test1_key_times = os.popen("aws iam list-access-keys --user Test1  --output text | awk '{print $3}'")
Test1_key_time = Test1_key_times.read()
replace_Test1_key_time = '+'.join(str(Test1_key_time).split('+')[:-1])

now = datetime.now()
date_to_compare = datetime.strptime(str(replace_Test1_key_time), '%Y-%m-%dT%H:%M:%S')
diff_time = now - timedelta(hours=N)
over_time = date_to_compare > diff_time

#print(type(over_time))


f=open('output.txt', 'w')

for i, name in enumerate(names):
    if over_time == True:
       key = os.popen(f'aws iam list-access-keys --user {name} --output text')
       access_key = key.read()
       f.write(access_key)
    else:
       key = os.popen(f'aws iam list-access-keys --user Test1 --output text')
       access_key = key.read()
       f.write(access_key)

f.close()
