import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city(chicago, new york city, washington) HINT: Use a while loop to handle invalid inputs

    city = input("\nPlease enter the city from these chicago, new york city, washington:")
    city = city.lower()
    while city != 'chicago' and city != 'new york city' and city != 'washington':
        print("\nInvalid input! ")
        city = input("\nPlease enter the city from these chicago, new york city, washington:")
        city = city.lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input("\nPlease enter any month from january to june or all : ")
    month = month.lower()
    while month not in month_list:
        print("\nInvalid input")
        month = input("\nPlease enter any month from january to june or all : ")
        month = month.lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input("\nPlease enter the day or all: ")
    day = day.lower()
    while day not in day_list:
        print("\nInvalid input")
        day = input("\nPlease enter the day or all: ")
        day = day.lower()
    print('-' * 40)
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
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == 'all':
        x = df['month'].mode()[0]
        print("The most common month =", x)

    # TO DO: display the most common day of week
    if day == 'all':
        y = df['day'].mode()[0]
        print("The most common day =", y)

        # TO DO: display the most common start hour
        z = df['hour'].mode()[0]
        print("the most common hour =", z)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    x = df['Start Station'].mode()[0]
    print("The most common used start station is", x)
    # TO DO: display most commonly used end station
    y = df['End Station'].mode()[0]
    print("The most common used end station is", y)
    # TO DO: display most frequent combination of start station and end station trip
    z = df['Start Station'] + df['End Station'].mode()[0]
    print("The most frequent combination of start station and end station trip is ", z[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    ttt = df['Trip Duration'].sum()
    print("Total travel time = ", ttt)

    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
    print("Mean travel time", mean)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types are: \n", user_types)
    # TO DO: Display counts of gender
    if city == 'chicago' or city == 'new york city':
        gender = df['Gender'].value_counts()
        print("Counts of gender are: \n", gender)
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        print("The earliest year of birth is ", earliest)
        recent = df['Birth Year'].max()
        print("The most recent year of birth is ", recent)
        common = df['Birth Year'].mode()[0]
        print("The most common year of birth is ", common)
        print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def view_data(df):
    loc = 0
    view = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    if view.lower() == 'yes':
        while True:
            data = (df.iloc[loc:loc + 5])
            print(data)
            loc += 5
            display = input("do you wish to continue? ").lower()
            if display.lower() == 'yes':
                print("ok we will continue")
            elif display.lower() == 'no':
                print("we will stop now")
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        view_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
