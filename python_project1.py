import http.client
import json
import datetime
from pytz import timezone
import requests
from bs4 import BeautifulSoup
from os import system
import json
import math
import os
from dotenv import load_dotenv

load_dotenv()

cls = lambda: system('cls')
cls()

OPENAPIKEY = os.getenv('OPENAPI_KEY')


def movie_finder():
    dTitle1 = "Not Found"
    dPoster1 = "Not Found"
    dStars1 = "Not Found"
    dYear1 = "Not Found"

    conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': OPENAPIKEY,
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    m_string = input('\nEnter a movie you would like to search for.  ')

    if " " in m_string:
        m_string = m_string.replace(" ", "_")

    conn.request("GET", "/auto-complete?q={}".format(m_string), headers=headers)

    res = conn.getresponse()
    data = res.read()
    dataJson = json.loads(data)

    try:
        dTitle1 = dataJson["d"][0]["l"]
        dPoster1 = dataJson["d"][0]["i"]["imageUrl"]
        dStars1 = dataJson["d"][0]["s"]
        last_char_index = dStars1.rfind(",")
        dStars1 = dStars1[:last_char_index] + " and" + dStars1[last_char_index+1:]
        dYear1 = dataJson["d"][0]["y"]
    except KeyError:
        print("\nEntering nothing results in the first occurance in IMDB's database being retrieved.")



    if dTitle1 == "Not Found":
        if "_" in m_string:
            m_string = m_string.replace("_", " ")
        print(" ")
        print('"{}" not found in IMDB API database.'.format(m_string))
    else:
        print(" ")
        print("\nTitle: {}".format(dTitle1))
        print("Movie Image URL: {}".format(dPoster1))
        print("Stars: {}".format(dStars1))
        print("Year Released: {}".format(dYear1))
        print(" ")


def holiday():
    conn = http.client.HTTPSConnection("public-holiday.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': OPENAPIKEY,
        'x-rapidapi-host': "public-holiday.p.rapidapi.com"
        }

    tz = timezone('EST')

    fnow = datetime.datetime.now(tz).year

    fconn = "/{}/US".format(fnow)

    conn.request("GET", fconn, headers=headers)

    res = conn.getresponse()
    data = res.read()

    data2 = json.loads(data)


    i = 0
    while i < len(data2):
        if datetime.datetime.now(tz) < datetime.datetime.strptime(data2[i]["date"], "%Y-%m-%d").replace(tzinfo=timezone('EST')):
            t_diff = datetime.datetime.strptime(data2[i]["date"], "%Y-%m-%d").replace(tzinfo=timezone('EST')) - datetime.datetime.now(tz)
            print("\nThe next holiday is {}.\nThe party starts in {} days!".format(data2[i]["name"], t_diff.days))
            break
        i += 1


def property_search():
    os.system('cls')

    class Property:
        def __init__(self, prop_image, address, owner, prop_type, parcel_ID):
            self.prop_image = prop_image
            self.address = address
            self.owner = owner
            self.prop_type = prop_type
            self.parcel_ID = parcel_ID


    print("\n")

    prop_list = []

    page_num = 1

    address = input("What street would you like to search? ")

    address = address.replace(".", "")


    print("\n")

    try:
        r = requests.get("https://jeffersonpva.ky.gov/property-search/property-listings/?order=ASC&sort=street&psfldAddress={}&searchType=StreetSearch&searchPage={}#results".format(address, page_num), headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
        c=r.content
        soup=BeautifulSoup(c, "html.parser")
        all=soup.find_all("td")


        records_found = soup.find("h1", {"id": "results"}).find_next("h3")

        num_str = records_found.text.split()[0]

        print(num_str + " Records Found")

        num_int = int(num_str)

        total_pages = math.ceil(num_int / 25)

        j = 0


        while j < total_pages:

            r = requests.get("https://jeffersonpva.ky.gov/property-search/property-listings/?order=ASC&sort=street&psfldAddress={}&searchType=StreetSearch&searchPage={}#results".format(address, page_num), headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
            c=r.content
            soup=BeautifulSoup(c, "html.parser")
            all=soup.find_all("td")



            for span_tag in soup.findAll("span"):
                span_tag.replace_with("")

            prop_num = 1


            for i in range(0, len(all), 5):

                prop1 = Property(all[i].text, all[i+1].text, all[i+2].text, all[i+3].text, all[i+4].text)
                jprop1 = json.dumps(prop1.__dict__)
                print("\nOwner:       " + prop1.owner)
                print("Address:     " + prop1.address)
                print("Prop. Type:  " + prop1.prop_type)
                print("Parcel ID:   " + prop1.parcel_ID)
                prop_list.append([jprop1])

            page_num += 1
            j += 1

    except AttributeError:
        print("Oppps. Something went wrong.")

    print("\n")

    # print(prop_list)



while True:

    print('\nFor Movie Info Enter "1"\nFor Upcoming Holiday Counter Enter "2"\nFor Jefferson County Street Property Search enter "3"\nTo Quit Enter "Q"')
    command = input('\nPlease Enter A Selection:  ')
    if command == "1":
        try:
            movie_finder()
        except ValueError:
            print("\nSorry. You must enter a value.")
    elif command == "2":
        holiday()
    elif command == "3":
        property_search()
    elif command == "Q" or command == "q":
        print("\n")
        break
    else:
        print("\nSorry. You must enter a valid option.")