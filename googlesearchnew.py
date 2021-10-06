import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup
import os
import sys
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url_home = "https://www.google.%(tld)s/"
url_search_num = "https://www.google.%(tld)s/search?hl=%(lang)s&q=%(query)s&" \
                 "num=%(num)d&btnG=Google+Search&tbs=%(tbs)s&safe=%(safe)s&" \
                 "cr=%(country)s"

#if sys.version_info[0] > 2:
 #   from http.cookiejar import LWPCookieJar
  #  from urllib.request import Request, urlopen
   # from urllib.parse import quote_plus, urlparse, parse_qs
#else:
 #   from cookielib import LWPCookieJar
  #  from urllib import quote_plus
   # from urllib2 import Request, urlopen
    #from urlparse import urlparse, parse_qs

home_folder = os.getenv('HOME')
if not home_folder:
    home_folder = os.getenv('USERHOME')
    if not home_folder:
        home_folder = '.'   # Use the current folder on error.
#cookie_jar = LWPCookieJar(os.path.join(home_folder, '.google-cookie'))
#try:
 #   cookie_jar.load()
#except Exception:
 #   pass


USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'

def get_page(url, user_agent=None):
    if user_agent is None:
        user_agent = USER_AGENT
        request = urllib.request.Request(url)
        request.add_header('User-Agent', user_agent)
  #      cookie_jar.add_cookie_header(request)
        response = urllib.request.urlopen(request)
   #     cookie_jar.extract_cookies(response, request)
        html = response.read()
        response.close()
    #    try:
     #       cookie_jar.save()
      #  except Exception:
       #     pass
        return html

def search(query, tld='com', lang='en', tbs='0', safe='off', num=10, start=0,
           stop=None, pause=2.0, country='', extra_params=None,
           user_agent=None, verify_ssl=True):
    query = urllib.parse.quote_plus(query)     #converts the unicode to utf-8

    if not extra_params:
        extra_params = {}

    # Grab the cookie from the home page.
    ###get_page(url_home % vars(), user_agent)   # not needed

    # Prepare the URL of the first request.
    url = url_search_num % vars()          ##vars to stuff the values for url

        # Sleep between requests.
        # Keeps Google from banning you for making too many requests.
    time.sleep(pause)

        # Request the Google Search results page.
    html = get_page(url, user_agent)

    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.prettify())
    print("###################################################")
    anchors = soup.find('div',attrs={"class":"uozReb"})  ##bulleted list class="TYvcTb"
    if anchors==None:
        print("No Description in the webpage")
        exit()
    anchors2=anchors.find("span")    ##findall(span) gives duplicate values so used find
    print(anchors2.text)   ## was not able to get the text while using for loop for anchors2

    anchors3 = soup.find('ul', attrs={"class": "TYvcTb"})    ##bulleted list class="TYvcTb"
    if anchors3 == None:
        print("No bulleted list")
        exit()
    return anchors3.text    ##findall(span) gives duplicate values so used find




## doubts : 1.dont know how many searches it might allow
##          2.whether the coolies will get downloaded in the new system