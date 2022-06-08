from car import Car, Servicible
import engine_factory
import battery_factory


class Car_factory(Car):
    def __init__(self, engine, battery):
        super().__init__(engine, battery)

    def needs_service(self):
        pass

    def create_calliope(self):
        # return car object of calliope
        return Servicible(self.engine, self.battery)

    def create_glissade(self, last_service_date, current_mileage, last_service_mileage):
        return Servicible(engine_factory.WilloughbyEngine(current_mileage, last_service_mileage),
                       battery_factory.SpindlerBattery(last_service_date))

    def create_palindrome(self, last_service_date, warning_light_on):
        return Servicible(engine_factory.SternmanEngine(warning_light_on),
                       battery_factory.NubbinBattery(last_service_date))

    def create_rorschach(self, last_service_date, current_mileage, last_service_mileage):
        return Servicible(engine_factory.WilloughbyEngine(current_mileage, last_service_mileage),
                       battery_factory.NubbinBattery(last_service_date))

    def create_thovex(self, last_service_date, current_mileage, last_service_mileage):
        return Servicible(engine_factory.CapuletEngine(current_mileage, last_service_mileage),
                       battery_factory.NubbinBattery(last_service_date))