# Space-Vehicle-Stimulator
Submitted By: Garvita Srivastava (25BAS10034)

## Project Introduction 
This project is about space vehicle simulations and majorly works on two function which are rocket launch trajectory and satellite telemetry. The objective is to combine fundamental principles of physics with modern data processing and visualization techniques to create an interactive and educational simulation. In general, the project shows how physics, programming, and data visualization can work together to make real-world aerospace systems easier to understand and use.

 ## Key Features 

 1. **Module 1 (Rocket Trajectory Simulator):** This modules takes in basic values of mass of rocket and thrust value on the rocket and then calculates acceleration. Furthermore it gives the value of velocity with respect to the altitude including the timestamp.
 2. **Module 2 (Satellite Telemetry):** This modules stores the data like voltage, temperature, altitude, velocity, radiation received from the satellite. It also gives error if the temperature of the satellite exceeds a certain limit. This module also plots the graph between temperature and time as well as voltage and time.


## Technologies Used 

1. **Database:** Both the modules take the data from the user and then store it in database which can help us keep track of the data which has been obtained from previous runs.
2. **Python Libraries:**
- *Matplotlib:* This library has been used in satellite telemetry in order to plot graphs between temperature and time as well as between voltage and time.
- *Random:* Since we don't have access to real life data which would be obtained from satellities so this library is used to generate fictious data parameters for variables like voltage, temperature, altitude, velocity, radiation. In order to keep the values realistic we have defined suitable range for each parameter.
- *SQLite:* This library is used to create databases.


## Steps to Install
- Upon accessing the repository link you have to download the files first.
- The files will get downloaded in the form of zip folder. Unzip it and then open it in any platform which supports python.
- Now when you run the program you will first be shown a menu, from there you can choose whatever function you want to run.
- Enter the inputs whatever ased for and the program runs.

## Important Points to Look Out For
- You must make sure that the patform is python friendly.
- Must make sure that all the libraries which are mentioned must be installed so that the program runs without any error.
- Must mae sure that the extension for database creation is also installed.
  
