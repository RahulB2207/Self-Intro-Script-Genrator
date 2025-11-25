"""
Challenge:
Create a Python script that interacts with user and genrates a personalized self-introduction

Your program should
1. Ask the user for their name, age, city, profession and favorite hobby
2. warm this data into a warm, friendly paragrph of interoduction
3. print the final paragraph in a clean and readable formt
"""
from datetime import date

get_info = {}
def User_input(user_info):
    global get_info
    for index,element in enumerate(user_info):
        value = input(f"please enter {element} :- ")
        get_info[element] = value

def greet(info):

    return f" {"*"*80}\n Hello! My name is {info['name']}, I'm {info['age']} and live in {info['city']}. I work as a {info['profession']} and I absolutely enjoy playing {info['hobby']} in my free time. Nice to meet you! by ---{(date.today())}\n {"*"*80}"  

required_user_info = ["name","age","city","profession","hobby"]
User_input(required_user_info)
print(greet(get_info))