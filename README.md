# python_project1
Code Louisville Project


To run this code:

1. Install Python from https://www.python.org/downloads/ for your specific environment

2. The movie search and holiday functions use an api key that is not included in the dotenv file to prevent them from being accessable
   publicly. You can get your own keys at https://rapidapi.com/ or I can provide them to you upon request

3. Enter 'pip install -r, requirements.txt' at the command prompt

4. Enter 'python python_project1.py' at the command prompt to run the program


Project currently meets the following Python Project requirements:

1.  Project is uploaded to your GitHub repository and shows at minimum 5 separate commits

2.  Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program
    -App has a main console that provides access to various functions

3.  Connect to an external/3rd party API and read data into your app
    -movie_finder function connects to IMDB's API and reads data returned in response to movie search criteria
    -holiday function connects to Public Holiday API and uses date and holiday local name from the response

4.  Calculate and display data based on an external factor (ex: get the current date, and display how many days remaining until some event)
    -holiday function gets the next holiday's date from Holiday API and subtracts current date to return days remaining until that holiday

5.  Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program
    -propery_search function scrapes data from Jefferson County PVA webiste and appends it, adding the data from webscraping as it iterates

6.  Connect to an external/3rd party API and read data into your app
    -both movie_finder and holiday functions connect to external APIs

7.  Implement a “scraper” that can be fed a type of file or URL and pull information off of it. 
    -property_search function inputs a street name and then scrapes owner, address, property details, parcel ID, neighborhood and assessed property value data from the Jefferson County PVA
     website, displays them in a listing and creates a csv file containing the results