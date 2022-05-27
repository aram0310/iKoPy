from bs4 import BeautifulSoup
import lxml

with open('website.html', encoding="utf8") as file:
    content = file.read()

#
soup = BeautifulSoup(content, 'lxml')
print(soup.title)
print(soup.title.name)

all_a = soup.find_all(name='a')

for tags in all_a:
    print(tags.name)
    print(tags.get('href'))


# find by ID & class
heading = soup.find(name='h3', id='heading')
sub_heading = soup.find(name='h6', class_='heading')
print(heading)
print(sub_heading)


# select by class
headings = soup.select('.heading')
print(headings)