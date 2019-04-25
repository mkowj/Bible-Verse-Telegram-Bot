from bs4 import BeautifulSoup
import requests
import csv
url = requests.get('https://lifehopeandtruth.com/bible/bible-study/encouraging-bible-verses/encouraging-bible-verses-about-love/').text
soup = BeautifulSoup(url, 'lxml')

csv_file = open('bible_scrape3.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['verse'])

#ChapterIso
for soup_find1 in soup.find_all('p', class_='ebv-verse-text'):
	verse_iso = soup_find1.text
	csv_writer.writerow([verse_iso])

csv_file.close()