# pythonMovieFinder
Code Louisville Project

Project currently meets the following Python Project requirements:


1.  Project is uploaded to your GitHub repository and shows at minimum 5 separate commits

2.  Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program
    -App has a main console that provides access to various functions

3.  Connect to an external/3rd party API and read data into your app
    -movie_finder function connects to IMDB's API and reads data returned in response to movie search criteria
    -holiday function connects to Public Holiday API and uses date

4.  Calculate and display data based on an external factor (ex: get the current date, and display how many days remaining until some event)
    -holiday function gets the next holiday's date from Holiday API and subtracts current date to return days remaining until that holiday

5.  Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program
    -propery_search function scrapes data from Jefferson County PVA webiste and compiles an array of objects that is then converted to a json and appended to an array

6.  Connect to an external/3rd party API and read data into your app
    -both movie_finder and holiday functions connect to external APIs

7.  Create a class, then create at least one object of that class and populate it with data. The value of at least one object must be used somewhere in your code
    -in proerty_search function a class ("Property") is instantiated and then the instances of Property objects are instantiated by iterating through a for loop

8.  Implement a “scraper” that can be fed a type of file or URL and pull information off of it. 
    -property_search function inputs a street name and then scrapes owner, address, property details and parcel ID data from the Jefferson County PVA
     website and displays them in a listing