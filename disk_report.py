
#!usr/bin/python3

# now we will use the __name__ to dentify the main code and use sys.argv to access the command line arguments

import sys
import os
import pandas as pd

#creating a function to determine space used by each directory
def get_size(path):
    total=0
    for entry in os.scandir(directory):
        try:
            if entry.is_dir(follow_symlinks=False):
                total+=get_size(entry.path) # if its a directory its going for a recursion
            else:
                total+=entry.stat(follow_symlinks=False).st_size # if its a file its adding size tot the total
        except Exception as e:
            print("Exception: ",e)
            total+=0 # if there is exception keep total as it is

if __name__ == '__main__':
     path = '/Users'
     print("Total arguments passed: ",len(sys.argv))
     directory = sys.argv[1] if len(sys.argv)>=2 else path
     
     usage=[]
     paths=[]
     with os.scandir(path) as it:
         for entry in it:# create a for loop to access each subdirectory
             print(entry.path)
             if (entry.is_dir(follow_symlinks=False)):
                 # So the above statement means that if the 'entry' is a directory and there are no symbolic links
                 print(entry.path + 'is a directory')
                 print(total)
                 paths.append(entry.path)
                 usage.append(total)
             # Now lets import disk usage data in csv format
             usage_dict = {'directory' : path,'usage' : usage}
             df = pd.DataFrame(usage_dict)
             print(df)
             df.to_csv("disk_home_usage.csv")
        
                
                
    
    
     
