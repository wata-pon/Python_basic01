"""
"Name: Kazuma, Age: 35"
"Name: Tom, Age: 57"
"Name: Bob, Age: 77"
"""

users_info = [["Kazuma", 35],
              ["Tom", 57],
              ["Bob", 77]]
for user_info in users_info:
    print(f'Name: {user_info[0]}, Age: {user_info[1]}')
