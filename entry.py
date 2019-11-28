
from datetime import datetime
from datetime import date

def timeStamp():
    dates=[]
    now=datetime.now()
    dates.append((now.strftime("%a,%d %B, %y")))           # Date - format(Day,Date Month , Year)
    dt=datetime.time(datetime.now())
    dates.append(dt.strftime("%I:%M %p"))                   #Time - format (Hour:Minute AM/PM)
    return(dates)
 