logs = [
    (1609459200, 1, "enter"),
    (1609459260, 2, "enter"),
    (1609459320, 1, "exit"),
    (1609459380, 2, "enter"),
    (1609459440, 3, "enter")
]

# logs = [
#     (1609459200, 1, "enter"),
#     (1609459260, 2, "enter"),
#     (1609459320, 1, "exit"),
#     (1609459380, 2, "exit")
# ]

# logs = [
#     (1609459200, 1, "enter"),
#     (1609459260, 1, "enter"),
#     (1609459380, 2, "enter"),
#     (1609459440, 3, "enter")
# ]

# logs = []

last_action = {}
stil_insides = set()
violations = set()
if logs:
    for _,emp_id,action in logs:
        if action == 'enter':
            if last_action.get(emp_id) == 'enter':
                violations.add(emp_id)
            last_action[emp_id] ='enter'
        elif action == 'exit':
            last_action[emp_id] = 'exit'

    for emp_id,action in last_action.items():
        if action == 'enter':
            stil_insides.add(emp_id)
else:
    print("stil_insides :",[])
    print("violations",[])    

print(last_action)
print("stil_insides :",list(stil_insides))
print("violations",list(violations))