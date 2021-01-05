from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys #Enter tuşuna basmak için ekledik.

browser = webdriver.Chrome("C://Users//Acer//Desktop//chromedriver_win32//chromedriver.exe")

browser.get("https://www.linkedin.com/home")

#kaynak kodunu kopyalarken xpath olarak kopyaladık kök dizini.
login = browser.find_element_by_xpath("/html/body/nav/div/a[2]")
login.click()
time.sleep(3)

email = browser.find_element_by_xpath("//*[@id='username']")
password = browser.find_element_by_xpath("//*[@id='password']")

email.send_keys("xxx@gmail.com") #tırnaklar arasına linkedin kullanıcı mailimizi giriyoruz.
password.send_keys("xxxxx")  #tırnaklar arasına linkedin parolamızı giriyoruz.

login_button = browser.find_element_by_xpath("//*[@id='app__container']/main/div[2]/form/div[3]/button")
login_button.click()
time.sleep(3)

#search_bar = browser.find_element_by_xpath("//*[@id='ember20']/input")
#search_bar.send_keys("#python")
#search_bar.send_keys(Keys.RETURN) #RETURN enter tuşu anlamına geliyor.
#time.sleep(5)

#giriş yaptıktan sonra bağlantılara tıkla
contact = browser.find_element_by_xpath("//*[@id='ember26']")
contact.click()
time.sleep(5)

#bağlantıların içine gir
contact_in = browser.find_element_by_class_name("mn-community-summary__entity-info")
contact_in.click()
time.sleep(3)

#scrool hareketi için javascript(sayfayı aşağı dopru yüklemek için)
for i in range(1,5):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(5)

#içine girilen bağlantıların adı, çalıştığı pozisyon, bağlantı kurulma yılı
followers = browser.find_elements_by_class_name("mn-connection-card__details")
followersList=[]

for follower in followers:
    followersList.append(follower.text)

with open ("follower.txt","w",encoding = "UTF-8")as file:
    for follower in followersList:
        file.write(follower + "\n"+ "\n")
time.sleep(5)

browser.quit()
