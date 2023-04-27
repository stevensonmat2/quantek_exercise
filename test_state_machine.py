from state_machine import State, TaskState, ConfirmationState, Device

# Test the State class
def test_state_actions():
    state = State("prompt", "error message")
    assert state.actions == ["progress", "revert", "repeat"]

def test_state_prompt_message():
    state = State("prompt", "error message")
    assert state.prompt == "prompt"

def test_state_error_message():
    state = State("prompt", "error message")
    assert state.error_message == "error message"


# Test the TaskState class
def test_task_state_error_message():
    task_state = TaskState("prompt", "error message")
    assert task_state.error_message == "error message"


def test_task_state_prompt():
    task_state = TaskState("prompt", "error message")
    assert task_state.prompt == "prompt"


def test_task_state_complete_with_correct_input():
    task_state = TaskState("prompt", "error message")
    assert task_state.complete("c") == "progress"


def test_task_state_complete_with_incorrect_input():
    task_state = TaskState("prompt", "error message")
    assert task_state.complete("d") == "repeat"


# Test the ConfirmationState class
def test_confirmation_state_prompt():
    confirmation_state = ConfirmationState("prompt", "error message")
    assert confirmation_state.prompt == "prompt"


def test_confirmation_state_complete_with_correct_input():
    confirmation_state = ConfirmationState("prompt", "error message")
    assert confirmation_state.complete("y") == "progress"
    assert confirmation_state.complete("n") == "revert"


def test_confirmation_state_complete_with_incorrect_input():
    confirmation_state = ConfirmationState("prompt", "error message")
    assert confirmation_state.complete("d") == "repeat"


# Test the Device class
def test_device_init():
    tasks = [TaskState("prompt1", "error1"), TaskState("prompt2", "error2")]
    device = Device(tasks)
    assert device.tasks == tasks
    assert device.active == True


def test_device_handle_action_progress():
    tasks = [TaskState("prompt1", "error1"), TaskState("prompt2", "error2")]
    device = Device(tasks)
    assert device.state == tasks[0]
    device.handle_action("progress")
    assert device.state == tasks[1]


def test_device_handle_action_revert():
    tasks = [TaskState("prompt1", "error1"), TaskState("prompt2", "error2")]
    device = Device(tasks)
    device.handle_action("progress")
    assert device.state == tasks[1]
    device.handle_action("revert")
    assert device.state == tasks[0]


def test_device_handle_action_repeat():
    tasks = [TaskState("prompt1", "error1"), TaskState("prompt2", "error2")]
    device = Device(tasks)
    assert device.state == tasks[0]
    device.handle_action("repeat")
    assert device.state == tasks[0]
