import re
from datetime import datetime, timedelta

class Nap:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
    
    def napTime(self):
        return (self.end - self.begin).total_seconds()/60


class Guard:
    def __init__(self, id):
        self.id = id
        self.nap = []
    
    def takeNap(self, begin, end):
        self.nap.append(Nap(begin, end))

    def totalNap(self):
        total = 0
        for nap in self.nap:
            total += nap.napTime()
        return total
    
    def __str__(self):
        return "Guard %s napped %d times for %d minutes, mostly on minute %d (%d times)" % (self.id, len(self.nap), self.totalNap(), self.sleepyMinute(), self.sleepyMinute2())

    def sleepyMinute(self):
        minutes = [0] * 60
        for nap in self.nap:
            for x in range(nap.begin.minute, nap.end.minute):
                minutes[x]+= 1
        return minutes.index(max(minutes))

    def sleepyMinute2(self):
        minutes = [0] * 60
        for nap in self.nap:
            for x in range(nap.begin.minute, nap.end.minute):
                minutes[x]+= 1
        return max(minutes)
            

pattern = re.compile(r'\[(.+)\] (.+)')
dateformat = '%Y-%m-%d %H:%M'

data = []
with open('./input4.txt') as fp:
    line = fp.readline()
    while line:
        parse = pattern.match(line.strip())
        if parse:
            a = datetime.strptime(parse.group(1),dateformat)
            b = parse.group(2)
            data.append([a,b])
        line = fp.readline()

history = sorted(data)
guards = {}
theGuard = None
napStart = None
napEnd = None
for x in history:
    guardIdSearch = re.search('#(\d+)',x[1])
    if guardIdSearch:
        theGuardId = guardIdSearch.group(1)
        if theGuardId in guards:
            theGuard = guards[theGuardId]
        else:
            theGuard = Guard(theGuardId)
            guards[theGuardId] = theGuard
    elif theGuard:
        if napStart:
            theGuard.takeNap(napStart, x[0])
            napStart = None
        else:
            napStart = x[0]


# problem 1 
for key, value in sorted(guards.items(), key=lambda el: (el[1].totalNap(),el[0]), reverse=True):
    print (value)
    print( int(value.id)*value.sleepyMinute())
    break

# problem 2
for key, value in sorted(guards.items(), key=lambda el: (el[1].sleepyMinute2(),el[0]), reverse=True):
    print (value)
    print( int(value.id)*value.sleepyMinute())
    break
 
