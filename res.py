from bs4 import BeautifulSoup
import requests
 
session = requests.Session()
url_page = 'WEBSITE'
loginpage = session.get(url_page,verify=False)
soup = BeautifulSoup(loginpage.text,"html.parser")

#Self Serve portal details
username = ""
password = ""

#initilaze viewstate objects
viewstate = soup.select("#__VIEWSTATE")[0]['value']
viewstategenerator = soup.select("#__VIEWSTATEGENERATOR")[0]['value']
viewstateencrypted = soup.select("#__VIEWSTATEENCRYPTED")[0]['value']
eventvalidation = soup.select("#__EVENTVALIDATION")[0]['value']

item_request_body = {
"__EVENTTARGET":"",
"__EVENTARGUMENT":"",
"__VIEWSTATE":viewstate,
"__VIEWSTATEGENERATOR":viewstategenerator,
"__VIEWSTATEENCRYPTED":viewstateencrypted,
"__EVENTVALIDATION":eventvalidation,
"ctl00$FullContent$ContentBottom$LoginControl$UserName":username,
"ctl00$FullContent$ContentBottom$LoginControl$Password":password,
"ctl00$FullContent$ContentBottom$LoginControl$chkRememberUsername":"on",
"ctl00$FullContent$ContentBottom$LoginControl$LoginButton":"Log In"
}
 
response = session.post(url=url_page, data=item_request_body, headers={"Referer": url_page}, verify=False)
soup = BeautifulSoup(response.text,"html.parser")
print(soup.find(id="PrePaidCurrentBalanceLabelPnP"))


# How to Login and Scrape Websites with Python
# https://codeyogi.co.uk/2020/01/21/how-to-login-and-scrape-websites-with-python/

# Scrape Websites Behind a Login | Web Scraping for Beginners
# https://www.youtube.com/watch?v=SA18JCBtlXY