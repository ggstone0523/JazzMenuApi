from locust import HttpUser, between, task

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def main_page(self):
        self.client.get("/jazzcategorys")
        self.client.get("/jazzcategorys/1")
        self.client.get("/jazzcategorys/2")
        self.client.get("/jazzcategorys/3")
        self.client.get("/jazzcategorys/4")
        