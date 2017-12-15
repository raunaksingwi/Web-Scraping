#problem in answers

import requests, bs4 as bs

sauce = requests.get("https://www.kpit.com/company/careers/campus-placements-and-internships")
sauce.raise_for_status
soup = bs.BeautifulSoup(sauce.text,'lxml')


questions = []
answers = []

for question in soup.select('h4'): #though this is working for this website, this is a very bad practise to use h4 tag to use a specific information.
	if len(question.text):
		questions.append(question.text)

for answer in soup.select('div[class="panel-collapse"] div'):
	if len(answer.text):
		answers.append(answer.text)


for i in range(len(questions)):
  print(questions[i])
  print("Ans : ",answers[i])
  print("\n\n")