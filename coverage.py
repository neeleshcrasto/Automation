
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import json
import time

# Provides location of ChromeDriver and assigns variable to chromedriver
chromedriver = 'C:\Chromed\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
browser.maximize_window()

# Opens the page to be automated
browser.get('https://jmfl.com/Sitefinity/Authenticate/SWT?realm=https%3a%2f%2fjmfl.com%2f&redirect_uri=%2fSitefinity&deflate=true')

# Login to the website and navigate to the page to be updated
username = browser.find_element_by_xpath('//*[@id="wrap_name"]')
password = browser.find_element_by_xpath('//*[@id="wrap_password"]')
username.send_keys('Neelesh')
password.send_keys('Neelesh@2018')
browser.find_element_by_xpath('//*[@id="LoginFormControl"]/div[4]/a/strong').click()

with open('C:\\Users\\ncrasto\\Desktop\\SiteFinUpload\\rawdata.json', 'r') as readfile:
    data = json.load(readfile)
    hour = 13
    for p in data["list"]:

        browser.get('https://jmfl.com/Sitefinity/Content/Lists/ListItems/newscurrent/?provider=OpenAccessDataProvider')

        browser.implicitly_wait(120)
        browser.find_element_by_xpath('//*[@id="lstItmsCntView_itemsBackendList_ctl00_ctl00_toolbar_createItemWidget_ctl00_ctl00_buttonText"]').click()

        iframe = browser.find_element_by_xpath('//*[@id="RadWindowWrapper_lstItmsCntView_itemsBackendList_ctl00_ctl00_itemsTreeTable_ctl00_ctl00_createItem"]/table/tbody/tr[2]/td[2]/iframe')
        browser.switch_to.frame(iframe)

        # Input Form has opened, below code inserts content into the form
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

        dt = date.today()
        dt_str = dt.strftime('%m/%d/%Y')
        date_field = browser.find_element_by_xpath('//*[@id="contentViewInsertDialog_ctl00_ctl00_contentView_listsBackendInsertItem_ctl00_ctl00_sections_customFieldsSection_3_ctl00_3_ctl00_3_fields_3_ctl00_1_ctl00_1_ctl00_1_datePicker_1"]')        
        date_field.send_keys(dt_str," ",hour,":20")
        hour = hour + 1
        browser.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div[3]/button[2]').click()
        place = browser.find_element_by_xpath('//*[@id="contentViewInsertDialog_ctl00_ctl00_contentView_listsBackendInsertItem_ctl00_ctl00_sections_customFieldsSection_3_ctl00_3_ctl00_3_fields_3_ctl00_2_ctl00_2_ctl00_2_textBox_write_2"]')
        place.send_keys(p['place'])
        priority = browser.find_element_by_xpath('//*[@id="contentViewInsertDialog_ctl00_ctl00_contentView_listsBackendInsertItem_ctl00_ctl00_sections_customFieldsSection_3_ctl00_3_ctl00_3_fields_3_ctl00_4_ctl00_4_ctl00_4_textBox_write_4"]')
        priority.send_keys('1')

        # Publish the thing finally
        browser.find_element_by_xpath('//*[@id="contentViewInsertDialog_ctl00_ctl00_contentView_listsBackendInsertItem_ctl00_ctl00_ctl01_ctl00_ctl00_actionsContainer_Publish"]/span').click()
        browser.implicitly_wait(360)
        time.sleep(360)
        # browser.switch_to.default_content()
        # element = browser.find_element_by_xpath('//*[@id="TC79564B7002_ctl00_ctl00_logoutButton"]')
        # browser.execute_script("arguments[0].click();", element)
        
#browser.quit()

        





