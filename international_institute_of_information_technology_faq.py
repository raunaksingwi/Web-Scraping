#problem in fetching answers using the class et_pb_toggle_content.

import requests,bs4 as bs

sauce = requests.get("http://www.isquareit.edu.in/index.php/faqs/")
sauce.raise_for_status
soup = bs.BeautifulSoup(sauce.text,'lxml')

questions = []
answers = []

for question in soup.select('h5[class="et_pb_toggle_title"]'):
  questions.append(question.text)

for answer in soup.select('div[class="et_pb_toggle_content"] > p'):
  answers.append(answer.text)

"""for i in range(len(question)):
  print(questions[i])
  print(answers[i])
  print("\n\n")"""

print(questions)
print(answers)

print("Questions : ",len(questions))
print("Answers : ",len(answers))