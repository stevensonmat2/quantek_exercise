class TaskTwo:
    def __init__(self, prompt, repeatable) -> None:
        self.prompt = prompt
        self.repeatable = repeatable


class TaskTwoInterface:
    def __init__(self, tasks) -> None:
        self.tasks = tasks

    def complete_tasks(self) -> None:
        for task in self.tasks:
            task_prompt = f"{task.prompt}: "
            self.validate_user_input(task_prompt)

            if task.repeatable:
                while not self.confirm_problem_resolved():
                    self.validate_user_input(task_prompt)

    def validate_user_input(self, task_prompt):
        user_response = input(task_prompt)
        while not user_response.lower() == "c":
            print("Invalid response! Enter 'c' to complete.")
            user_response = input(task_prompt)

    def confirm_problem_resolved(self):
        valid_responses = ["y", "n"]
        complete_task_prompt = "Complete Task Problem Fixed (y/n)? "
        user_response = input(complete_task_prompt)

        while not user_response in valid_responses:
            print("Invalid response! Enter 'y' or 'n'.")
            user_response = input(complete_task_prompt)

        return True if user_response == valid_responses[0] else False
