from datetime import date


class Task:
    def __init__(self, description=None, severity=None, deadline=None, status=None, assignee=None, start_time=None, end_time=None, Story_points=None):
        self.Story_points = Story_points
        self.description = description
        self.severity = severity
        self.deadline = deadline
        self.status = status
        self.assignee = assignee
        self.start_time = start_time
        self.end_time = end_time

    def get_severity(self):
        return self.severity

    def get_status(self):
        return self.status

    def get_deadline(self):
        return self.deadline

    def get_description(self):
        return self.description

    def get_assignee(self):
        return self.assignee

    def get_creat(self):
        return self.creat

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def display(self):
        print(
            f'description: {self.description} severity: {self.severity} deadline: {self.deadline} status: {self.status} assignee: {self.assignee} start_time: {self.start_time} end_time: {self.end_time}')

    def creat_time(self):
        return self.get_end_time() - self.get_start_time()

    def __del__(self):
        print(f'Bug {self.description} deleted')

class Bug (Task):
    def __init__(self, description=None, severity=None, deadline=None, status=None, assignee=None, start_time=None, end_time=None, Story_points=None):
        super().__init__(description, severity, deadline, status, assignee, start_time, end_time, Story_points)
        
class Backlog:
    def __init__(self, backlog=None):
        self.backlog = []

    def add_backlog(self, bug):
        self.backlog.append(bug)

    def get_resolved_bugs_by_assignee(self, assignee):
        lst = []
        for bug in self.backlog:
            if bug.get_status() == "RESOLVED" and bug.get_assignee() == assignee:
                lst.append(bug)
        return lst
    
    def sort_by_severity(self):
        n = len(self.backlog)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.backlog[j].severity > self.backlog[j + 1].severity:
                    self.backlog[j], self.backlog[j + 1] = self.backlog[j + 1], self.backlog[j]

        

    def all_display(self):
        for bug in self.backlog:
            bug.display()

    def story_points_by_months(self, year, months):
        monthly_points = {f"{year}/{month}": [] for month in months}
        for bug in self.backlog:
            if bug.get_status() == "RESOLVED" and bug.get_end_time():
                end_time = bug.get_end_time()
                month_key = f"{end_time.year}/{end_time.month}"
                if month_key in monthly_points:
                    monthly_points[month_key].append(bug.Story_points)

        return monthly_points

    def __del__(self):
        print(f'Backlog deleted')


def main():
    bug1 = Bug("не натискається кнопка Запуск", 3, deadline=date(2020, 12, 6), status='RESOLVED', assignee="Артьом", start_time=date(2020, 11, 8), end_time=date(2020, 11, 9), Story_points=4)
    bug2 = Bug("чорний екран", 4, deadline=date(2020, 12, 6), status='RESOLVED', assignee="Артьом", start_time=date(2020, 10, 8), end_time=date(2020, 11, 11), Story_points=7)
    bug3 = Bug("не натискається кнопка Огляд", 1, deadline=date(2021, 1, 23), status='RESOLVED', assignee="Міша", start_time=date(2020, 11, 8), end_time=date(2020, 12, 19), Story_points=1)
    bug4 = Bug("програма не запускаєть", 5, deadline=date(2021, 1, 3), status='open', assignee="Міша",  start_time=date(2020, 11, 8), end_time=date(2020, 12, 15), Story_points=10)

    backlog = Backlog()
    backlog.add_backlog(bug1)
    backlog.add_backlog(bug2)
    backlog.add_backlog(bug3)
    backlog.add_backlog(bug4)

    print('усі баги')
    backlog.all_display()

    print('\nчас вирішення помилок')
    print(bug1.creat_time())
    print(bug2.creat_time())
    print(bug3.creat_time())
    print(bug4.creat_time())

    backlog.sort_by_severity()
    print("\nусі баги(сортовані)")
    backlog.all_display()

    print("\nбаги вирішенні для Артьом")
    resolved_bugs_artom = backlog.get_resolved_bugs_by_assignee("Артьом")
    for bug in resolved_bugs_artom:
        bug.display()

    year = 2020
    months = [11, 12]
    monthly_story_points = backlog.story_points_by_months(year, months)
    for month, points in monthly_story_points.items():
        point = len(points)
        print(f'\n{month}: {point} Story points (за складністю {points})\n')

main()
