import time

class Routine:
    def __init__(self, breakfast_time, lunch_time, evening_time, night_time):
        self.wake_time = breakfast_time
        self.lunch_time = lunch_time
        self.evening_time = evening_time
        self.night_time = night_time

    def breakfast(self):
        print(f"now at {self.wake_time} a.m. Good Morning!")
        time.sleep(0.4)
        self.lunch()

    def lunch(self):
        print(f"now {self.lunch_time} a.m and lunch time!")
        time.sleep(0.4)
        self.evening()

    def evening(self):
        print(f"now {self.evening_time} p.m . Good evening!")
        time.sleep(0.4)
        self.night()

    def night(self):
        print(f"now {self.night_time} p.m. Bed time and Good Night!")
        time.sleep(0.4)

obj = Routine("5.00", "12.30", "18.00", "22.00")
obj.breakfast()




