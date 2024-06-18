from datetime import datetime, timedelta

# Task 1: Create Task Class
class Task:
    def __init__(self, title, description, due_date, priority='Low'):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = 'Pending'
        self.notes = ''
        self.completed = False
        self.duration = 0
        self.history = []
        self.recurring = False
        self.dependency = None

    # Task 2: Add Method to Task Class
    def is_overdue(self):
        return datetime.now() > self.due_date

    def is_due_today(self):
        return self.due_date.date() == datetime.now().date()

    # Task 7: Update Task
    def update(self, title=None, description=None, due_date=None, priority=None):
        if title: self.title = title
        if description: self.description = description
        if due_date: self.due_date = due_date
        if priority: self.priority = priority

    # Task 8: Task Status
    def set_status(self, status):
        self.status = status
        self.history.append((datetime.now(), status))

    # Task 15: Task Notes
    def set_notes(self, notes):
        self.notes = notes

    # Task 17: Mark Task as Completed
    def mark_completed(self):
        self.completed = True
        self.status = 'Completed'
        self.history.append((datetime.now(), 'Completed'))

    # Task 22: Task Duration
    def set_duration(self, duration):
        self.duration = duration

    # Task 30: Task Dependency
    def set_dependency(self, dependency):
        self.dependency = dependency


# Task 3: Create Schedule Class
class Schedule:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    # Task 4: List Overdue Tasks
    def list_overdue_tasks(self):
        return [task for task in self.tasks if task.is_overdue() and not task.completed]

    # Task 5: List Tasks Due Today
    def list_tasks_due_today(self):
        return [task for task in self.tasks if task.is_due_today() and not task.completed]

    # Task 6: Sort Tasks by Due Date
    def sort_tasks_by_due_date(self):
        return sorted(self.tasks, key=lambda task: task.due_date)

    # Task 7: Update Task
    def update_task(self, title, **kwargs):
        for task in self.tasks:
            if task.title == title:
                task.update(**kwargs)
                break

    # Task 11: Task Priority
    def list_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority and not task.completed]

    # Task 13: Save Schedule to File
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for task in self.tasks:
                f.write(f'{task.title},{task.description},{task.due_date},{task.priority},{task.status},{task.notes}\n')

    # Task 14: Load Schedule from File
    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                title, description, due_date, priority, status, notes = line.strip().split(',')
                task = Task(title, description, datetime.fromisoformat(due_date), priority)
                task.status = status
                task.notes = notes
                self.tasks.append(task)

    # Task 16: List Tasks with Notes
    def list_tasks_with_notes(self):
        return [task for task in self.tasks if task.notes]

    # Task 18: List Completed Tasks
    def list_completed_tasks(self):
        return [task for task in self.tasks if task.completed]

    # Task 19: Find Task by Keyword
    def find_task_by_keyword(self, keyword):
        return [task for task in self.tasks if keyword in task.title or keyword in task.description]

    # Task 21: List All Tasks
    def list_all_tasks(self):
        return self.tasks

    # Task 25: Clear Completed Tasks
    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task.completed]

    # Task 27: List Recurring Tasks
    def list_recurring_tasks(self):
        return [task for task in self.tasks if task.recurring]

    # Task 29: Task Completion Percentage
    def percentage_completed(self):
        completed = sum(1 for task in self.tasks if task.completed)
        return (completed / len(self.tasks)) * 100 if self.tasks else 0

    # Task 20: Task Deadline Notification
    def task_deadline_notification(self):
        return [task for task in self.tasks if datetime.now() >= task.due_date - timedelta(hours=24) and not task.completed]

    # Task 24: Task History
    def list_task_history(self):
        history = []
        for task in self.tasks:
            history.extend(task.history)
        return history

    # Task 23: List Tasks by Duration
    def list_tasks_by_duration(self, duration):
        return [task for task in self.tasks if task.duration == duration]

    # Task 30: Task Dependency
    def set_task_dependency(self, title, dependency_title):
        dependency = next((task for task in self.tasks if task.title == dependency_title), None)
        if dependency:
            for task in self.tasks:
                if task.title == title:
                    task.set_dependency(dependency)
                    break


# Example Usage
schedule = Schedule()

task1 = Task("Buy groceries", "Milk, Bread, Eggs", datetime(2024, 6, 20), priority="High")
task2 = Task("Clean house", "Living room, Kitchen", datetime(2024, 6, 18))
task3 = Task("Write report", "Monthly financial report", datetime(2024, 6, 19), priority="Medium")

schedule.add(task1)
schedule.add(task2)
schedule.add(task3)

print("Overdue Tasks:", schedule.list_overdue_tasks()) # Task 4
print("Tasks Due Today:", schedule.list_tasks_due_today()) # Task 5
print("Tasks by Priority:", schedule.list_tasks_by_priority("High")) # Task 12

schedule.save_to_file("schedule.txt") # Task 13
schedule.load_from_file("schedule.txt") # Task 14

print("All Tasks:", schedule.list_all_tasks()) # Task 21
print("Completed Tasks:", schedule.list_completed_tasks()) # Task 18
print("Task Percentage Completed:", schedule.percentage_completed()) # Task 29
