from models import graph ,node
import csv
from  datetime import datetime
from datetime import date

# create a dictionary for the months
monthDict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9,
             'Oct': 10, 'Nov': 11, 'Dec': 12}


# read files content
# process data: remove missing rows , handle time str's
# return : 2 dict : nodesdict= paths and overall time spent ,countdict =overall pepole go throw this path
def proccessdata(name):

    #print (name)
    #parmeters
    i = 1
    nodesdict = {}
    countdict ={}
    #print(len(paths))

    with open(name) as f:
        reader = csv.reader(f)
        roads=list(reader)

    # Go over paths list
    # extract paths , time between paths , and number of paths traveled.
    while i<=len(roads )-1:
        if len(roads [i])==4: # avoid cases where record is missing data
            #function handle hour , day , month not in the right formats
            f_handlehour = (lambda hour: str('0') if hour == '00' else str(hour))
            lf_handleday = (lambda day: str('01') if day == '00' else str(hour))
            lf_convertdate = lambda _month: int (monthDict[_month]) if _month in monthDict else int(1)

            if name=='travelsWE.csv': #example:['Center', '04:35:00AM ; Jan 02 16', 'South', '07:39:00AM ; Jan 02 16']
                # From Datetime
                em,month,day,year=roads [i][1].split(';')[1].split(' ')
                hour  = f_handlehour(roads [i][1].split(';')[0][:2]) # hour
                minutes= roads [i][1].split(';')[0][3:5] # minute

                if (int(hour) < 0 or int(hour) > 23): hour = '12'  # handle row where hour is not legal set to 12
                if (int(minutes) < 0 or int(minutes) > 60): minutes = '00'  # handle row where hour is not legal set to 12


                #set time left Date time object
                _timeleft= datetime(year=int(year), month=lf_convertdate(month), day=int(lf_handleday(day)), hour=int(hour) , minute=int(minutes))

                # To DateTime
                #if i>982:
                #  print(i)

                try:
                    em,tomonth,today, toyear = roads [i][3].split(';')[1].split(' ')
                except Exception:
                    em, tomonth, today, toyear = roads[i][3].split(':')[3].split(' ')

                tohour = f_handlehour(roads [i][3].split(';')[0][:2])  # hour
                tominutes = roads [i][3].split(';')[0][3:5]  # minute

                if (int(tohour)<0 or int(tohour)>23): tohour='12' # handle row where hour is not legal set to 12
                if (int(tominutes) < 0 or int(tominutes) > 60): tominutes = '00'  # handle row where hour is not legal set to 12

                # set time left Date time object
                _timearrived = datetime(year=int(toyear), month=lf_convertdate(tomonth), day=int(lf_handleday(today)), hour=int(tohour), minute=int(tominutes))

                _timespentonroad= _timearrived -_timeleft

                lista=[]
                lista= [roads[i][0],roads[i][2],_timespentonroad]


                # Build dict holds time on each path
                if (float(lista[2].total_seconds()) > 0):  # handle cases where we get negative result
                    if '{}_{}'.format(lista[0], lista[1]) in nodesdict :
                        #print('{}_{}'.format(lista[0],lista[1]))
                        nodesdict['{}_{}'.format(lista[0], lista[1])] = int(nodesdict['{}_{}'.format(lista[0],lista[1])]) + float(lista[2].total_seconds())
                    else:
                        nodesdict['{}_{}'.format(lista[0], lista[1])] = 0
                else:(lista[2].total_seconds())

                # Build dict holds number of users go throw this  path
                if '{}_{}'.format(lista[0], lista[1]) in countdict:
                    countdict['{}_{}'.format(lista[0], lista[1])] = int(countdict['{}_{}'.format(lista[0],lista[1])]) + 1
                else:
                    countdict['{}_{}'.format(lista[0], lista[1])] = 0
            elif name=='travelsEW.csv': # example :['Center', '01/01/2016 00h15m', 'West', '01/01/2016 01h50m']
                # From Datetime
                day, month, year = roads[i][1].split(' ')[0].split('/')
                hour = f_handlehour(roads[i][1][11:13])  # hour
                minutes = roads[i][1][14:16]  # minute

                if (int(hour) < 0 or int(hour) > 23): hour = '12'  # handle row where hour is not legal set to 12
                if (int(minutes) < 0 or int(minutes) > 60): minutes = '00'  # handle row where hour is not legal set to 12

                # set time left Date time object
                _timeleft = datetime(year=int(year), month=int(month), day=int(day), hour=int(hour), minute=int(minutes))

                # To DateTime
                today, tomonth, toyear = roads[i][3].split(' ')[0].split('/')
                tohour = f_handlehour(roads[i][3][11:13])  # hour
                tominutes = roads[i][3][14:16]  # minute

                if (int(tohour) < 0 or int(tohour) > 23): tohour = '12'  # handle row where hour is not legal set to 12
                if (int(tominutes) < 0 or int(
                    tominutes) > 60): tominutes = '00'  # handle row where hour is not legal set to 12

                # set time left Date time object
                _timearrived = datetime(year=int(toyear), month=int(tomonth), day=int(today), hour=int(tohour),
                                        minute=int(tominutes))

                _timespentonroad = _timearrived - _timeleft

                lista = []
                lista = [roads[i][0], roads[i][2], _timespentonroad]

                # Build dict holds time on each path
                if (float(lista[2].total_seconds()) >0):  # handle cases where we get negative result
                    if '{}_{}'.format(lista[0], lista[1]) in nodesdict:
                        nodesdict['{}_{}'.format(lista[0], lista[1])] = int(nodesdict['{}_{}'.format(lista[0], lista[1])]) + float(lista[2].total_seconds())
                    else:
                        nodesdict['{}_{}'.format(lista[0], lista[1])] = 0
                else:
                    print (float(lista[2].total_seconds()))

                # Build dict holds number of users go throw this  path
                if '{}_{}'.format(lista[0], lista[1]) in countdict:
                    countdict['{}_{}'.format(lista[0], lista[1])] = int(countdict['{}_{}'.format(lista[0], lista[1])]) + 1
                else:
                    countdict['{}_{}'.format(lista[0], lista[1])] = 0
        else:
            pass
        i = i + 1

    return nodesdict ,countdict


# Task 3
# Question 1
# for each file :travelsEW.csv and travelsWE.cs
#   create a graph whose nodes are the country regions, and whose edges are the roads themselves
#       weight of each edge is defined as the average time (in seconds) of all the travels done on that road

timedict_we,countdict_we=proccessdata('travelsWE.csv')
timedict_ew,countdict_ew=proccessdata('travelsEW.csv')


avgdict_ew={}
avgdict_we={}


# Build dict holds avg = time spent on path / number of users go throw this  path
for k,v in timedict_we.items():
    avgdict_we[k] = int(round(v/countdict_we[k]))

# Build dict holds avg = time spent on path / number of users go throw this  path
for kew,vew in timedict_ew.items():
    avgdict_ew[kew] = int(round(v/countdict_ew[kew]))

# Create first Graph
nodes=[]
# k exmple - north_east:1233
for k,v in avgdict_we.items():
     mnode = node.Node(k.split('_')[0], {})
     mnode.add_edge(k.split('_')[1], v)
     nodes.append(mnode)
graph1= graph.Graph('r1', nodes)
print(graph1)

# Create second Graph
nodes=[]
for k,v in avgdict_ew.items():
     mnode = node.Node(k.split('_')[0], {})
     mnode.add_edge(k.split('_')[1], v)
     nodes.append(mnode)
graph2= graph.Graph('r2', nodes)
print(graph2)

graph3 = graph1+graph2
print(graph3)
