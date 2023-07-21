"""
CP1404 Prac 7 - Project management program
Estimated time: 2 hr
Actual time:
"""



class Project:
    """Represent a Project object."""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """
        Initialise a Project instance
        name: string, what the task is
        start_date: datetime.date, start date of task
        priority: int, the order of the tasks
        cost_estimate: float, how much it will cost to do task
        completion_percentage: int, how close to completing task
        """
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return string representation of data in a Project object."""
        return f"{self.name}, start: {self.start_date: %d/%m/%Y}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"
