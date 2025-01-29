#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  hours = input("Enter Hours: ")
  hours = int(hours) #change text to numbers

  mins = input("Enter Minutes: ")
  mins = int(mins)

  currentHour = int(currentHour)
  currentMinute = int(currentMinute)

  futureHour = currentHour + hours
  futureHour = futureHour % 24  
  

  futureMinute = currentMinute + mins
  futureMinute = futureMinute % 60
 


  StrHour = str(futureHour)
  StrMin = str(futureMinute)

  print(StrHour + ":" + StrMin)
  
  
  
  #Ask user for minutes

  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
