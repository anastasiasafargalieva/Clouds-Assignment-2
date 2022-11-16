import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    @task
    def integral(self):
        self.client.get("/api/0/3.14159")

# locust -f locustfile.py --headless -u 3 --run-time 180 --host=https://polite-hill-a9b768bb46e84a76b2a9bdeb1437c2a9.azurewebsites.net --csv=part3 &> part3.dat

# locust -f locustfile.py --headless -u 3 --run-time 180 --host=https://myshinyfunction.azurewebsites.net --csv=part3 &> part3.dat