import requests
from bs4 import BeautifulSoup
m = "http://books.toscrape.com/catalogue/category/books/"
n = "sports-and-games_17"
o = "/index.html"
p = m + n + o
result = requests.get(p)    # site which you want to connect to
c = result.status_code   # 200 for successful connection
a = result.headers    # headers of the page
src = result.content
i = 0
soup = BeautifulSoup(src, 'lxml')
for a_tag in soup.find_all('a'):
    title = a_tag.attrs['href']
    d = title.split('/')
    if len(d) >= 4:
        i = i+1
        if i%2 == 0:
            x = d[len(d)-2].split('_')
            y = x[0]
            z = y.split('-')
            for j in z:
                if z.index(j) != len(z)-1:
                    print(j.upper(), end=" ")
                else:
                    print(j.upper())
        else:
            pass
    else:
        pass

