import time
import pandas as pd
import numpy as np

# dictionary for city
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
    valid_cities = ['chicago', 'new york city', 'washington']

    while True:
        city = input('Enter a city (Chicago, New York City, Washington): ').lower()
    
        if city in valid_cities:
            break
        else:
            print('Invalid input. Please enter a valid city.')
    
    print('You have selected: ', city)

    # TO DO: get user input for month (all, january, february, ... , june)
    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    
    while True:
        month = input('Enter a month (all, January, February, March, April, May, June): ').lower()
    
        if month in valid_months:
            break
        else:
            print('Invalid input. Please enter a valid month or \'all\'.')
    
    print('You have selected: ', month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    while True:
        day = input('Enter a day of the week(all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): ').lower()

        if day in valid_days:
            break
        else:
            print('Invalid input. Please enter a valid day of the week or \'all\'.')
    
    print('You have selected: ', day)

    print('-'*40)
    print('*'*40)
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
    df = pd.read_csv(CITY_DATA[city])    
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df
    user_stats(df, city)
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print('The most common month is: ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].value_counts().idxmax()
    print('The most common day of the week is: ', most_common_day)

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print('The most common start hour is: ', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is: ', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is: ', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('The most frequent combination of start station and end station is: ', most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time, 'seconds')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: ', mean_travel_time, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print('Counts of user types: ', user_type_counts)

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print('Counts of gender: ', gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].value_counts().idxmax()

        print('Earliest birth year: ', earliest_birth_year)
        print('Most recent birth year: ', most_recent_birth_year)
        print('Most common birth year: ', most_common_birth_year)

    except KeyError:
        print("'Gender' or 'Birth Year' columns not available for", city, 'skipping analysis.')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):
    """
    Display rows of data based on user input.

    Parameters:
    - data_frame: pandas DataFrame
 
    """
 
    view_data = input('\nWould you like to view the first 5 rows of trip data? Enter yes or no\n').lower()
    start_loc = 0

    while view_data != 'no':       
        if view_data == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
        view_data = input("Do you wish to view the next 5 rows of data?: ").lower()
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
