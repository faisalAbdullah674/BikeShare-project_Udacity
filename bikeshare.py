import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input("Choose a city name (chicago, new york city, washington)\n : ")).lower()
    while city not in CITY_DATA.keys():#keys() means chicago, new your city, and washington
        print("Your city isn't valid, please enter a valid city")
        city = str(input("choose a city name (chicago, new york city, washington\n : ")).lower()
  

    # TO DO: get user input for month (all, january, february, ... , june)
    months=['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = str(input("Choose a one of these months 'January','February','March','April','May','June', or 'All the months'\n : ")).lower()
    if month == "all the months":
          month="all" 
    else:
            while month not in months:
                month = str(input("Please write a valid month\n : ")).lower()
                if month in months:
                    break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['sunday', 'monday', 'tuesday', 'wedensday', 'thursday', 'friday', 'saturday', 'all']
    day = str(input("Choose a specific day(Sunday,Monday,... etc) or write all\n : ")).lower()
    if day == "all the days": #It'll be fine if the user wrote "All the days" 
          day="all"
    else:
            while day not in days: #if the user wrote an invalid day, then the script asks the user to write a valid day
                day=str(input("Please write a valid day like sunday, monday,... etc\n : ")).lower()
                if day in days: #if he/her wrote a valid day, then the loop will stop by using break key word
                    break
                    
    print('-'*40)
    print("Excellent you choosed",city,",",month[0:3],", and",day,"\n") #Display a message to the user with his/her choices
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city]) #Read the city selected by the user, for example if the user select Chicago, then this line will read the chicago.csv
    df['Start Time']= pd.to_datetime(df['Start Time']) #To separate the month, day, and hour so that I can use each of them separately.
    df['month']= df['Start Time'].dt.month #Extract the month into a new column. dt = date time
    
    if month != 'all':
        months=['january', 'february', 'march', 'april', 'may', 'june']
        month=months.index(month)+1 # I wrote "+1" because the index starts with 0.
        df= df[df['month'] == month] #Create new data frame
     
    df['day_of_week'] = df['Start Time'].dt.weekday_name #Extract the days
    df['start hour'] = df['Start Time'].dt.hour #Extract the hours ( To use it on time_stats funcation )
    
    if day != 'all': #Same idea with line number 68
        df= df[df['day_of_week'] == day.title()]
        
    return df

def Convert_the_month_to_string(month): #Additional method
    months=['january', 'february', 'march', 'april', 'may', 'june']

    for i in range(len(months)):
        if i+1==month: #To compare the index+1 with the number of the month
            month=months[i]
    return month #Return the name of the month rather than  the number of the month.


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    most_common_month= df['month'].value_counts().idxmax() #idmax() returend the maximum numer in the column
    Name_of_the_month= Convert_the_month_to_string(most_common_month)
    print("The most common month is the: "+str(most_common_month)+"th month",Name_of_the_month.title())
    
    # TO DO: display the most common day of week
    most_common_day_of_week= df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is:",most_common_day_of_week)
    
    # TO DO: display the most common start hour
    most_common_start_hour= df['start hour'].value_counts().idxmax()
    print("The most common start hour is:",most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station= df['Start Station'].value_counts().idxmax()
    print("The most common start station is:",most_start_station)

    # TO DO: display most commonly used end station
    most_end_station= df['End Station'].value_counts().idxmax()
    print("The most common end station is:",most_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df["combination"] = df["Start Station"]+ " to " +df["End Station"]
    print ("The most frequent combination of start station and end station is:", df["combination"].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    Sum_duration= df['Trip Duration'].sum()
    Mean_duration= df['Trip Duration'].mean()
    # TO DO: display total travel time
    print("The total travel time is: "+str(Sum_duration)+" days")

    # TO DO: display mean travel time
    print("The average travel time is: "+str(Mean_duration)+" sec") #Mean = Average

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users = df['User Type'].value_counts().to_frame()
    print("The count of all users for each type is: \n",users)
    
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts().to_frame()
        print("\n\nThe count of all users for each gender is:\n",gender)
    except:
         print("\nWashington doesn't have a Gender column")

    print("-------------------------------------------")
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest=df['Birth Year'].min() #Minimum number in the column
        most_recent= df['Birth Year'].max()
        common_year= df['Birth Year'].value_counts().idxmax()
    
        print("The earliest year of birth is: ",int(earliest))
        print("The most recent year of birth is: ",int(most_recent))
        print("The most common year of birth is: ",int(common_year))
    except:
         print("Washington doesn't have a Birth Year column")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display(df): 
    #Display the info of the city as chunks of 5 rows for each press "Yes"
    start,end=0,5
    keyboard = input("Wanna display five rows of the data? Write 'Y' or 'N'--> ").lower()
    if keyboard=="yes":
            keyboard="y"
    elif keyboard=="no":
            keyboard="n"
    while True:
        if keyboard.lower() in ['y', 'n']:
            if keyboard.lower() == 'y':
                print(df[start:end])
                start += 5
                end += 5
                keyboard = input("Wanna display the next five rows of the data? Write 'Y' or 'N'--> ").lower()
            else:
                break
                
        else:
            print("\n**Invalid input, please write yes or no**\n")
            keyboard = input("Wanna display the five rows of the data? Write 'Y' or 'N'--> ").lower()
            
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
