import requests, bs4 as bs

sauce = requests.get("https://cdac.in/index.aspx?id=PlacementFAQ")
sauce.raise_for_status
soup = bs.BeautifulSoup(sauce.text,'lxml')


questions = []
answers = []

for question in soup.select('h4[class="panel-title"] span'):
  if len(question.text):
    questions.append(question.text.strip())

for answer in soup.select('div[class="panel-body"] div'):
  if len(answer.text):
    answers.append(answer.text.strip())


for i in range(len(questions)):
  print(questions[i])
  print("Ans : ",answers[i])
  print("\n\n")
