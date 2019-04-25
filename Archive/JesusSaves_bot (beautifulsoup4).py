# imports
from bs4 import BeautifulSoup
import requests
url = requests.get('https://lifehopeandtruth.com/bible/bible-study/encouraging-bible-verses/encouraging-bible-verses-about-gods-strength/').text
soup = BeautifulSoup(url, 'lxml')

#VerseIso
for soup_find in soup.find_all('p', class_='ebv-verse-text'):
    verse_iso = soup_find.text
    print(verse_iso)

#ChapterIso
for soup_find1 in soup.find_all('p', class_='ebv-verse'):
    chapter_iso = soup_find1.text
    print(chapter_iso)

print()
print('helloworld')