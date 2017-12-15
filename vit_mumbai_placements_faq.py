#i cant understand why these problems are happning !

import requests, bs4 as bs

sauce = requests.get("http://www.vit.edu.in/placements/tips-faq")
sauce.raise_for_status
soup = bs.BeautifulSoup(sauce.text,'lxml')


questions = []
answers = []

for question in soup.select('div[class="field-item"] h3'):
	if len(question.text):
		questions.append(question.text)

for answer in soup.select('div[class="field-item"] p'):
	if len(answer.text):
		answers.append(answer.text)

answers = answers[2:]


for i in range(len(questions)):
  print(questions[i])
  print("Ans : ",answers[i])
  print("\n\n")