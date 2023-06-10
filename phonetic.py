import requests
from bs4 import BeautifulSoup
def read( word ):
    url = f'https://tw.dictionary.search.yahoo.com/search;_ylt=Awrt4EJEZYRkEbkQsgp7rolQ;_ylc=X1MDMTM1MTIwMDM3OQRfcgMyBGZyAwRmcjIDc2ItdG9wLXNlYXJjaARncHJpZANwMXdsM25pWFREeURjZDEuX0pMRFNBBG5fcnNsdAMwBG5fc3VnZwM2BG9yaWdpbgN0dy5kaWN0aW9uYXJ5LnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzMEcXVlcnkDY2F0BHRfc3RtcAMxNjg2Mzk4Mjg0?p={word}&fr=sfp&iscqry=&fr2=sb-top-search'  
    html = requests.get( url )
    bs = BeautifulSoup(html.text,'lxml')
    data = bs.find('div', {'class':'grp grp-main pl-25'} )

    try:
        english = data.find_all('span')[0].text
        chinese = data.find_all('li')[2].text
        return( english + " " + chinese)
    except:
        return( '無法翻譯此單字，請重新輸入' )
