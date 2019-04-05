#Importing pandas dataframe to manipulate our project csv files
import pandas as pd
import seaborn as sns

#For loading our csv files into the pandas dataframe for furthur manipulation
super_bowls = pd.read_csv('input/super_bowls.csv')
tv = pd.read_csv('input/tv.csv')
halftime_musicians = pd.read_csv('input/halftime_musicians.csv')

#For an overview of the loaded data
print(super_bowls.head())
print(tv.head())
print(halftime_musicians.head())

#For Looking into the dataset issues (missing values)
super_bowls.info()
tv.info()
halftime_musicians.info()

# Import matplotlib and set plotting style for visualizing our data
from matplotlib import pyplot as plt
plt.style.use('seaborn')

#Plotting the combined points column to see
super_bowls['combined_pts'].plot(kind='hist')
plt.xlabel('Combined Points')
plt.ylabel('Number of Super Bowls')
plt.savefig('output/combined_points.png')
plt.close()

# Displaying the Super Bowls with the highest and lowest combined scores
print(super_bowls[super_bowls['combined_pts'] > 70])
print(super_bowls[super_bowls['combined_pts'] < 25])

# Plotting a histogram of point differences
plt.hist(super_bowls.difference_pts)
plt.xlabel('Point Difference')
plt.ylabel('Number of Super Bowls')
plt.savefig('output/point_difference.png')
plt.close()

# Display the closest game(s) and biggest blowouts
print(super_bowls[super_bowls['difference_pts'] == 1])
print(super_bowls[super_bowls['difference_pts'] >= 35])

# Joining game and TV data, filtering out SB I because it was split over two networks
games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on='super_bowl')

# Creating a scatter plot with a linear regression model fit
#This plot will show how blowouts are effecting the TV viewership
sns.regplot(x="difference_pts" , y="share_household", data=games_tv)
plt.savefig('output/blowout_effect.png')

# The below plots will help us understand the evolution of viewers, household ratings(people watching superbowl out
#  of all TV viewers and the evolution of ad rates

# Creating a figure with 3x1 subplot and activate the top subplot
plt.subplot(3, 1, 1)
plt.plot(tv.super_bowl, tv.avg_us_viewers , color='#648FFF')
plt.title('Average Number of US Viewers')

# Activating the middle subplot
plt.subplot(3, 1, 2)
plt.plot(tv.super_bowl, tv.rating_household, color='#DC267F')
plt.title('Household Rating')

# Activating the bottom subplot
plt.subplot(3, 1, 3)
plt.plot(tv.super_bowl, tv.ad_cost, color='#FFB000')
plt.title('Ad Cost')
plt.xlabel('SUPER BOWL')

# Improving the spacing between subplots
plt.tight_layout()
plt.savefig('output/evolution.png')
plt.close()

#Printing Halftime Musicians Data.
print(halftime_musicians[halftime_musicians['super_bowl'] <= 27])

# Counting halftime show appearances for each musician and sorting them from most to least
halftime_appearances = halftime_musicians.groupby('musician').count()['super_bowl'].reset_index()
halftime_appearances = halftime_appearances.sort_values('super_bowl', ascending=False)

# Printing musicians with more than one halftime show appearance
print(halftime_appearances[halftime_appearances['super_bowl']>1])

# Filtering out most marching bands most of whom had either 'marching' or 'spirit' in name, as they have mostly nil values
no_bands = halftime_musicians[~halftime_musicians.musician.str.contains('Marching')]
no_bands = no_bands[~no_bands.musician.str.contains('Spirit')]

# Plotting a histogram of number of songs per performance
most_songs = int(max(no_bands['num_songs'].values))
plt.hist(no_bands.num_songs.dropna(), bins=most_songs)
plt.ylabel('Number of Musicians')
plt.xlabel('Number of Songs Per Halftime Show Performance')
plt.savefig('output/musicians_vs_songs.png')
plt.close()

# Sorting the non-band musicians by number of songs per appearance...
no_bands = no_bands.sort_values('num_songs', ascending=False)

# Displaying the top 15 musicians
print(no_bands.head(15))
