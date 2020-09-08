import requests
from bs4 import BeautifulSoup as bs
from config import user, password

URL = 'https://selfserve.publicmobile.ca'
LOGIN_ROUTE = 'https://selfserve.publicmobile.ca/'

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
           'origin': URL, 'referer': LOGIN_ROUTE}

s = requests.session()

viewState_token = s.get(URL).cookies['__VIEWSTATE']
viewStateGenerator_token = s.get(URL).cookies['__VIEWSTATEGENERATOR']
eventValidation_token = s.get(URL).cookies['__EVENTVALIDATION']

login_payload = {
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': viewState_token,
    '__VIEWSTATEGENERATOR': viewStateGenerator_token,
    '__VIEWSTATEENCRYPTED': '',
    '__EVENTVALIDATION': eventValidation_token,
    'ctl00$FullContent$ContentBottom$LoginControl$UserName': user,
    'ctl00$FullContent$ContentBottom$LoginControl$Password': password,
    'ctl00$FullContent$ContentBottom$LoginControl$LoginButton': 'Log In'
}

login_req = s.post(LOGIN_ROUTE, headers=HEADERS, data=login_payload)

print(login_req.status_code)
