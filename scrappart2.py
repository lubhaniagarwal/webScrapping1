from bs4 import BeautifulSoup
import requests

url= 'https://nameless-meadow-64755.herokuapp.com/'
r=requests.get(url)
data = r.text
soup = BeautifulSoup(data,'html.parser')
container = soup.find("div",{"class":"box1"})

filename= "experience.csv"
f= open(filename, "w")
headers= "Title_experience, information, images\n"
f.write(headers)


experience = soup.findAll("div",{"class":"card zoom zoom"})



for exper in experience:
    more_info= exper.find("div",{"class":"card-body"})
    tit= more_info.h6.text
    info = more_info.p.text
    list = exper.img["src"]
    f.write(tit + "," + info + "," + list+ "\n")  

f.close()
    



 
