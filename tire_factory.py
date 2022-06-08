from abc import ABC, abstractmethod


class Tire(ABC):
    @abstractmethod
    def needs_service(self):
        pass

# The new tire wear sensors produce an array of four numbers between
# 0 and 1 inclusive, representing how worn each of the tires are.
# This array will be passed to each function in the car factory class,
# to be used by your tire implementation. Carrigan tires should be serviced
# only when one or more of the values in the tire wear array is greater
# than or equal to 0.9. Octoprime tires should be serviced only when
# the sum of all values in the tire wear array is greater than or equal to 3.
# Think carefully about the cleanest way to implement the new tire
# service criteria, then modify the system to complete the change.
# When you’re finished, push your changes and submit a link to your repo.
class Carrigan_tires(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        if self.tire_wear >= 0.9:
            return True
        else:
            return False


class Octoprime_tires(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        if self.tire_wear * 4 >= 3:
            return True
        else:
            return False

