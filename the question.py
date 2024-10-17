# To mark World Health Day, the school organized a week-long campaign called "Move!"
# Each participant of the campaign had to register online,
# indicating their class category and step length, and then enter the number of steps taken each day of the week.
# Write a program that lists the distance traveled by all students
# in each class category who participated in the event.
# Initial data:
# The data is presented in the text file U1.txt.
# The first line contains the number of students who participated in the campaign m (10 ≤ m ≤ 50).
# The following lines contain the data of the students who participated in the campaign
# : class ID (number from 1 to 12); step length in centimeters;
# the number of steps taken each day of the campaign week.
# If the student did not enter the number of steps taken on a certain day of the week,
# the value 0 is given. The data is separated by one space character.
# There was at least one student who entered the number of steps taken each day of the campaign week.
# Results
# Submit the results in the text file U1rez.txt.
# A list of the total distance traveled by students of each class category is printed: class ID;
# how many students entered the number of steps taken each day of the campaign week;
# the total distance traveled in kilometers for the specified class category, rounded to the nearest hundredth.
# If the participant did not enter the number of steps taken for at least one day,
# his data are not used for calculations.
# Data is separated by a single space character.
# One row contains the data of one class category.
# If there was no student in any class category who
# entered the number of steps taken on each day of the promotion week,
# then data for this class category does not need to be submitted.
# The list by class category is in the order in which they were listed in the source data file.
# Instructions
# Create and write one function that calculates the total distance traveled in kilometers
# for each class category and counts how many students
# in that class category have entered the number of steps taken each day of the campaign week.
