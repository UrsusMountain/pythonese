from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

capabilities = webdriver.DesiredCapabilities().FIREFOX
capabilities["marionette"] = True
binary=FirefoxBinary(r'/Applications/Firefox.app/Contents/MacOS/firefox')
driver=webdriver.Firefox(firefox_binary=binary,capabilities=capabilities)
url='http://www.baidu.com'
driver.get(url)
search_box=driver.find_element_by_name('wd') #or search_box=driver.find_element_by_name('kw)
search_box.send_keys('ChromeDriver')
search_box.submit()

'''import time
from selenium import webdriver

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()'''

