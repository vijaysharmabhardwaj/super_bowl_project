SUPERBOWL DATA ANALYSIS

1.Folder Structure
Input  : Contains the 3 csv files i.e super_bowls, tv and halftime_musicians.
Output : Contains the charts (5) which were generated during the data analysis of csv files
Scripts: Contains 1 script named project_script.py used
Project_screen_shots: Contains the 13 screen shots of rendered data

2.i Editor Used : Pycharm with python 3.6 environment setup
2.ii Packages Used : pandas, matplotlib, seaborn

3.Project Description: The Super Bowl is the annual championship game of the National Football League (NFL)
 where the champion of the National Football Conference (NFC) competes against the champion of the American 
Football Conference (AFC).

4.The Aim of the project is to analyse the game data along with the tv and halftime_musicians data to answer the
questions such as:-

i)How combined points in the matches(scores of both teams) are distributed across number of superbowl matches
(see output/combined_points.png)
 
ii)How difference in points between the two teams in matches are distributed across number of superbowl matches
(see output/point_difference.png)

iii)Do blowouts(matches having huge difference between the points) affect the TV viewership? 
(see output/blowout_effect.png)

iv)How average US viewers, household ratings (people watching superbowl out of total people having a TV) and
ad rates have evolved over time.
(see output/evolution.png)

v)What is the distribution of number of songs per halftime show performance across all the musicians.
(see output/musicians_vs_songs.png)

5.Conclusion: After the analysis of 3 csv files successfully using our python script, we were able to conclude 
that 40-50 was the most common score across all superbowl games, the blowouts resulted in decreased viewership,
rates of ad for the superbowl increased rapidly and faster than that of increasing viewers or household ratings
(% of superbowl viewers out of people owning a tv) and most of the musicians only got 2 songs.


NOTE: load the csv files in the same directory where you are working on the project or update the paths in scripts
read_csv functions.