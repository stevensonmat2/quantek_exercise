class State:
    def __init__(self):
        self.actions = ['progress', 'revert']
    def complete(self):
        pass


class TaskState(State):
    def __init__(self, prompt):
        super().__init__()
        self.prompt = prompt

    def complete(self):
        while not input("enter c: ") == 'c':
            print("invalid")
        return self.actions[0]
        


class GreetingState(State):
    def __init__(self, greeting):
        self.greeting = greeting

    def complete(self):
        print(self.greeting)


class ConfirmationState(State):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def complete(self):
        response = input("done? y/n: ")
        while not response in ['y', 'n']:
            print("invalid")
            response = input("done? y/n: ")

        if response == 'y':
            return self.actions[0]
        
        elif response == 'n':
            return self.actions[1]


class Device:
    def __init__(self, tasks) -> None:
        self.tasks = tasks
        self.active = True

    def complete_tasks(self):
        print("welcome")
        task_index = 0
        while self.active:
            self.state = self.tasks[task_index]
            action = self.state.complete()

            if action == "progress":
                task_index = task_index + 1
                if task_index == len(self.tasks):
                    self.active = False

            elif action == "revert":
                task_index = task_index - 1 or 0



tasks = [TaskState("test"), TaskState("test"), ConfirmationState("done?")]

Device(tasks).complete_tasks()
