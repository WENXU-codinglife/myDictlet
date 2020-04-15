import requests
import datetime
from pytz import timezone


def datetoday():#fetch the string of today date
    x = datetime.datetime.now()
    datetime_obj_pacific = timezone('US/Pacific').localize(x)
    print(datetime_obj_pacific)

    today = "2"
    for i in range(1,10):
        today = today + str(datetime_obj_pacific)[i]
    
    return today

def differ_lists(list1,list2):
    list_difference = [item for item in list1 if item not in list2]
    return list_difference