#script to open a file, find all the tasks, and append them to another file

from datetime import datetime
from sys import argv

#arguments
argv[0] = 'taskcollector.py'

#--if the -t option is passed
#---the last argument is the file you want your tasks written to
if argv[1] == '-t':
    files = argv[2:-1]
    taskfile = argv[-1]

#--if no option
#---new file is written with tasks
else:
    files = argv[1:]

#two formats for date strings
date_dot = datetime.now().strftime('%d.%m.%Y')
date_dash = datetime.now().strftime('%Y-%m-%d')

#initialize tasks array
tasks = []
for f in files:
    #get name of file (for later referencing)
    tasks.append(f+ '\n')
    df = open(f)
    lines = df.readlines()
    df.close()
    for l in lines:
        if (('[ ]' in l) or ('[x]' in l)):
            #get tasks in file
            tasks.append(l)

#if taskfile is specified
#--open the given file and writes the date
if argv[1] == '-t':
    g = open(taskfile,'a+')
    g.write('# ' + date_dot + '\n')
#if taskfile not specified
#--create new file with name 'tasks_YYY-MM-DD.md' and writes the date
else:
    g = open('taskcollector_'+date_dash+'.md','w+')
    g.write('# '+date_dot + '\n\n')

#writes the filenames and tasks
for t in tasks:
    g.write(t)

g.close()
