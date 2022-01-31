#!/usr/bin/env python
# coding: utf-8

# In[52]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[17]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ## Scraping articles from NASA's Mars Exploration Program website

# In[18]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[19]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[24]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[25]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# In[27]:


# Use the parent element to find the paragraph text
for p in slide_elem.find_all('div', class_='article_teaser_body'):
    print(p.get_text())


# ## Scraping images from Jet Propulsion Laboratory's website

# In[44]:


# Visit URL
url = 'https://spaceimages-mars.com/'
browser.visit(url)


# In[45]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[46]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[47]:


img_soup


# In[48]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[49]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
#img_url = url + img_url_rel # this is another option
img_url


# ## Scraping Mars facts from Galaxy Facts website

# In[ ]:


url = 'https://galaxyfacts-mars.com/'


# In[53]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[55]:


df.to_html()


# In[56]:


browser.quit()


# In[ ]:




