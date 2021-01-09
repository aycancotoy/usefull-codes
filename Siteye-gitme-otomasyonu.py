from selenium import webdriver
import time

#seleniumun web sitesinden indirdiğimiz chrome sürümümüze uygun olan sürümün yolunu belirtiyoruz.
browser = webdriver.Chrome("C://Users//Acer//Desktop//chromedriver_win32//chromedriver.exe")

#siteyi get komutu ile alıyoruz..
browser.get("https://www.forbes.com/the-worlds-most-valuable-brands/#6ccb89e3119c")

#content ya da başlık almak için page source'u kullanıyoruz.
#print(browser.page_source)

#sitenin başlığı alalım
#print(browser.title)

browser.fullscreen_window()
time.sleep(5)

browser.get("https://www.forbes.com/companies/apple/?list=powerful-brands/&sh=6116b9975355")
time.sleep(5)

browser.set_window_size(600,400)
time.sleep(5)

#browser.refresh

browser.save_screenshot("C://Users//Acer//Desktop//img.png")
time.sleep(2)

browser.back()
time.sleep(3)

#Close komutu sadece tek sekme kapatmada kullanılır
#browser.close()

#chrome'u kapatır
browser.quit()