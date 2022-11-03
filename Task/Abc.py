from selenium import webdriver

from selenium .webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select

import time



browser = webdriver.Firefox(executable_path = 'E:\seleniumDriver\geckodriver.exe')

browser.get('http://automationpractice.com/index.php')



browser.find_element_by_class_name('login').click()



time.sleep(5)



browser.find_element_by_id('email_create').send_keys('tamilgd@gmail.com')



time.sleep(5)



browser.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/div[1]/form/div/div[3]/button/span').click()



time.sleep(5)



Mr_radio_button = browser.find_element_by_id('id_gender1')

Mr_radio_button.click()



browser.find_element_by_id('customer_firstname').send_keys('Tamil')



browser.find_element_by_id('customer_lastname').send_keys('Maran')



browser.find_element_by_id('passwd').send_keys('helloworld')



time.sleep(5)



dropdown_element = browser.find_element_by_id('days')

dropdown_object = Select(dropdown_element)

dropdown_object.select_by_index("6")



dropdown_element1 = browser.find_element_by_id('months')

dropdown_object1 = Select(dropdown_element1)

dropdown_object1.select_by_index("7")



dropdown_element2 = browser.find_element_by_id('years')

dropdown_object2 = Select(dropdown_element2)

dropdown_object2.select_by_index("23")



time.sleep(2)



browser.find_element_by_id('company').send_keys("L&T")



time.sleep(2)

browser.find_element_by_id('address1').send_keys("No.45 , North street , Orathanadu")



time.sleep(2)

browser.find_element_by_id('city').send_keys("Thanjavur")



time.sleep(2)

dropdown_element3 = browser.find_element_by_id('id_state')

dropdown_object3 = Select(dropdown_element3)

dropdown_object3.select_by_visible_text("Florida")



time.sleep(2)

browser.find_element_by_id('postcode').send_keys("60028")



time.sleep(2)

dropdown_element4 = browser.find_element_by_id('id_country')

dropdown_object4 = Select(dropdown_element4)

dropdown_object4.select_by_visible_text("United States")



time.sleep(1)

browser.find_element_by_id('other').send_keys("9568423813")



time.sleep(1)

browser.find_element_by_id('phone').send_keys("245")



browser.find_element_by_id('phone_mobile').send_keys("7695423846")



browser.find_element_by_id('alias').send_keys("No.22 , Gandhi Nagar")



time.sleep(2)

browser.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div[4]/button/span').click()
