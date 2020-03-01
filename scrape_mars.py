# Dependencies
import os
from bs4 import BeautifulSoup
from splinter.browser import Browser
import pandas as pd
import requests
import html5lib 

def init_browser():
    executable_path = {"executable_path": "C:/Program Files/chromedriver_win32/chromedriver.exe"}
    return Browser("chrome", **executable_path,headless= False)

def scrape():
    # create a python dictionary to store all the data 
    scrape_dict = {}

    #Scrape nasa news
    nasa_url = 'https://mars.nasa.gov/news/'
    response = requests.get(nasa_url)
    nasa_soup = BeautifulSoup(response.text, 'html.parser')
    # Parse HTML with Beautiful Soup

    news_title = nasa_soup.find('div',class_ ="content_title").find('a').text
    print(news_title)

    p_results= nasa_soup.find_all("div", class_="rollover_description_inner")
    news_p = p_results[0].text.strip()
    print(news_p)

    # store into python dictionary
    scrape_dict['news_title']=news_title
    scrape_dict['news_p']=news_p 
    
    # Scrape JPL Mars Space Images
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    response = requests.get(jpl_url)
    # Parse HTML with Beautiful Soup
    jpl_soup = BeautifulSoup(response.text, 'html.parser')

    featured = jpl_soup.find('div',class_ ="default floating_text_area ms-layer")
    featured_image = featured.find('footer')
    featured_image_url = 'https://www.jpl.nasa.gov'+ featured_image.find('a')['data-fancybox-href']
    print(str(featured_image_url))
    
    # store into python dictionary
    scrape_dict['featured_image_url']=featured_image_url

    # Scrape Mars Weather
    weather_url = "https://twitter.com/marswxreport?lang=en"
    response = requests.get(weather_url)
    # Parse HTML with Beautiful Soup
    weather_soup = BeautifulSoup(response.text, 'lxml')

    tweets = weather_soup.find('div',class_ ="js-tweet-text-container")
    mars_weather = tweets.find('p',class_="js-tweet-text").text
    mars_weather
    # store into python dictionary
    scrape_dict['mars_weather']=mars_weather

    # Scrape Mars Facts
    facts_url = "https://space-facts.com/mars/"
    mars_facts = pd.read_html(facts_url)
    mars_facts
    mars_df = mars_facts[0]
    mars_df.columns = ['Description','Value']
    mars_df
    mars_df.set_index("Description")

    # store into python dictionary
    scrape_dict['mars_df']=mars_df

    # Scrape Mars Hemispheres
    return scrape_dict 