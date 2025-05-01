import time
# asks for name
name = input("What is your name? ")
# asks for age
years = int(input("How old are you? "))
# sets what days are in terms of year
days = years*365
print("You have been alive for", days,"days")
# delays print for 1 second 
time.sleep(1)
# sets hours in terms of days
hours = days*24
print("You have been alive for", hours,"hours")
time.sleep(1)
# sets mins in terms of hours
mins = hours*60
# sets secs in terms of mins
secs = mins*60
print("You have been alive for", mins,"minutes")
time.sleep(1)
print("And You have been alive for", secs,"seconds")