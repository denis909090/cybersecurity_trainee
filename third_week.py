users = {
    "user_001": {
        "name": "Олександр Коваленко",
        "age": 28,
        "email": "olex.koval@example.com",
        "role": "Software Engineer",
        "is_active": True
    },
    "user_002": {
        "name": "Elena Rodriguez",
        "age": 34,
        "email": "e.rodriguez@domain.es",
        "role": "UI/UX Designer",
        "is_active": False
    },
    "user_003": {
        "name": "Максим Зайченко",
        "age": 21,
        "email": "max_z@ukr.net",
        "role": "Intern",
        "is_active": True
    },
    "user_004": {
        "name": "Yuki Tanaka",
        "age": 30,
        "email": "yuki.t@company.jp",
        "role": "Project Manager",
        "is_active": True
    },
    "user_005": {
        "name": "Анна Петренко",
        "age": 25,
        "email": "petrenko.a@tech-it.ua",
        "role": "Data Analyst",
        "is_active": True
    }
}

def user_name(user_name, mass_users):  
    for user in mass_users:  
        if user_name in mass_users[user]["name"]:  
            print('В нас є такий робітник')  
            print(mass_users[user]["name"])  
  
user_name("Олександр ", users)