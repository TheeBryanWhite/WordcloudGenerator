from bs4 import BeautifulSoup
import urllib
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

url ="https://www.anchour.com/portfolio/logofolio/"
headers = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.3'}

req = urllib.request.Request(url, headers=headers)
data = urllib.request.urlopen(req).read()

soup = BeautifulSoup(data, "html.parser")

main_content = soup.find("main", attrs= {"class" : "main-content"})
lists = main_content.find_all("section")

str = ""
for list in lists:
    info= list.text
    str+=info

STOPWORDS.update(["see","common"])

mask = np.array(Image.open("./cloud-icon.png"))

color= ImageColorGenerator(mask)

wordcloud = WordCloud(width=2200, height=2000,    max_words=100,mask=mask, stopwords=STOPWORDS, background_color="white", random_state=42).generate(str)

plt.imshow(wordcloud.recolor(color_func=color),interpolation="bilinear")
plt.axis("off")
plt.show()

wordcloud.to_file("./wordcloud.png")
