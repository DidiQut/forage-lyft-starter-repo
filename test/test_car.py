import unittest
from datetime import datetime

import sys
sys.path.append('../')
from engine_factory import CapuletEngine
from engine_factory import SternmanEngine
from engine_factory import WilloughbyEngine

from battery_factory import SpindlerBattery
from battery_factory import NubbinBattery
from car_factory import Car_factory
import engine_factory
import battery_factory


class Test_battery(unittest.TestCase):
    def test_SpindlerBattery(self):
        spindler = SpindlerBattery(datetime(2014, 11, 11).date())
        self.assertTrue(spindler.needs_service())

    def test_NubbinBattery(self):
        nubbin = NubbinBattery(datetime(2016, 11, 11).date())
        self.assertTrue(nubbin.needs_service())


class Test_engine(unittest.TestCase):
    def test_CapuletEngine(self):
        capulet = CapuletEngine(67000, 25000) # test case1: expect True
        self.assertTrue(capulet.needs_service())

    def test_SternmanEngine(self):
        sternman = SternmanEngine(True) # test case1: expect True
        self.assertTrue(sternman.needs_service())

    def test_WilloughbyEngine(self):
        willoughby = WilloughbyEngine(90000,20000)  # test case1: expect True
        self.assertTrue(willoughby.needs_service())


class Test_car_model(unittest.TestCase):

    def test_glissade(self):
        spindler_battery = battery_factory.SpindlerBattery(datetime(2016, 11, 11).date())
        capulet_engine = engine_factory.WilloughbyEngine(50000, 0)
        car_factory = Car_factory(capulet_engine, spindler_battery)
        glissade = car_factory.create_glissade(datetime(2016, 11, 11).date(), 50000, 0)
        self.assertTrue(glissade.needs_service())

    def test_palindrome(self):
        nubbin_battery = battery_factory.NubbinBattery(datetime(2016, 11, 11).date())
        sternman_engine = engine_factory.SternmanEngine(True)
        car_factory = Car_factory(sternman_engine, nubbin_battery)
        palindrome = car_factory.create_palindrome(datetime(2016, 11, 11).date(), True)
        self.assertTrue(palindrome.needs_service())

    def test_rorschach(self):
        nubbin_battery = battery_factory.NubbinBattery(datetime(2020, 11, 11).date())
        willoughby_engine = engine_factory.WilloughbyEngine(90000, 5000)
        car_factory = Car_factory(willoughby_engine, nubbin_battery)
        rorschach = car_factory.create_rorschach(datetime(2020, 11, 11).date(), 90000, 5000)
        self.assertTrue(rorschach.needs_service())

    def test_thovex(self):
        nubbin_battery = battery_factory.NubbinBattery(datetime(2016, 11, 11).date())
        capulet_engine = engine_factory.CapuletEngine(50000, 45000)
        car_factory = Car_factory(capulet_engine, nubbin_battery)
        thovex = car_factory.create_thovex(datetime(2016, 11, 11).date(), 50000, 45000)
        self.assertTrue(thovex.needs_service())


if __name__ == '__main__':
    unittest.main()
