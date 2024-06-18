# lab16
2.1 Лабораторна робота 16: Розширений список справ (Advanced TODO List)
2.2 Мета роботи:
Метою цієї лабораторної роботи є створення розширеного списку справ за допомогою об'єктно-орієнтованого програмування на мові Python. Очікувані результати включають розробку класів для представлення задач та розкладу, реалізацію різних методів для роботи із задачами, а також збереження та завантаження розкладу з файлу.

2.3 Опис завдання:
Створити клас Task з атрибутами title, description, due_date, priority.
Додати методи до класу Task для перевірки прострочених задач, задач на сьогодні, оновлення задачі, змінення статусу задачі, додавання приміток, маркування задачі як виконаної, встановлення тривалості виконання задачі, а також встановлення залежності задачі.
Створити клас Schedule для керування задачами.
Реалізувати методи класу Schedule для додавання задач, переліку прострочених задач, задач на сьогодні, сортування задач за терміном виконання, оновлення задач, переліку задач за пріоритетом, збереження та завантаження розкладу з файлу, переліку задач з примітками, виконаних задач, пошуку задач за ключовими словами, переліку всіх задач, очищення списку виконаних задач, переліку повторюваних задач, визначення відсотка виконаних задач, сповіщення про дедлайни, історії задач та задач за тривалістю виконання.
2.4 Виконання роботи:
Кроки виконання:

Створити репозиторій на GitHub з назвою, яка містить номер лабораторної роботи, наприклад labX.

Завантажити основний код програми (main.py) та README файл з детальним поясненням до репозиторію.

Структура проекту:


labX/
├── main.py
└── README.md
Опис файлів:

main.py: містить реалізацію класів Task та Schedule та основний код для демонстрації їх використання.
README.md: містить детальний опис проекту, основних функцій та методів, приклади використання.
Опис основних функцій та методів з поясненням їх роботи:

Клас Task:
__init__(self, title, description, due_date, priority='Low'): Конструктор класу.
is_overdue(self): Перевіряє, чи прострочена задача.
is_due_today(self): Перевіряє, чи має бути виконана задача сьогодні.
update(self, title=None, description=None, due_date=None, priority=None): Оновлює атрибути задачі.
set_status(self, status): Встановлює статус задачі.
set_notes(self, notes): Додає примітки до задачі.
mark_completed(self): Маркує задачу як виконану.
set_duration(self, duration): Встановлює тривалість виконання задачі.
set_dependency(self, dependency): Встановлює залежність задачі.
Клас Schedule:
add(self, task): Додає задачу до розкладу.
list_overdue_tasks(self): Перелік прострочених задач.
list_tasks_due_today(self): Перелік задач на сьогодні.
sort_tasks_by_due_date(self): Сортування задач за терміном виконання.
update_task(self, title, **kwargs): Оновлення задачі.
list_tasks_by_priority(self, priority): Перелік задач за пріоритетом.
save_to_file(self, filename): Збереження розкладу у файл.
load_from_file(self, filename): Завантаження розкладу з файлу.
list_tasks_with_notes(self): Перелік задач з примітками.
list_completed_tasks(self): Перелік виконаних задач.
find_task_by_keyword(self, keyword): Пошук задач за ключовими словами.
list_all_tasks(self): Перелік всіх задач.
clear_completed_tasks(self): Очищення списку виконаних задач.
list_recurring_tasks(self): Перелік повторюваних задач.
percentage_completed(self): Відсоток виконаних задач.
task_deadline_notification(self): Сповіщення про дедлайни.
list_task_history(self): Історія задач.
list_tasks_by_duration(self, duration): Перелік задач за тривалістю виконання.
set_task_dependency(self, title, dependency_title): Встановлення залежності задачі.
2.5 Приклади використання:


schedule = Schedule()

task1 = Task("Buy groceries", "Milk, Bread, Eggs", datetime(2024, 6, 20), priority="High")
task2 = Task("Clean house", "Living room, Kitchen", datetime(2024, 6, 18))
task3 = Task("Write report", "Monthly financial report", datetime(2024, 6, 19), priority="Medium")

schedule.add(task1)
schedule.add(task2)
schedule.add(task3)

print("Overdue Tasks:", schedule.list_overdue_tasks())
print("Tasks Due Today:", schedule.list_tasks_due_today())
print("Tasks by Priority:", schedule.list_tasks_by_priority("High"))

schedule.save_to_file("schedule.txt")
schedule.load_from_file("schedule.txt")

print("All Tasks:", schedule.list_all_tasks())
print("Completed Tasks:", schedule.list_completed_tasks())
print("Task Percentage Completed:", schedule.percentage_completed())
Результати:
Код реалізовано та завантажено до репозиторію на GitHub.
Основний код програми містить реалізацію класів Task та Schedule.
README файл містить опис проекту, опис кожного файлу та його призначення, опис основних функцій та методів, приклади використання.
Нижче надані скріншоти або приклади виводу програми:
Приклад виводу:


Overdue Tasks: [<__main__.Task object at 0x7f8e2a2d1a60>]
Tasks Due Today: []
Tasks by Priority: [<__main__.Task object at 0x7f8e2a2d19d0>]
All Tasks: [<__main__.Task object at 0x7f8e2a2d1a60>, <__main__.Task object at 0x7f8e2a2d1a90>, <__main__.Task object at 0x7f8e2a2d19d0>]
Completed Tasks: []
Task Percentage Completed: 0.0
