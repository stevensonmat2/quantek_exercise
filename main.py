from exercise_one import TaskOne, TaskOneInterface
from exercise_two import TaskTwo, TaskTwoInterface

if __name__ == "__main__":
    # Exercise 1
    tasks_one = [
        TaskOne("Complete Task Read Support Request"),
        TaskOne("Complete Task Isolate Source of Problem"),
        TaskOne("Complete Task Fix Problem"),
        TaskOne("Complete Task Document Issue and Solution"),
    ]

    task_one_interface = TaskOneInterface(tasks_one)
    print("New Support Request!\n** Enter 'c' to complete a task.")
    task_one_interface.complete_tasks()
    print("Support Request Complete!")

    # Exercise 2
    tasks_two = [
        TaskTwo("Complete Task Read Support Request", False),
        TaskTwo("Complete Task Isolate Source of Problem", False),
        TaskTwo("Complete Task Work on Solution", True),
        TaskTwo("Complete Task Document Issue and Solution", False),
    ]

    task_two_interface = TaskTwoInterface(tasks_two)
    print("New Support Request!\n** Enter 'c' to complete a task.")
    task_two_interface.complete_tasks()
    print("Support Request Complete!")
