from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
import re

# This program auto bids on select fifa items
email = 'email@email.com'
password = 'PASSWORD1234'

url = 'https://www.easports.com/fifa/ultimate-team/web-app/'
driver = webdriver.Chrome('PATHTOCHROMEDRIVER')


url2 = 'https://www.gmail.com' # or user email account
driver2 = webdriver.Chrome('PATHTOCHROMEDRIVER')

def main():
    webAppLogin(email,password)
    tranferTab()
    # consumablesINTRANSFERTAB()
    # makeBids()


# starts logging into web app
def webAppLogin(email,password):
    # waits for webapp to load and begins logging in
    successbool = True
    while successbool:
        print('Loading web app...')
        driver.get(url)
        driver.set_window_size(1000, 1000)
        time.sleep(8)
        print('Entering account info...')
        driver.find_element_by_xpath('//*[contains(@class,"standard call-to-action")]').click()
        driver.find_element_by_id('email').send_keys(email)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_id('btnLogin').click()
        time.sleep(3)
        driver.find_element_by_id('btnSendCode').click()
        print('Sending verification code')

# opens email to recieve verification code

        print('Opening email...')
        driver2.get(url2)
        time.sleep(2)
        driver2.find_element_by_id('identifierId').send_keys(email)
        driver2.find_element_by_id('identifierNext').click()
        time.sleep(2)
        driver2.find_element_by_name('password').send_keys(password)
        driver2.find_element_by_id('passwordNext').click()
        time.sleep(2)

        print('Grabbing verification code')
        try:
            securityCode = driver2.find_element_by_class_name('bog').text
        except:
            print('Too many login attempts. Try again later')
            quit()
        securityCode = re.sub("\D", "", securityCode)

        print('Grabbed verification code')
        time.sleep(2)
        # enter security code after extracting from gmail and then finishing login
        print('Entering verification code')
        driver.find_element_by_id('oneTimeCode').send_keys(securityCode)

        eaSecurityStatus = ''
        driver.find_element_by_id('btnSubmit').click()
        print('submitted code')
        time.sleep(3)
        try:
            eaSecurityStatus = driver.find_element_by_xpath(
                '//*[contains(@class,"origin-ux-textbox-status-message origin-ux-status-message")]').text
        except:
            print('successfully entered code')
        print(eaSecurityStatus)
        if eaSecurityStatus != 'Incorrect code entered':
            successbool = False
        else:
            print('error with verification')
            try:
                driver.quit()
                driver2.quit()
            except:
                print('restarting...')

    print('Verification successful, entering account security...')
    time.sleep(12)
    driver.find_element_by_xpath('//*[contains(@class,"textInput isolated-section")]').send_keys('North')
    driver.find_element_by_xpath('//*[contains(@class,"standard call-to-action")]').click()
    time.sleep(6)
    driver.find_element_by_xpath('//*[contains(@class,"standard call-to-action")]').click()
    time.sleep(5)
    print('Accessing web app...')

# going to transfers
def tranferTab():
    time.sleep(3)
    print('Accessing transfer tab...')
    driver.find_element_by_xpath('//*[contains(@class,"btnFooter btnTransfers")]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[contains(@class,"btnFooter btnTransfers selected")]').click()
    driver.find_element_by_xpath('//*[contains(@class,"tile transferMarketTile")]').click()
    time.sleep(3)
# selecting Consumables
def consumablesINTRANSFERTAB():
    print('Opening consumables tab')
    driver.find_element_by_xpath("//*[contains(text(), 'Consumables')]").click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[contains(@class,"inline-list-select filter has-selection has-image")]').click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[contains(text(), 'Chemistry Styles')]").click()
    time.sleep(1)
    driver.find_elements_by_xpath("//*[contains(text(), 'Chemistry Style')]")[1].click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[contains(text(), 'ANCHOR')]").click()
    time.sleep(2)
    driver.find_elements_by_class_name('numericInput')[1].send_keys('700')
    time.sleep(3)
    try:
        driver.find_elements_by_xpath("//*[contains(text(), 'Search')]")[1].click()
    except:
        driver.find_elements_by_xpath("//*[contains(text(), 'Search')]")[3].click()
    time.sleep(1)

def makeBids():
    # clicks element and bids the selected price
    itemsOfInterestList = driver.find_elements_by_class_name('entityContainer')
    print('Locating and bidding selected items...')
    for item in itemsOfInterestList:
        time.sleep(3)
        print('1')
        item.click()
        print('2')
        time.sleep(1)
        itemPriceInput = driver.find_element_by_class_name('numericInput')
        itemPriceInput.click()
        itemPriceInput.clear()
        print('3')
        time.sleep(1)
        itemPriceInput.send_keys('700')
        print('4')
        executeBid = driver.find_element_by_xpath("//*[contains(text(), 'Make Bid')]")
        executeBid.click()
        time.sleep(1)
        try:
            highestbidderwarning = driver.find_element_by_xpath(
                '//*[contains(@class,"Dialog ui-dialog-type-message")]')
            highestbidderwarning.find_element_by_xpath("//*[contains(text(), 'Cancel')]").click()
        except:
            pass
        print('5')

        '''TODO ISSUES: 
        function will automatically bid higher than the current bid, ie, if bid is 4500, will bid 4600
        function bids regardless of time left on bid... bid on sometime with 2 days left
        function always stops at end of page - need to create function to change page
        '''
def transferTargetsTab():
    print('Opening Transfer targets...')
    driver.find_element_by_xpath('//*[contains(@class,"btnFooter btnTransfers")]').click()
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[contains(@class,"tile col-mobile-1-2 col-1-2 transferTargetsTile")]').click()
    time.sleep(1)

def listItems():
    availableItems = driver.find_elements_by_xpath(
        '//*[contains(@class,"list-view sectioned-item-list")]')[2]
    itemsForSale = availableItems.find_elements_by_class_name('entityContainer')
    for item in itemsForSale:
        print(1)
        time.sleep(2)
        item.click()
        time.sleep(1)
        driver.find_element_by_class_name('QuickListPanel').click()
        time.sleep(1)
        buyItNow = driver.find_elements_by_class_name('numericInput')[1]
        buyItNow.click()
        buyItNow.clear()
        buyItNow.click()
        time.sleep(1)
        buyItNow.send_keys('1300')
        time.sleep(2)
        print(2)
        itemPriceInput = driver.find_element_by_class_name('numericInput')
        itemPriceInput.click()
        itemPriceInput.clear()
        itemPriceInput.click()
        time.sleep(1)
        itemPriceInput.send_keys('1200')
        time.sleep(1)
        print(3)
        listTime = driver.find_element_by_xpath(
            '//*[contains(@class,"inline-list-select drop-down-select")]')
        listTime.click()
        listTime.find_element_by_xpath("//*[contains(text(), '3 Hours')]").click()
        time.sleep(1)
        print(4)
        executeList = driver.find_element_by_xpath("//*[contains(text(), 'List Item')]")
        executeList.click()

if __name__ == '__main__':
    main()

