import time
import pandas as pd
import numpy as np
from statistics import mode
from datetime import datetime

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city(chicago, new york city, washington).HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please Type the city you would like to review, Chicago, New York City, or Washington?")
        city = city.lower()
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            break
        else:
            print('Choose Chicago, New York City, or Washington please!')

    while True:
        question = input('Would you like to filter the data by month, day, or both?')
        question = question.lower()
        options = ['day', 'month', 'both']

        if question in options:
            break
        else:
            print('Please choose day , month, or both!')

    # TO DO: get user input for month (all, january, february, ... , june)
    if question == 'month':

        while True:
            # get user input for month (all, january, february, ... , june)
            month = input('Which month - January, February, March, April, May, or June?')
            month = month.lower()
            months = ['january', 'february', 'march', 'april', 'may', 'june']

            if month in months:
                break
            else:
                print('please choose a month, January, February, March, April, May, or June!')
        day = 'no'
    elif question == "day":
        while True:
            day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?')
            day = day.lower()
            week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

            if day in week:
                break
            else:
                print(
                    'please type a day of the week, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday!')
        month = 'no'
    elif question == "both":
        while True:
            month = input('Which month - January, February, March, April, May, or June?')
            month = month.lower()
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            if month in months:
                break
            else:
                print('please choose a month, January, February, March, April, May, or June!')

        while True:
            day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?')
            day = day.lower()
            week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

            if day in week:
                break
            else:
                print(
                    'please type a day of the week, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday!')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

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
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name
    df['day'] = df['Start Time'].apply(lambda x: datetime.strftime(x, '%A'))
    df['month'] = df['Start Time'].apply(lambda x: datetime.strftime(x, '%B'))

    # filtring data

    if day != 'no' and month != 'no':
        df = df[(df['month'] == month.title()) & (df['day'] == day.title())]
    elif month == 'no':
        df = df[df['day'] == day.title()]
    elif day == 'no':
        df = df[df['month'] == month.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    day = df['day'].mode()[0]

    # TO DO: display the most common start hour
    h = mode([pd.Timestamp(i).hour for i in df['Start Time']])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('common month : ', month)
    print('common day   : ', day)
    print('common hour  : ', h)
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    trip = df[df['Start Station'] == df['End Station']]['Start Station'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('commonly used start station : ', start_station)
    print('commonly used end station   : ', end_station)
    print('commonly used trip          : ', trip)
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('total travel time : ', total)
    print('mean travel time  : ', mean)
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count = df['User Type'].value_counts()

    if 'Gender' in df.keys() and 'Birth Year' in df.keys():

        # Display counts of gender
        gender_count = df['Gender'].value_counts()

        # Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common = df['Birth Year'].mode()[0]

    else:
        gender_count = 'This Data Frame not have gender !'
        earliest = 'not-founad'

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('counts of user types :\n', user_count)
    print('counts of gender     :\n', gender_count)
    print('-' * 15)
    if earliest == 'not-founad':
        print('earliest year of birth : This Data Frame not have date of birth!')
    else:
        print('earliest year of birth    : ', earliest)
        print('recent year of birth      : ', recent)
        print('most common year of birth : ', common)
        print('-' * 40)


def raw_data(df):
    # get 5 rows  of data
    count = 5
    data_df = df.head()

    # print data frame
    print(data_df)
    while True:
        # if user want more 5 rows or no
        user_answer = input('Do you want 5 more rows? please write yes or no')
        user_answer = user_answer.lower()

        if user_answer == 'yes':
            data_df = df.iloc[count:count + 5]
            count = count + 5
            print(data_df)
        else:
            break


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