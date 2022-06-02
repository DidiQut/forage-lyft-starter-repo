import abc
from datetime import datetime
from abc import ABC, abstractmethod

class battery(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class SpindlerBattery(battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.needs_service():
            return True
        else:
            return False


class NubbinBatter(battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.needs_service():
            return True
        else:
            return False