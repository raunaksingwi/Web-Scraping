import requests, bs4 as bs

sauce = requests.get("http://dmietr.edu.in/faq.htm")
sauce.raise_for_status
soup = bs.BeautifulSoup(sauce.text,'lxml')


questions = []
answers = []





for i in range(len(questions)):
  print(questions[i])
  print("Ans : ",answers[i])
  print("\n\n")