import datetime
from prac_07.project import Project

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
        menu_choice = input(">>> ").upper()

    file_name = "projects.txt"
    save_file(file_name, projects)


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
