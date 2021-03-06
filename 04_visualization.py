"""
CLASS:  Visualization
"""

# imports
import pandas as pd
import matplotlib.pyplot as plt

# import the data available at https://raw.githubusercontent.com/justmarkham/DAT5/master/data/drinks.csv
drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/drinks.csv')

'''
Visualization
'''

# bar plot of number of countries in each continent
drinks.continent.value_counts().plot(kind='bar', title='Countries per Continent')
plt.xlabel('Continent')
plt.ylabel('Count')
plt.show()                                  # show plot window (if it doesn't automatically appear)
plt.savefig('countries_per_continent.png')  # save plot to file

# bar plot of average number of beer servings (per adult per year) by continent
drinks.groupby('continent').beer_servings.mean().plot(kind='bar', title='Average Number of Beer Servings By Continent')
plt.ylabel('Average Number of Beer Servings Per Year')
plt.show()

# histogram of beer servings (shows the distribution of a numeric column)
drinks.beer_servings.hist(bins=20)
plt.title("Distribution of Beer Servings")
plt.xlabel('Beer Servings')
plt.ylabel('Frequency')
plt.show()

# density plot of beer servings (smooth version of a histogram)
drinks.beer_servings.plot(kind='density', xlim=(0,500))
plt.title("Distribution of Beer Servings")
plt.xlabel('Beer Servings')
plt.show()

# grouped histogram of beer servings (shows the distribution for each group)
drinks.beer_servings.hist(by=drinks.continent)
plt.show()

drinks.beer_servings.hist(by=drinks.continent, sharex=True)
plt.show()

drinks.beer_servings.hist(by=drinks.continent, sharex=True, sharey=True)
plt.show()

drinks.beer_servings.hist(by=drinks.continent, sharey=True, layout=(2, 3))   # change layout (new in pandas 0.15.0)
plt.show()

# boxplot of beer servings by continent (shows five-number summary and outliers)
drinks.boxplot(column='beer_servings', by='continent')
plt.show()

# scatterplot of beer servings versus wine servings
drinks.plot(kind='scatter', x='beer_servings', y='wine_servings', alpha=0.3)
plt.show()

# same scatterplot, except point color varies by 'spirit_servings'
# note: must use 'c=drinks.spirit_servings' prior to pandas 0.15.0
drinks.plot(kind='scatter', x='beer_servings', y='wine_servings', c='spirit_servings', colormap='Blues')
plt.show()

# same scatterplot, except all European countries are colored red
colors = np.where(drinks.continent=='EU', 'r', 'b')
drinks.plot(x='beer_servings', y='wine_servings', kind='scatter', c=colors)
plt.show()

# Scatter matrix
pd.scatter_matrix(drinks)
plt.show()


##########################################
############    Exercise 1    ############
##########################################

# 1. Generate a plot showing the average number of total litres of pure alcohol
# by continent.
drinks.groupby('continent').total_litres_of_pure_alcohol.mean().plot(kind='bar')
plt.show()

# 2. Illustrate the relationship between spirit servings and total litres of 
# pure alcohol.  What kind of relationship is there?
drinks.plot(kind='scatter', x='spirit_servings', y='total_litres_of_pure_alcohol', alpha=0.4)
plt.show()

# 3. Generate one plot that shows the distribution of spirit servings for each 
# continent.
drinks.spirit_servings.hist(by=drinks.continent, sharex=True, sharey=True)
plt.show()


##########################################
#############    Homework    #############
##########################################
'''
Use the automotive mpg data (https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt) 
to complete the following parts.  Please turn in your code for each part.  
Before each code chunk, give a brief description (one line) of what the code is
doing (e.g. "Loads the data" or "Creates scatter plot of mpg and weight").  If 
the code output produces a plot or answers a question, give a brief
interpretation of the output (e.g. "This plot shows X,Y,Z" or "The mean for 
group A is higher than the mean for group B which means X,Y,Z").
'''
#loads and reads the data
auto = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt', sep='|')
auto.head

'''
Part 1
Produce a plot that compares the mean mpg for the different numbers of cylinders.
'''
#groups by number of cylinders, and bar plots the mean mpg
auto.groupby('cylinders').mpg.mean().plot(kind='bar', title='Average MPG by # of Cylinders')
plt.show()
#The mean for four cylinders is highest, and 8 is the lowest. 
'''
Part 2
Use a scatter matrix to explore relationships between different numeric variables.
'''
pd.scatter_matrix(auto)
plt.show()
#mpg increases as displacement, horsepower, and weight decrease, except for acceleration and model year, which increases with mpg
#Most cars have either 4 or 6 cylinders
#displacement increases with horsepower and wight; acceleration decreases as displacement increases
#larger displacements became lesser as time went by

'''
Part 3
Use a plot to answer the following questions:
-Do heavier or lighter cars get better mpg? 
'''
#lighter cars get better mpg

'''-How are horsepower and displacement related?'''
#the smaller the volume of cylinder (displacement), the smaller the horsepower

'''-What does the distribution of acceleration look like?'''
auto.acceleration.hist(bins=20)
plt.show()
#there is a concentration of occurances of vehicles with accelerations of 14-16, and 16-18.

'''-How is mpg spread for cars with different numbers of cylinders?'''
auto.mpg.hist(by=auto.cylinders, sharey=True, layout=(2, 3))
plt.show()
#Almost no cars with 3 or 5 cylinders, mpgs between 20-40 are typically 4 cyliderns, 15-25 are 6, and 10-15 are 8. 

'''-Do cars made before or after 1975 get better average mpg? (Hint: You need to 
create a new column that encodes whether a year is before or after 1975.)
'''
auto.columns #checks for name of columns
auto['before'] = (auto['model_year'] < 75).astype(int) #adds column that will display 1 if car comes from before 1975 and a 0 if it comes after
auto.plot(kind='scatter', x='before', y='model_year') #plot to ensure columns works
plt.show()

#create a graph that displays mean mpg for both 0 and 1 in the before column
auto.groupby('before').mpg.mean().plot(kind='bar')
plt.show() #cars with 0 have a higher avg mpg, meaning cars that come from 1975 and after have better fuel efficiency 

