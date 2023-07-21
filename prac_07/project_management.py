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
    for project in projects:
        print(project)
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        projects.sort()
        if menu_choice == "L":
            file_name = input("File name: ")
            load_file(file_name, projects)


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
