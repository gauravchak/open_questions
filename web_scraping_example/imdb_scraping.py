from bs4 import BeautifulSoup
 
import requests
import sys
 
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, features="html.parser")
tr = soup.findChildren("tr")
tr = iter(tr)
next(tr)
 
for movie in tr:
    if movie:
        c_title = movie.find('td', {'class': 'titleColumn'})
        if c_title:
            title = c_title.find('a').contents[0]
            year = c_title.find('span', {'class': 'secondaryInfo'}).contents[0]
        else:
            continue
        c_rating = movie.find('td', {'class': 'ratingColumn imdbRating'})
        if c_rating:
            rating = c_rating.find('strong').contents[0]
        else:
            continue
        row = title + ' - ' + year + ' ' + ' ' + rating
        print(row)
    else:
        break
