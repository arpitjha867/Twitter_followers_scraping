# I have tried beautifulsoup but was not working on the twitter site so I am using selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
# setup webdriver
driver=webdriver.Firefox(executable_path='./geckodriver')
# we have to wait for 10 seconds as the web page do not load right away
driver.implicitly_wait(10)
# we will access the twitter 
handle=str(input("Please Enter the Twitter username :"))
full_path="https://twitter.com/"+handle
driver.get(full_path)
''' now we need to scrape the data from the page 
the problem is that twitter make randomised class names that so we cannot use any of these to get to our number of followers 
so we will see for something that is constant on the web page like the 'a' tag with the href attribute that will not change
after that we can see in the inspect element feature of the web browser that within span there is another span and in that 
 we have our required data'''
followers=driver.find_element_by_css_selector('a[href="/{handle_str}/followers"] > span > span'.format(handle_str=handle)).text
print(followers)