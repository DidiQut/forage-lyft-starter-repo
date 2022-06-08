from car_factory import Car_factory
import engine_factory
import battery_factory
from datetime import datetime

def check_service_or_not():

    spindler_battery = battery_factory.SpindlerBattery(datetime.today().date())
    capulet_engine = engine_factory.CapuletEngine(50000,0)
    car_factory = Car_factory(capulet_engine, spindler_battery)

    calliope_333 = car_factory.create_calliope()

    print(calliope_333.needs_service())


check_service_or_not()