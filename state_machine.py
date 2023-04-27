class State:
    pass


class TaskState(State):
    def __init__(self, prompt):
        self.prompt = prompt

    def complete(self):
        return self.prompt


class GreetingState(State):
    def __init__(self, greeting):
        self.greeting = greeting

    def welcome(self):
        print(self.greeting)


class ConfirmationState(State):
    pass


class Device:
    def __init__(self, tasks) -> None:
        self.tasks = tasks
        self.reject_input_state = TaskState("Invalid: ")
        self.state = GreetingState("welcome")

    def complete_tasks(self):
        self.state.welcome()
        for task in self.tasks:
            self.state = task
            while not input(f"{self.state.complete().lower()}: ") == "c":
                self.state = self.reject_input_state



tasks = [TaskState("test"), TaskState("test"), TaskState("test")]

Device(tasks).complete_tasks()
