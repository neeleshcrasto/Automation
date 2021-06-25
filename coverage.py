
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from datetime import date
import json
import time
import fetch

# fetch.getinf()

print('Data has been entered into the JSON file. Enter and verify all details in JSON file')

proceed = input('Once completed, press Y: ')
while proceed != 'y':
    if proceed == 'y':
        break
    proceed = input('Incorrect input. Try again: ')


# Provides location of ChromeDriver and assigns variable to chromedriver
chromedriver = 'C:\\Chromed\\chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
browser = webdriver.Chrome(chromedriver, options=chrome_options)
browser.maximize_window()

# Opens the page to be automated
browser.get('https://www.jmfl.com/Sitefinity/Authenticate/SWT?realm=https%3a%2f%2fwww.jmfl.com%2f&redirect_uri=%2fsitefinity%2f&deflate=true')

# Login to the website and navigate to the page to be updated
username = browser.find_element_by_xpath('//*[@id="wrap_name"]')
password = browser.find_element_by_xpath('//*[@id="wrap_password"]')
username.send_keys('')
password.send_keys('')
browser.find_element_by_xpath('//*[@id="LoginFormControl"]/div[4]/a/strong').click()

try:
    browser.find_element_by_xpath('//*[@id="MainMenu"]')
except NoSuchElementException:
    browser.find_element_by_xpath('//*[@id="ctl04_ctl00_ctl00_ctl00_ctl00_ctl00_selfLogoutButton"]').click()


browser.find_element_by_xpath('//*[@id="MainMenu"]/ul/li[3]/a').click()
browser.find_element_by_xpath('//*[@id="MainMenu"]/ul/li[3]/div/ul/li[5]/a').click()
time.sleep(5)
# for links in find_element_by_xpath('/html/body/form/div[3]/div[2]/div[1]/div[1]/div[4]/div[3]/div[2]/table/tbody/tr'):
#     text = 
elem = browser.find_element_by_link_text("NewsCurrent")
elem.click()
# browser.find_element_by_xpath('//*[@id="lstsCntView_listsBackendList_ctl00_ctl00_itemsGrid_ctl00_ctl00_grid_ctl00__0"]/td[2]/div/span/a').click()
# /html/body/form/div[3]/div[2]/div[1]/div[1]/div[4]/div[3]/div[2]/table/tbody/tr

with open('C:\\Users\\ncrasto\\Desktop\\SiteFinUpload\\rawdata.json', 'r') as readfile:
    data = json.load(readfile)
    hour = 13
    for p in data["list"]:

        # browser.find_element_by_xpath('//*[@id="MainMenu"]/ul/li[3]/a').click()
        # browser.find_element_by_xpath('//*[@id="MainMenu"]/ul/li[3]/div/ul/li[4]/a').click()
        # time.sleep(5)
        # browser.find_element_by_xpath('//*[@id="lstsCntView_listsBackendList_ctl00_ctl00_itemsGrid_ctl00_ctl00_grid_ctl00__0"]/td[2]/div/span/a').click()
        # browser.get('https://jmfl.com/Sitefinity/Content/Lists/ListItems/newscurrent/?provider=OpenAccessDataProvider')

        browser.switch_to.default_content()
        browser.implicitly_wait(60)
        browser.find_element_by_xpath('//*[@id="lstItmsCntView_itemsBackendList_ctl00_ctl00_toolbar_createItemWidget_ctl00_ctl00_buttonText"]').click()

        iframe = browser.find_element_by_xpath('//*[@id="RadWindowWrapper_lstItmsCntView_itemsBackendList_ctl00_ctl00_itemsTreeTable_ctl00_ctl00_createItem"]/table/tbody/tr[2]/td[2]/iframe')
        browser.switch_to.frame(iframe)

        # Input Form has opened, below code inserts content into the form
        time.sleep(15)
        title = browser.find_element_by_xpath('//*[@id="contentViewInsertDialog_ctl00_ctl00_contentView_listsBackendInsertItem_ctl00_ctl00_sections_mainSection_0_ctl00_0_ctl00_0_fields_0_titleField_0_ctl00_0_ctl00_0_textBox_write_0"]')
        title.send_keys(p['title'])
        title2 = browser.find_element_by_xpath('//*[@id="contentViewInsertDialog_ctl00_ctl00_contentView_listsBackendInsertItem_ctl00_ctl00_sections_customFieldsSection_3_ctl00_3_ctl00_3_fields_3_ctl00_7_ctl00_7_ctl00_7_textBox_write_7"]')
        title2.send_keys(p['title'])
        ## Toggles the HTML and Design in the Content 2 field
        browser.find_element_by_xpath('//*[@id="contentViewInsertDialog_ctl00_ctl00_contentView_listsBackendInsertItem_ctl00_ctl00_sections_ctl03_customFieldsSection_ctl00_ctl00_fields_ctl01_ctl00_ctl00_ctl00_editControl_ModesWrapper"]/ul/li[2]/a/span').click()
        browser.find_element_by_xpath('//*[@id="contentViewInsertDialog_ctl00_ctl00_contentView_listsBackendInsertItem_ctl00_ctl00_sections_ctl03_customFieldsSection_ctl00_ctl00_fields_ctl01_ctl00_ctl00_ctl00_editControl_ModesWrapper"]/ul/li[1]/a/span').click()
        browser.find_element_by_xpath('//*[@id="contentViewInsertDialog_ctl00_ctl00_contentView_listsBackendInsertItem_ctl00_ctl00_sections_ctl03_customFieldsSection_ctl00_ctl00_fields_ctl01_ctl00_ctl00_ctl00_editControlTop"]/div/ul[1]/li[2]/a/span').click()
        browser.find_element_by_xpath('//*[@id="contentViewInsertDialog_ctl00_ctl00_contentView_listsBackendInsertItem_ctl00_ctl00_sections_ctl03_customFieldsSection_ctl00_ctl00_fields_ctl01_ctl00_ctl00_ctl00_editControlTop"]/div/ul[3]/li[4]/a/span').click()

        # Switch to upload iframe window and upload file
        iframe_upld = browser.find_element_by_xpath('//*[@id="RadWindowWrapper_contentViewInsertDialog_ctl00_ctl00_contentView_listsBackendInsertItem_ctl00_ctl00_sections_ctl03_customFieldsSection_ctl00_ctl00_fields_ctl01_ctl00_ctl00_ctl00_editControl_dialogOpenerEXTERNAL_URLdefault"]/table/tbody/tr[2]/td[2]/iframe')
        browser.switch_to.frame(iframe_upld)
        upload = browser.find_element_by_xpath('//*[@id="mediaContentManagerDialog_ctl00_ctl00_contentSelectorView_ctl00_ctl00_imageSelector_ctl00_ctl00_uploaderView_ctl00_ctl00_fileUpload_ctl00_ctl00_uploadInput"]')
        upload.send_keys("C:\\Users\\ncrasto\\Desktop\\SiteFinUpload\\",p['filename'])
        browser.find_element_by_xpath('//*[@id="mediaContentManagerDialog_ctl00_ctl00_contentSelectorView_ctl00_ctl00_imageSelector_ctl00_ctl00_saveLinkTitle"]').click()
        browser.find_element_by_xpath('//*[@id="mediaContentManagerDialog_ctl00_ctl00_saveLinkTitle"]').click()

        browser.switch_to.default_content()
        iframe = browser.find_element_by_xpath('//*[@id="RadWindowWrapper_lstItmsCntView_itemsBackendList_ctl00_ctl00_itemsTreeTable_ctl00_ctl00_createItem"]/table/tbody/tr[2]/td[2]/iframe')
        browser.switch_to.frame(iframe)
        iframe_embed = browser.find_element_by_xpath('//*[@id="contentViewInsertDialog_ctl00_ctl00_contentView_listsBackendInsertItem_ctl00_ctl00_sections_ctl03_customFieldsSection_ctl00_ctl00_fields_ctl01_ctl00_ctl00_ctl00_editControl_contentIframe"]')
        browser.switch_to.frame(iframe_embed)
        embed = browser.find_element_by_xpath('/html/body/a')
        url = str(embed.get_attribute('href'))

        browser.switch_to.default_content()
        iframe = browser.find_element_by_xpath('//*[@id="RadWindowWrapper_lstItmsCntView_itemsBackendList_ctl00_ctl00_itemsTreeTable_ctl00_ctl00_createItem"]/table/tbody/tr[2]/td[2]/iframe')
        browser.switch_to.frame(iframe)
        browser.find_element_by_xpath('//*[@id="contentViewInsertDialog_ctl00_ctl00_contentView_listsBackendInsertItem_ctl00_ctl00_sections_ctl03_customFieldsSection_ctl00_ctl00_fields_ctl01_ctl00_ctl00_ctl00_editControl_ModesWrapper"]/ul/li[2]/a/span').click()
        embed_w = browser.find_element_by_xpath('//*[@id="contentViewInsertDialog_ctl00_ctl00_contentView_listsBackendInsertItem_ctl00_ctl00_sections_ctl03_customFieldsSection_ctl00_ctl00_fields_ctl01_ctl00_ctl00_ctl00_editControlCenter"]/textarea[2]')
        embed_w.clear()
        new_url = '<object internalinstanceid="7" data="'+url+'" width="1000" height="1000"></object>'
        embed_w.send_keys(new_url)

        # Other fields like URL number, Date, Place, Priority
        browser.switch_to.default_content()
        iframe = browser.find_element_by_xpath('//*[@id="RadWindowWrapper_lstItmsCntView_itemsBackendList_ctl00_ctl00_itemsTreeTable_ctl00_ctl00_createItem"]/table/tbody/tr[2]/td[2]/iframe')
        browser.switch_to.frame(iframe)
        iframe_no = browser.find_element_by_xpath('//*[@id="contentViewInsertDialog_ctl00_ctl00_contentView_listsBackendInsertItem_ctl00_ctl00_sections_ctl03_customFieldsSection_ctl00_ctl00_fields_ctl06_ctl00_ctl00_ctl00_editControl_contentIframe"]')
        browser.switch_to.frame(iframe_no)
        url_no = browser.find_element_by_xpath('/html/body')
        url_no.send_keys(p['urlno'])

        browser.switch_to.default_content()
        iframe = browser.find_element_by_xpath('//*[@id="RadWindowWrapper_lstItmsCntView_itemsBackendList_ctl00_ctl00_itemsTreeTable_ctl00_ctl00_createItem"]/table/tbody/tr[2]/td[2]/iframe')
        browser.switch_to.frame(iframe)

        # dt = date.today()
        # dt_str = dt.strftime('%m/%d/%Y')
        date_field = browser.find_element_by_xpath('//*[@id="contentViewInsertDialog_ctl00_ctl00_contentView_listsBackendInsertItem_ctl00_ctl00_sections_customFieldsSection_3_ctl00_3_ctl00_3_fields_3_ctl00_1_ctl00_1_ctl00_1_datePicker_1"]')        
        date_field.send_keys(p['datetime'])
        # hour = hour + 1
        browser.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div[3]/button[2]').click()
        place = browser.find_element_by_xpath('//*[@id="contentViewInsertDialog_ctl00_ctl00_contentView_listsBackendInsertItem_ctl00_ctl00_sections_customFieldsSection_3_ctl00_3_ctl00_3_fields_3_ctl00_2_ctl00_2_ctl00_2_textBox_write_2"]')
        place.send_keys(p['place'])
        priority = browser.find_element_by_xpath('//*[@id="contentViewInsertDialog_ctl00_ctl00_contentView_listsBackendInsertItem_ctl00_ctl00_sections_customFieldsSection_3_ctl00_3_ctl00_3_fields_3_ctl00_4_ctl00_4_ctl00_4_textBox_write_4"]')
        priority.send_keys('1')

        # Publish the thing finally
        browser.find_element_by_xpath('//*[@id="contentViewInsertDialog_ctl00_ctl00_contentView_listsBackendInsertItem_ctl00_ctl00_ctl01_ctl00_ctl00_actionsContainer_Publish"]/span').click()
        browser.implicitly_wait(360)
        time.sleep(200)
        # browser.switch_to.default_content()
        # element = browser.find_element_by_xpath('//*[@id="TC79564B7002_ctl00_ctl00_logoutButton"]')
        # browser.execute_script("arguments[0].click();", element)
        
# #browser.quit()
