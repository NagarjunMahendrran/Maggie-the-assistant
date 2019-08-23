import selenium as webdriver
driver = webdriver.Firefox()
url = 'google.com'
driver.get(url)
driver.find_element_by_name('query') # this works for id's, names, etc
driver.send_keys('Whatever your tryna type')
button = driver.find_element_by_name('button')
button.click()
