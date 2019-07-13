from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1.0'
desired_caps['deviceName'] = 'Samsung SM-N960U1'
desired_caps['appPackage'] = 'com.narvii.amino.master.dev'
desired_caps['appActivity'] = 'com.narvii.master.MasterActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
listview=driver.find_element_by_id('android:id/list')
listview.find_element_by_id('com.narvii.amino.master.dev:id/image').click()
#driver.find_element_by_id('com.android.dialer:id/search_box_collapsed').click()
#search_box = driver.find_element_by_id('com.android.dialer:id/search_view')
#search_box.click()
#search_box.send_keys('hello toby')