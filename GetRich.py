from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime


#Assign Variables
tweet= []
temp=[]
max=-2
boole=True
try:
    #Firefox Profile Configurations
    options = Options()
    options.add_argument("-profile")
    options.add_argument(r"C:\Users\user\AppData\Roaming\Mozilla\Firefox\Profiles\j71f4oya.default-release")
    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    browser = webdriver.Firefox(capabilities=firefox_capabilities, firefox_options=options)
    browser.maximize_window()
    time.sleep(1)
except: 
    print("Firefox profile Error")
#Lets Begin 
while(boole):
    #Date
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    #Twitter Notifications Page
    browser.get("https://twitter.com/notifications")
    time.sleep(2)
    #Click Last Notification
    bildirim=browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[2]/div/article/div[1]/div[2]/div[1]/div")
    time.sleep(2)
    bildirim.click()
    time.sleep(2)
    #Crawl Website
    html = browser.page_source
    soup = BeautifulSoup(html,"lxml")

    st1 = soup.find("div",attrs={"class":"css-1dbjc4n"})
    st2=st1.find("div",attrs={"class":"css-1dbjc4n r-1igl3o0 r-qklmqi r-1adg3ll r-1ny4l3l"})
    st5=st2.find_all("span",attrs={"class":"css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"})
    result = []
    acilis_fiyati=[]
    market_fiyati=[]
    #What is last tweet and who is author
    for link in st5:
        result.append(link.get_text())
    #Second element of list is author    
    account=result[1]
    tweet=result 
    #I need only tweet so
    del tweet[0]
    del tweet[0]
    del tweet[0]
    #Split all words and take name of Coin
    tweet=" ".join(tweet)
    tweet=tweet.split()
    #If account is Coinbase and This is Inbound transfer tweet
    if(account=="@CoinbasePro" and tweet[0]=="Inbound" ):
        print("this is Coin Base Twit\n")
        print ("Current date and time : ")
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        print("user is: " + account)
        
        #4. word is our Coin
        Coin=tweet[3]
        print("Coin is " + Coin)
        #Lets go coin market and buy it
        link_bası= "https://ftx.com/trade/"
        link_sonu="-PERP"
        link=link_bası + Coin + link_sonu
        browser.get(link)
        time.sleep(2)
        #buy as 11 dollar
        emir=browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/main/div[3]/div[3]/div/div/form/div/div[1]/div[2]/div/div")
        emir.click()
        
        market = browser.find_elements_by_css_selector(".MuiButtonBase-root.MuiListItem-root.MuiMenuItem-root.MuiMenuItem-gutters.MuiListItem-gutters.MuiListItem-button")
        
        market[1].click()
        
        money_box=browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/main/div[3]/div[3]/div/div/form/div/div[2]/div/div[2]/div/div/input")
    
        money_box.send_keys("11");
        
        time.sleep(1)
        buy=browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/main/div[3]/div[3]/div/div/form/div/div[4]/div/button[1]/span[1]")
        
        buy.click()
        time.sleep(1)
        browser.get(link)
        time.sleep(3)
        #After here, we can watch Profit and Loss and make moves accordingly.
        while(boole):
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            #Take HTML codes of market page
            html = browser.page_source

            soup = BeautifulSoup(html,"lxml")
            
            time.sleep(1)
            #Let's Take Instant Market Information as a List

            st7 = soup.find_all("td",attrs={"class":"MuiTableCell-root MuiTableCell-body MuiTableCell-alignRight"})
            
            time.sleep(1)

            for link in st7:
                acilis_fiyati.append(link.get_text())
            
            #The 3rd element of the list is the instant price, 5. the price we buy the element
            #Profit calculation and Screen printing
            
            anlik_fiyat = float(acilis_fiyati[3].replace(',',''))
            emir_fiyat = float(acilis_fiyati[5].replace(',',''))
            
            kar=(anlik_fiyat-emir_fiyat)/emir_fiyat 
            kar= kar*100
            kar=float(format(kar,".3f"))
            net_kar=kar*10
            #assign the profit rate to the variable. if profits decrease, sell.
            if(net_kar>max):
                max=net_kar
                
            
            print("emir_fiyat: " + str(emir_fiyat) + "\nanlık fiyat: " + str(anlik_fiyat) +"\nkar: %" + str(net_kar))
            print ("Current date and time : ")
            print (now.strftime("%Y-%m-%d %H:%M:%S"))
            print("\n***********************\n")
            acilis_fiyati=[]
            time.sleep(2)
            #Close Market
            if(net_kar<max):
                market_kapa=browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/main/div[3]/div[8]/div/div/div/table/tbody/tr/td[11]/button/span[1]")
                market_kapa.click()
                time.sleep(2)
                onay=browser.find_element_by_xpath("/html/body/div[5]/div[3]/div/div[3]/button[2]/span[1]")
                onay.click()
                print("Market %" + str(net_kar) + " kar ile kapatılmıştır")
                boole=False
        
    else:
        
    
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("This is unnecesary twit\n***********************\n")
        print('Tweet from:' + account)
        print ("Current date and time : ")
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
    
    
