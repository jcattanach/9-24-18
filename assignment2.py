#Still need to finish remove ability and user id incrementing
#





# TO DO LIST ASSIGNMENT
class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.id = 1

    def increment_id(self):
        self.id = self.id + 1

    def __repr__(self):
        return "** TO-DO ITEM {0}: {1}\n PRIORITY: {2} **\n".format(self.id, self.title, self.priority)

tasks = []

while True:

    print("**** WELCOME TO TO-DO LIST ****\n(press 'q' to quit at anytime)")

    choice = input("What would you like to do?\na-add new task, \nq-quit, \nr-remove, \nv-view list: ").upper()
    if choice == 'A':
        task_input = input("Enter your task: ").upper()
        if task_input == 'Q':
            break
        priority_input = input("Enter the priority of your task (HIGH, MEDIUM, OR LOW): ").upper()
        if priority_input == 'Q':
            break

        task1 = Task(task_input, priority_input)

        task1.increment_id()

        tasks.append(task1)


    # if choice == 'R':
    #     del tasks[:]
    #     print("Items removed")
    #     print(tasks)

    if choice == 'V':
        print(tasks)

    if choice == 'Q':
        break



print("Thank you for using TO-DO LIST!")
