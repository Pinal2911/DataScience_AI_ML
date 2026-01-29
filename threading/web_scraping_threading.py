import threading
from bs4 import BeautifulSoup
import requests

urls=[
'https://python.langchain.com/v0.2/docs/introduction/',

'https://python.langchain.com/v0.2/docs/concepts/',

'https://python.langchain.com/v0.2/docs/tutorials/'
]

def fetch_content(url):
    res=requests.get(url)
    soup=BeautifulSoup(res.content,'html.parser')
    print(f"fetched {len(soup.text)} characters from {url}")

threads=[]
for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for t in threads:
    t.join()

print("all data from all urls collected")
