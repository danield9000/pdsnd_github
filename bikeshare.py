import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("Would you like to see data for Chicago, New York, or Washington?").lower()
        if city in CITY_DATA:
            break
        else:
            print("Please input valid city")

    # get user input for how he/she wishes to have data sorted
    while True:
        decision = input("Would you like to filter the data by month, day, both or not at all? Type ""none"" for no time filter.").lower()
        if decision in ["month","day","both","none"]:
            break
        else:
            print("Please provide valid input")
    
    if decision == "both":

    # get user input for month and day 
        valid_months = {"january":1, "february":2, "march":3, "april":4, "may":5, "june":6}

        while True:
            month_name = input("Which month? January, February, March, April, May or June?").lower()
            if month_name in valid_months:
                break
            else:
                print("Please input valid month")
        month = valid_months[month_name]

        while True:
            try:
                day = int(input("Which day?Please type in an integer (Monday = 0)"))
                if 0 <= day <= 6:
                    break
                else:
                    print("Please enter a number between 0 and 6")
            except ValueError:
                print("Invalid input. Please enter an integer.")
    
 
    # get user input for month  

    if decision == "month":
        valid_months = {"january":1, "february":2, "march":3, "april":4, "may":5, "june":6}

        while True:
            month_name = input("Which month? January, February, March, April, May or June?").lower()
            if month_name in valid_months:
                break
            else:
                print("Please input valid month")
        month = valid_months[month_name]
        day = "all"

    # get user input for day 

    if decision == "day":
        while True:
            try:
                day = int(input("Which day?Please type in an integer (Monday = 0)"))
                if 0 <= day <= 6:
                    break
                else:
                    print("Please enter a number between 0 and 6")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        month = "all"
    
    if decision == "none":
        day = "all"
        month = "all"
    
    return city,month,day
        


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    if month != "all" and day !="all":
        df = df[(df['month'] == month) & (df['day_of_week'] == day)]
    if month != "all":
        df = df[(df['month'] == month)]
    if day != "all":
        df = df[(df['day_of_week'] == day)]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['hour'] = df['Start Time'].dt.hour
    df["month_name"] = df["Start Time"].dt.month_name()
    popular_month = df["month_name"].mode()[0]
    popular_day = df["day_of_week"].mode()[0]
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Month:', popular_month)
    print('Most Popular Day:', popular_day)
    print('Most Popular Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    df['station_combination'] = df["Start Station"] + ' ' + df["End Station"]
    popular_start = df["Start Station"].mode()[0]
    popular_end = df["End Station"].mode()[0]
    popular_combination = df['station_combination'].mode()[0]

    print('Most Popular Start Station:', popular_start)
    print('Most Popular End Station:', popular_end)
    print('Most Popular Trip:', popular_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    travel_time = df["Trip Duration"].sum()
    mean_travel_time = df["Trip Duration"].mean()

    print('Total Travel Time:', travel_time)
    print('Mean Travel Time:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    count_user_types = df['User Type'].value_counts().reset_index(name='count')
    print('\nUser Type Breakdown:\n')
    print(count_user_types)

    try:
        count_genders = df['Gender'].value_counts().reset_index(name='count')
        print('\nGender Breakdown:\n')
        print(count_genders)
    except KeyError as e:
        print(f"\nGender information is not available for this city\n")


    try:
        count_genders = df['Gender'].value_counts().reset_index(name='count')
        print('\nDate of Birth Information:\n')
        earliest_birth = df["Birth Year"].min()
        latest_birth = df["Birth Year"].max()
        most_common_birth = df["Birth Year"].mode()[0]
        print('Earliest Birth Year:', earliest_birth)
        print('Latest Birth Year:', latest_birth)
        print('Most Common Birth:', most_common_birth)
    except KeyError as e:
        print(f"\nDate of birth informtion is not available for this city\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """Displays raw data on user's demand"""
    i = 0
    while True:
        raw_data = input('\nWould you like to see raw data or another 5 lines of raw data? Enter yes or no.\n')
        if raw_data.lower() != 'yes':
            break
        print(df.head(5+i))
        i+=5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
     
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
