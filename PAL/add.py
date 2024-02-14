def solution():
    total_students = 17
    not_picked = 5
    groups = 3

    selected_students = total_students - not_picked
    group_size = selected_students // groups

    print(f"Target: {group_size}")


"""
                Sure, here's a Python function that solves the problem:
```python
def solution():
    total_students = 17
    not_picked = 5
    groups = 3

    selected_students = total_students - not_picked
    group_size = selected_students // groups

    print(f"Target: {group_size}")
```
Explanation:

1. First, we calculate the number of selected students by subtracting the number of students not picked from the total number of students.
2. Then, we divide the number of selected students by the number of groups to find the size of each group.
3. Finally, we print the size of each group as the output.

Note: The `f` string prefix is used to create a formatted string, which allows us to include variables in the string using `{ }`. This makes the output more readable.
"""
