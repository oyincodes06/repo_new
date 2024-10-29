my_todo_list = [
    ("Monday", ["Prayer","Exercise", "Chores", "Assignment",  "Attend team meeting", "Code review", "Prayer", "Recess"]),
    ("Tuesday", ["Plan new features", "Write a Program", "Check email updates"]),
    ("Wednesday", ["Debug code", "Read Python Trends", "Update my Codes"]),
    ("Thursday", ["Fix bugs", "Upload_my_code", "Prepare for presentation"]),
    ("Friday", ["Code new feature", "Review analytics", "Plan for next week"]),
]

def show_all_todos():
    print("All to-dos for the week:")
    for day, todos in my_todo_list:
        print(f"\n{day}:")
        for todo in todos:
            print(f"{todo}")



show_all_todos()