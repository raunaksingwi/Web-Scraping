import requests,bs4 as bs

sauce = requests.get("https://www.cs.umn.edu/admissions/graduate/faq")
sauce.raise_for_status
soup = bs.BeautifulSoup(sauce.text,'lxml')

questions = []
answers = []

for paragraph in soup.select('div[class="field-items"] p'):
  p = paragraph.text
  if len(p):
    if p[0] == 'Q':
      questions.append(p)
    if p[0] == 'A':
      answers.append(p)

for i in range(len(questions)):
  print(questions[i])
  print(answers[i])
  print("\n\n")
