class State:
    def __init__(self, prompt, error_message):
        self.actions = ["progress", "revert", "repeat"]
        self.prompt = prompt
        self.error_message = error_message

    def complete(self):
        pass


class TaskState(State):
    def complete(self, user_input):
        if not user_input == "c":
            return self.actions[2]
        return self.actions[0]


class ConfirmationState(State):
    def complete(self, user_input):
        if not user_input in ["y", "n"]:
            return self.actions[2]

        elif user_input == "y":
            return self.actions[0]

        elif user_input == "n":
            return self.actions[1]


class Device:
    def __init__(self, tasks) -> None:
        self.tasks = tasks
        self.active = True
        self.task_index = 0
        self.state = self.tasks[self.task_index]

    def complete_tasks(self):
        print("New Support Request!\n** Enter 'c' to complete a task.")

        while self.active:
            user_input = input(f"{self.state.prompt}: ")
            action = self.state.complete(user_input)
            self.handle_action(action)

        print("Support Request Complete!")

    def handle_action(self, action):
        if action == "progress":
            self.task_index = self.task_index + 1
            if self.task_index == len(self.tasks):
                self.active = False
            else:
                self.state = self.tasks[self.task_index]

        elif action == "revert":
            self.task_index = self.task_index - 1 or 0
            self.state = self.tasks[self.task_index]

        elif action == "repeat":
            print(self.state.error_message)


if __name__ == "__main__":
    task_error_message = "invalid response! enter 'c'"
    tasks = [
        TaskState("Complete Task Read Support Request", task_error_message),
        TaskState("Complete Task Isolate Source of Problem", task_error_message),
        TaskState("Complete Task Work on Solution", task_error_message),
        ConfirmationState(
            "Complete Task Problem Fixed (y/n)?", "Invalid response! Enter 'y' or 'n'"
        ),
        TaskState("Complete Task Document Issue and Solution", task_error_message),
    ]

    Device(tasks).complete_tasks()
