import datetime
import operator

from prac_07.project import Project
from operator import attrgetter

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter project by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    """Project management - help keep track of projects."""
    projects = []
    file_name = "projects.txt"
    load_file(file_name, projects)
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        projects.sort()
        if menu_choice == "L":
            file_name = input("File name: ")
            load_file(file_name, projects)
        elif menu_choice == "S":
            file_name = input("File name: ")
            save_file(file_name, projects)
        elif menu_choice == "D":
            display_projects(projects)
        elif menu_choice == "F":
            pass
        elif menu_choice == "A":
            add_project(projects)
        elif menu_choice == "U":
            projects.sort(key=operator.attrgetter('start_date'))
            update_project(projects)
        else:
            print("Invalid input")

        print(MENU)
        menu_choice = input(">>> ").upper()

    file_name = "projects.txt"
    save_file(file_name, projects)
    print("Thank you for using custom-built project management software")


def update_project(projects):
    """Update a projects percentage and priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    print(projects[project_choice])
    project = projects[project_choice]
    new_percentage = int(input("New Percentage: "))
    if new_percentage != 0:
        project.completion_percentage = new_percentage
    new_priority = int(input("New Priority: "))
    if new_priority != 0:
        project.priority = new_priority


def add_project(projects):
    """Add new project."""
    print("Let's add a new project")
    name = input("Name: ")
    date = input("Start date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))
    project = Project(name, date, priority, cost_estimate, percent_complete)
    projects.append(project)


def display_projects(projects):
    """Displays projects if they are completed or not."""
    print("Incomplete projects: ")
    for project in projects:
        if not project.is_completed():
            print(project)
    print("Completed projects: ")
    for project in projects:
        if project.is_completed():
            print(project)


def save_file(file_name, projects):
    """Save a file."""
    out_file = open(file_name, 'w')
    for project in projects:
        print(
            f"{project.name} {project.start_date} {project.priority} {project.cost_estimate} {project.completion_percentage}",
            file=out_file)
    out_file.close()


def load_file(file_name, projects):
    """Load a file."""
    in_file = open(file_name, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split("\t")
        date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
        project = Project(parts[0], date, int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)
    in_file.close()


main()
