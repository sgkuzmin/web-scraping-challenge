from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape():
    #initialize browser
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    #visit first url
    url='https://redplanetscience.com/#'
    browser.visit(url)
    html = browser.html
    #parse the page
    soup = bs(html, 'html.parser')

    #Scrape the Mars News Site and collect the latest News Title and Paragraph Text.
    news = soup.find_all('div', class_="list_text")
    #Assign the text to variables that you can reference later.
    news_title=news[0].find('div', class_='content_title').text
    news_p=news[0].find('div', class_='article_teaser_body').text

    #Visit the url for the Featured Space Image site
    url1="https://spaceimages-mars.com/"
    #Use splinter to navigate the site 
    browser.visit(url1)
    #Show the full resolution image by clicking a button
    browser.links.find_by_partial_text('FULL IMAGE').click()
    #find the image url 
    #for the current Featured Mars Image and assign the url 
    #string to a variable called featured_image_url.
    html = browser.html
    soup = bs(html, 'html.parser')
    featured_image_url=url1+soup.find('img', class_="fancybox-image")['src']

    #Visit the astrogeology site
    url2="https://galaxyfacts-mars.com/"

    #use Pandas to scrape the table containing facts 
    #about the planet including Diameter, Mass, etc.

    tables = pd.read_html(url2)
    #create a dataframe of Mars facts
    df_mars_facts=tables[1]
    #Use Pandas to convert the data to a HTML table string.
    html_table_mars = df_mars_facts.to_html(header=False, index=False, classes="table table-striped")

    #Visit the astrogeology site here to obtain high resolution images for 
    # each of Mar's hemispheres.
    url3="https://marshemispheres.com/"
    browser.visit(url3)

    # create empty list of dictionaries
    hemisphere_image_urls = []
    # click each of the links to the hemispheres in order to find the image url to the 
    # full resolution image
    browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced').click()
    html = browser.html
    soup = bs(html, 'html.parser')
    #full resolution image link:
    full_res_img_url=url3+soup.ul.find_all('li')[0].a['href']
    #title of the hemisphere
    hemisphere_title=soup.h2.text.rsplit(' ', 1)[0]
    #append to the list of dictionaries
    hemisphere_image_urls.append({"title": hemisphere_title, "img_url": full_res_img_url})

    #do the same for second hemisphere
    browser.visit(url3)
    browser.links.find_by_partial_text('Schiaparelli Hemisphere Enhanced').click()
    html = browser.html
    soup = bs(html, 'html.parser')
    #full resolution image link:
    full_res_img_url=url3+soup.ul.find_all('li')[0].a['href']
    #title of the hemisphere
    hemisphere_title=soup.h2.text.rsplit(' ', 1)[0]
    #append to the list of dictionaries
    hemisphere_image_urls.append({"title": hemisphere_title, "img_url": full_res_img_url})

    #do the same for third hemisphere
    browser.visit(url3)
    browser.links.find_by_partial_text('Syrtis Major Hemisphere Enhanced').click()
    html = browser.html
    soup = bs(html, 'html.parser')
    #full resolution image link:
    full_res_img_url=url3+soup.ul.find_all('li')[0].a['href']
    #title of the hemisphere
    hemisphere_title=soup.h2.text.rsplit(' ', 1)[0]
    #append to the list of dictionaries
    hemisphere_image_urls.append({"title": hemisphere_title, "img_url": full_res_img_url})

    #do the same for forth hemisphere
    browser.visit(url3)
    browser.links.find_by_partial_text('Valles Marineris Hemisphere Enhanced').click()
    html = browser.html
    soup = bs(html, 'html.parser')
    #full resolution image link:
    full_res_img_url=url3+soup.ul.find_all('li')[0].a['href']
    #title of the hemisphere
    hemisphere_title=soup.h2.text.rsplit(' ', 1)[0]
    #append to the list of dictionaries
    hemisphere_image_urls.append({"title": hemisphere_title, "img_url": full_res_img_url})

    #return one Python dictionary containing all of the scraped data
    mars_scraped={'news_title':news_title, 'news_p':news_p,'featured_image_url':featured_image_url,'html_table_mars':html_table_mars,'hemisphere_image_urls':hemisphere_image_urls}

    #quit browser
    browser.quit()




    return mars_scraped