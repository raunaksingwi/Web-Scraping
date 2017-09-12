#problem where there is lists in the answers.

import requests, bs4 as bs

sauce = requests.get("http://dmietr.edu.in/faq.htm")
sauce.raise_for_status
soup = bs.BeautifulSoup(sauce.text,'lxml')


questions = []
answers = []

for question in soup.select('td[class="grid-row"] strong'):
  questions.append(question.text)

for answer in soup.select('td[class="grid-alternate-row"]'):
  answers.append(answer.text)

for i in range(len(questions)):
  print(questions[i])
  print("Ans : ",answers[i])
  print("\n\n")