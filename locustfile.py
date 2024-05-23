from locust import HttpUser, TaskSet, task, between

class TodoTasks(TaskSet):
    @task
    def view_index(self):
        self.client.get("/")

    @task
    def add_task(self):
        self.client.post("/add", {"task": "New task"})

    @task
    def delete_task(self):
        self.client.get("/delete/0")

class WebsiteUser(HttpUser):
    tasks = [TodoTasks]
    wait_time = between(1, 5)

if __name__ == "__main__":
    import os
    os.system("locust -f locustfile.py")
