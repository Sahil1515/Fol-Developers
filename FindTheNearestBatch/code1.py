
from datetime import datetime , timedelta 

import calendar  
import time

# Function to convert the date format 
def convert24(str1): 
      
    # Checking if last two elements of time 
    # is AM and first two elements are 12 
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return "00" + str1[2:-2]
          
    # remove the AM     
    elif str1[-2:] == "AM": 
        return str1[:-2] 
      
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2] 
          
    else: 
          
        # add 12 to hours and remove PM 
        return str(int(str1[:2]) + 12)



# If it is today list then find the minimum
def findMinFromTodayList(index_arr,validTime,timeList):
    i=0
    index=index_arr[0]
 
    minVal=validTime[0]
    for t in validTime:
        if t<minVal:
            minVal=t
            index=index_arr[i]
        i=i+1

    return (arr1[index],timeList[index],"0")


#  Main function 

def getNextRegisteredBatch(arr1):

    timeList=[]
    for t in arr1:
        temp=int(convert24(t))
        timeList.append(temp)
    
    listToday =[]
    for t in timeList:
        datetom = datetime.today() + timedelta(days=0)
        excel_date = datetom.strftime('%Y-%m-%d')
        time_new = calendar.timegm(time.strptime(excel_date + ' ' + str(t) + ':00:00', '%Y-%m-%d %H:%M:%S'))
        listToday.append(time_new)



    time_epoch = int(time.time())


    i=0

    index_arr=[]
    validTime=[]


    for t in listToday:
        if (int(t)>time_epoch):
            validTime.append(int(t))
            index_arr.append(i)
        i=i+1
    
#Tom
    if(len(validTime)==0):
        result = min(range(len(listToday)), key=lambda i: abs(listToday[i]))
        return (arr1[result],timeList[result],"1") 

# Today
    else:
        return findMinFromTodayList(index_arr,validTime,timeList)
    




#Working
# arr1 = ["11 AM","8 AM", "9 AM","10 AM"]
# arr1 = ["11 PM","8 PM", "9 PM","10 PM"]
# arr1 = ["11 AM","8 AM", "9 AM","10 AM", "11 PM"]
# arr1 = ["11 PM","11 AM","8 AM", "9 AM","10 AM"]
# arr1 = [ "12 PM","11 AM","8 AM","9 AM","10 AM"]
# arr1 = [ "11 AM","8 AM","9 AM","10 AM"]
arr1 = [ "11 PM" , "8 PM","9 PM","10 PM"]



selected_batch, formatted_hour, selected_day= getNextRegisteredBatch(arr1)

print("Selected Batch is :"+str(selected_batch))
print("Formatted Hour is: "+str(formatted_hour))
print("Selected Day is :"+ str(selected_day))

