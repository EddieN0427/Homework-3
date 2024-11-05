#Eddie Neitenbach
#Lab Section: 11
#Submission date: 11/5/24



def leap_year(year):
    leapYear_4 = (year // 4) * 4 == year

    NotleapYear_100 = (year // 100) * 100 == year
    
    leapYear_400 = (year // 400) * 400 == year

    if leapYear_4 and (not NotleapYear_100 or leapYear_400):
        return True
    else:
        return False

def Jan1st_weekday(year):
    y = year - 1
    day = 36 + y + (y // 4) - (y // 100) + (y // 400)

    while day > 6:
        day -= 7  
    while day < 0:
        day += 7 
        
    return day

def date_works(month, day, year):
    monthDays = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    if leap_year(year):
        monthDays[2] = 29  
    
    if month < 1 or month > 12:
        return False
    if day < 1 or day > monthDays.get(month, 0):
        return False
    return True

def day(month, day, year):
    New_Jan1st_weekday = Jan1st_weekday(year)
    
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(year):
        month_days[1] = 29  
    totalDays = sum(month_days[:month-1]) + (day - 1)
    
    weekday = Jan1st_weekday + totalDays
    
    while weekday > 6:
        weekday -= 7  
    while weekday < 0:
        weekday += 7 
        
    return day[weekday]

def main():
    input = input("Enter date (MM/DD/YYYY): ").strip()
    
    try:
        month, day, year = (int, input.split('/'))
        
        if not date_works(month, day, year):
            print(f"{input} Invalid Date")
        else:
            weekday = (month, day, year)
            print(f"{input} {weekday}")
    
    except ValueError:
        print(f"{input} Invalid Date")
if name == "  main  ":
    main()
