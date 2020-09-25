from splinter import Browser
from bs4 import BeautifulSoup
# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def echo():
    return render_template("index.html", text="Mission to Mars server!!")

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver

    # MAC Users:
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

    # Windows Users:
    # executable_path = {'executable_path': 'chromedriver.exe'}
    # browser = Browser('chrome', **executable_path, headless=False)

# Store return values as a Python dictionary
mars_info{}

# NASA Mars News
def scrape_mars_news():
    browser = init_browser()

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Extract the latest News Title and Paragraph 
    news_title = soup.find('div', class_='bottom_gradient').text
    news_p = soup.find('div', class_='article_teaser_body').text


# JPL Featured Space Image
def scrape_mars_news():
    browser = init_browser()

    # Use Splinter to navigate the following site and find the image
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)

    html_img = browser.html
    soup = BeautifulSoup(html_img, "html.parser")

    # Website Url 
    webs_url = 'https://www.jpl.nasa.gov'

    # Retrieve background-image from style tag 
    back_img  = soup.find('article')['style']
    back_img    

# NASA Mars Facts
def scrape_mars_facts():
    browser = init_browser()

    facts_url = 'https://space-facts.com/mars/'
    browser.visit(facts_url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Mars Facts Table
    f_table = pd.read_html(facts_url)
    df = f_table[0] 
    df.columns = ['Mars Planet', 'Value']
    df.set_index(['Mars Planet'], inplace = True)
    df.to_html('Mars_df.html'   

 # Mars Hemispheres
def scrape_mars_astro():
    browser = init_browser()

    astro_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(astro_url)

    html_astro = browser.html
    soup = BeautifulSoup(html_astro, 'html.parser')

    # Retreive all items that contain Mars hemispheres information
    items = soup.find_all('div', class_='item')

    # Retrieve images
         

    return mars_info


if __name__ == "__main__":
    app.run(debug=True)