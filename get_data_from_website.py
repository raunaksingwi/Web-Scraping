import sys
import urllib.request, bs4 as bs

try:
  if sys.argv[1] == '--help':
    print("Pass website url as arguement for which you want to collect the data for in the form example.com")
except:
  print("Pass website url as arguement for which you want to collect the data for in the form example.com")
  sys.exit()

root = str(sys.argv[1])

#to store the all the data (Paragraphs) from the webstie
data_file = open(root + ".txt",'w')
print("This will take time according to the volume of data. Generally takes few minutes...")
root = "http://www." + root
urls = [root]
to_search = [root]

root = sys.argv[1]

while to_search:
  current = to_search.pop()
  
  try:
    source = urllib.request.urlopen(current).read()
  except:
    continue

  soup = bs.BeautifulSoup(source, "html5lib")

  #Finding all the links from this page
  for anchor_text in soup.find_all('a'):
    link = anchor_text.get('href')
    if link not in urls:
      link_text = str(link)
      if root in link_text and ".pdf" not in link_text and ".rar" not in link_text:
        to_search.append(link)
        urls.append(link)
  
  #Parcing the data from this page.
  text = soup.findAll('p')

  for paragraph in text:
    paragraph = [word for word in paragraph.text.split() if word]
    paragraph = " ".join(paragraph)
    try:
      data_file.write(paragraph + "\n\n")
    except Exception:
      continue
data_file.close()

