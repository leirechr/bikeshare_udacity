# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:39:50 2020

@author: U378217
"""
import numpy as np
import pandas as pd




CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#def load_data(city, month, day):

#df = pd.read_csv("chicago.csv")

def get_filters():
    print('-'*40)
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Would you like to see data for Chicago, New York or Washington?')
    city = input('Enter the city name: ').lower()
    if str(city) == str('chicago'):
        print('The city given is accepted')

    elif str(city) == str('new york city'):
        print('The city given is accepted')
    elif str(city) == str('washington'):
        print('The city given is accepted')
    else:
        print('Error: Please write one of the three cities given. Restarting...')
        print('-'*40)
        get_filters()
    print('-'*40)

    x=np.array(['january','february','march','april','may','june','july','august','september','october','november','december'])
    print('Would you like to filter the data by month?')
    choose_month=input('Yes/No: ').lower()
    if choose_month=='yes':
        choose_month = input('Which month? (For example: January): ').lower()
        if choose_month in x:
            print('The month is accepted')
        else:
            print('Sintax Error. Restarting...')
            get_filters()            
    elif choose_month=='no':
        print('No filters applied')
    else:
        print('Sintax Error. Restarting...')
        get_filters()            
        print('-'*40)

    print('-'*40)
    y=np.array(['monday','tuesday','wednesday','thursday','friday'])
    print('Would you like to filter the data by day?')
    choose_day=input('Yes/No: ').lower()
    if choose_day=='yes':
        choose_day = input('Which day of the week? (For example: Monday): ').lower()
        if choose_day in y:
            print('The day is accepted')
        else:
                print('Sintax Error. Restarting...')
                get_filters()        
    elif choose_day=='no':
        print('No filters applied')
    else:
        print('Sintax Error. Restarting...')
        get_filters()            
        print('-'*40)

    print('-'*40)
    return city, choose_month, choose_day  
    
    
def load_data(city, choose_month, choose_day):
    df = pd.read_csv(CITY_DATA[city])


# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
# extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour

#df['hour'] = df['Start Time'].dt.hour

#print(df['day_of_week'])

# filter by month if applicable
    months=[]
    for month in df['month']:
        if month==1:        
            #month=['january']
            months.append('january')
        elif month==2:        
            #month=['january']
            months.append('february')
        elif month==3:        
            #month=['january']
            months.append('march')
        elif month==4:        
            #month=['january']
            months.append('april')
        elif month==5:        
            #month=['january']
            months.append('may')            
        elif month==6:        
            #month=['january']
            months.append('june')            
        elif month==7:        
            #month=['january']
            months.append('july')
        elif month==8:        
            #month=['january']
            months.append('august')
        elif month==9:        
            #month=['january']
            months.append('september')
        elif month==10:        
            #month=['january']
            months.append('october')    
        elif month==11:        
            #month=['january']
            months.append('november')    
        else:        
            #month=['january']
            months.append('december')                
   # if month != 'all':
    # use the index of the months list to get the corresponding int
     #   months = ['january', 'february', 'march', 'april', 'may', 'june']
      #  month = months.index(month) + 1
        
    df['month'] = months  
  
    
    

    days=[]
    for day in df['day_of_week']:
        if day==0:        
            #month=['january']
            days.append('monday')
        elif day==1:        
            #month=['january']
            days.append('tuesday')
        elif day==2:        
            #month=['january']
            days.append('wednesday')
        elif day==3:        
            #month=['january']
            days.append('thursday')
        elif day==4:        
            #month=['january']
            days.append('friday')            
        elif day==5:        
            #month=['january']
            days.append('saturday')            
        else:        
            #month=['january']
            days.append('sunday')            

    df['day_of_week'] = days
  
    if choose_month != 'no':
        df=df[df['month']==choose_month]
   
    if choose_day != 'no':
        df=df[df['day_of_week']==choose_day]
   
    return df

#############################################
def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
     # start_time = time.time()  

    # TO DO: display the most common month
    a1 = df['month'].mode()[0]

    # TO DO: display the most common day of week
    a2 = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    a3 = df['hour'].mode()[0]

    print ('The most common month is {}. \n The most common day is {}. \n The most common hour is {}.'.format(a1,a2,a3))
    
    #print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)
    
    
    ################################################
#def station_stats(df):
    #print('\nCalculating The Most Popular Stations and Trip...\n')

    # TO DO: display most commonly used start station
    #a4 = df['Start Station'].mode()[0]


    # TO DO: display most commonly used end station
    #a5 = df['End Station'].mode()[0]


    # TO DO: display most frequent combination of start station and end station trip
    #df['station_comb']=df['Start Station']+['and']+df['End Station']
    #a6 = df['station_comb'].mode()[0]

    #print ('The most common start station is: {}.'.format(a4))
    #print ('The most common end station is: {}.'.format(a5))
    #print ('The most frequent start and end station is: {}.'.format(a6))
    #print('-'*40)

#######################################################
def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')

    # TO DO: display total travel time
    #a7 = df['Trip Duration'].mode()[0]
    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print('The total trip duration is {} hours, {} minutes and {}'
          ' seconds.'.format(hour, minute, second))




    # TO DO: display mean travel time
    print("The mean travel time is: ", np.mean(df['Trip Duration']))  
    print('-'*40)


#######################################################
def user_stats(df,city):

    print('\nCalculating User Stats...\n')

    # TO DO: Display counts of user types
    count_user=df['User Type'].value_counts()
    print('The counts of user types are the following:\n {}'.format(count_user))  


    # TO DO: Display counts of gender
    if str(city)==str('chicago'):
        gender=df['Gender'].value_counts()
        print('\nThe counts of gender are:\n{}'.format(gender))
        early=df['Birth Year'].min()
        print('\nThe earliest year of birth is:\n{}'.format(early))
        recent=df['Birth Year'].max()
        print('\nThe most recent year of birth is:\n{}'.format(recent))
        common_birth= df['Birth Year'].mode()[0]
        print('\nThe most common year of birth is:\n{}'.format(common_birth))


        
    elif str(city)==str('new york city'):
        gender=df['Gender'].value_counts()
        print('\nThe counts of gender are:\n{}'.format(gender))  
        early=df['Birth Year'].min()
        print('\nThe earliest year of birth is:\n{}'.format(early))
        recent=df['Birth Year'].max()
        print('\nThe most recent year of birth is:\n{}'.format(recent))
        common_birth= df['Birth Year'].mode()[0]
        print('\nThe most common year of birth is:\n{}'.format(common_birth))
    print('-'*40)



    # TO DO: Display earliest, most recent, and most common year of birth


def main():
    while True:
        city, choose_month, choose_day = get_filters()
        df = load_data(city, choose_month, choose_day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
