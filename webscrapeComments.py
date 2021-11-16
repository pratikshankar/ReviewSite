import requests
from bs4 import BeautifulSoup
  
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/90.0.4430.212 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
  
# user define function
# Scrape the data
def getdata(url):
    r = requests.get(url, headers=HEADERS)
    return r.text
  
  
def html_code(url):
  
    # pass the url
    # into getdata function
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
  
    # display html code
    return (soup)
  
  
url = "https://www.amazon.in/Columbia-Mens-wind-\
resistant-Glove/dp/B0772WVHPS/?_encoding=UTF8&pd_rd\
_w=d9RS9&pf_rd_p=3d2ae0df-d986-4d1d-8c95-aa25d2ade606&pf\
_rd_r=7MP3ZDYBBV88PYJ7KEMJ&pd_rd_r=550bec4d-5268-41d5-\
87cb-8af40554a01e&pd_rd_wg=oy8v8&ref_=pd_gw_cr_cartx&th=1"
  
soup = html_code(url)
# print(soup)

def cus_rev(soup):
    # find the Html tag
    # with find()
    # and convert into string
    data_str = ""
  
    for item in soup.find_all("div", class_="a-expander-content \
    reviewText review-text-content a-expander-partial-collapse-content"):
        data_str = data_str + item.get_text()
  
    result = data_str.split("\n")
    print(result)
    return (result)
  
  
rev_data = cus_rev(soup)
print(rev_data)
rev_result = []
for i in rev_data:
    if i == "":
        pass
    else:
        rev_result.append(i)
