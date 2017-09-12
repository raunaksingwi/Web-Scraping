import requests, bs4 as bs

sauce = requests.get("http://www.rknec.edu/FAQ.aspx")
sauce.raise_for_status
soup = bs.BeautifulSoup(sauce.text,'lxml')


questions = []
answers = []
flag = True

for paragraph in soup.select('div[class="main-content-div"] p'):
  if paragraph.text == ' ':
    continue
  if flag:
    questions.append(paragraph.text)
    flag = False
  else:
    answers.append(paragraph.text)
    flag = True


for i in range(len(questions)):
  print(questions[i])
  print("Ans : ",answers[i])
  print("\n\n")