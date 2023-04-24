class TaskOne:
    def __init__(self, prompt) -> None:
        self.prompt = prompt


class TaskOneInterface:
    def __init__(self, tasks) -> None:
        self.tasks = tasks

    def complete_tasks(self) -> None:
        for task in self.tasks:
            task_prompt = f"{task.prompt}: "
            self.validate_user_input(task_prompt)

    def validate_user_input(self, task_prompt):
        user_response = input(task_prompt)

        while not user_response.lower() == "c":
            print("Invalid response! Enter 'c' to complete.")
            user_response = input(task_prompt)
