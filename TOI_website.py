import requests
from bs4 import BeautifulSoup
result = requests.get("https://timesofindia.indiatimes.com/home/headlines")    # site which you want to connect to
c = result.status_code   # 200 for successful connection
a = result.headers    # headers of the page
src = result.content
soup = BeautifulSoup(src, 'lxml')
g = []
city = "mumbai"
for a_tag in soup.find_all('a'):
    title = a_tag.attrs['href']
    a = title.split('/')
    if len(a) > 2:
        if a[2] == city:
            if len(a) > 3:
                if a[3] not in g:
                    g.append(a[3])
                    b = a[3].split('-')
                    for j in b:
                        if b.index(j) != len(b)-1:
                            print(j.upper(), end=" ")
                        else:
                            print(j.upper())

            else:
                pass
    else:
        pass




