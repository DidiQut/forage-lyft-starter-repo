from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        pass


class Servicible(Car):
    def __init__(self,engine, battery):
        super().__init__(engine, battery)

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
