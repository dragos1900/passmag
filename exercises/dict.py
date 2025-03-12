import datetime

adate = datetime.datetime.now()
dateepoch = adate.timestamp()
details = dict(age = 34, weight = 90, update = dateepoch )
thisdict = dict(name = "John", persondetails = details)
print(thisdict["name"], thisdict["persondetails"]["age"], thisdict["persondetails"]["update"])