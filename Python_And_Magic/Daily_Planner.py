planner = [
    "Submit Assignments",
    "Go for a walk"
]

"""By coping like this both today_tasks & planner referencing to the same list in the memory that's why changing one will reflect this other better use copy()"""
today_tasks = planner.copy()
today_tasks.append("Practice Coding")

print(today_tasks)
print(planner)