import requests
from bs4 import BeautifulSoup
#request modu ile alıyoruz. beautiful ile parçalıoyurz.

#google'a "my user agent" yazıp çıkan kodu parametre olarak yapıştırıyoruz.
headers_param = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
glassdor = requests.get("https://taksimokullari.com/basinda-biz", headers=headers_param)

#print(glassdor.content)
jobs = glassdor.content

soup = BeautifulSoup(jobs,"html.parser")

#html içindeki h1 etiketine sahip olanların sadece başlığını alır.
#print(soup.find("h1").text) 

#html içindeki div etiketine sahip olanları alır.
#print(soup.find_all("div"))  

#html içindeki a etiketine sahip olanları alır.
#print(soup.find_all("a"))

#print(soup.find_all("p"))

all_jobs = soup.find_all("div",{"class":"col-md-4 blog-mt"})

#print(all_jobs)
for job in all_jobs:
    print(job.h4.text)
    
alt_menu = soup.find_all("div",{"class":"col-md-4 altmenu"})
for data in alt_menu:
    print(data.text)
    