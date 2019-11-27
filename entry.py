
from datetime import datetime
from datetime import date
#dates=[]
def timeStamp():
    
    # dt=datetime.time(datetime.now())
    # current_time = dt.strftime("%H:%M:%S")
    dates=[]
    # return(dt.strftime("%I:%M %p"))
    #print(datetime.time(datetime.now()))
    #d=datetime.date(datetime.now())
    now=datetime.now()
    dates.append((now.strftime("%a,%d %B, %y")))
    dt=datetime.time(datetime.now())
    dates.append(dt.strftime("%I:%M %p"))
    return(dates)
#timeStamp()    