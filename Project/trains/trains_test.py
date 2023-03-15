import unittest
from trains import *


class TestStation(unittest.TestCase):
    """
    Tests all the functions of the Station class
    """

    station_a = Station("a", 0.5)
    station_b = Station("B", 0.001)
    station_c = Station("C", 0.02)
    stations = [station_a, station_b, station_c]

    def test_init(self):
        self.assertEqual(self.station_a.name, "A")
        self.assertAlmostEqual(self.station_b.delay_prob, 0.001)

    def test_get_station_obj(self):
        self.assertEqual(self.station_a, Station.get_station_obj(self.stations, "A"))
        self.assertEqual(self.station_b, Station.get_station_obj(self.stations, "B"))
        self.assertEqual(self.station_c, Station.get_station_obj(self.stations, "C"))

    def test_str(self):
        self.assertEqual("C", str(self.station_c))
        self.assertEqual("B", str(self.station_b))
        self.assertNotEqual("A", str(self.station_c))


class TestRail(unittest.TestCase):
    """
    Test all the functions of the Rail class
    """
    station_a = Station("a", 0.5)
    station_b = Station("B", 0.001)
    station_c = Station("C", 0.02)
    station_d = Station("D", 0.09)

    rail_1 = Rail(station_a, station_b, "blue", "s")
    rail_2 = Rail(station_b, station_c, "blue", "S")
    rail_3 = Rail(station_d, station_c, "blue", "n")

    def test_init(self):
        self.assertEqual(self.rail_1.source, self.station_a)
        self.assertEqual(self.rail_2.target, self.station_c)
        self.assertEqual(self.rail_2.line, "BLUE")
        self.assertEqual(self.rail_3.direction, "N")

    def test_str(self):
        self.assertEqual("A-B (BLUE, S)", str(self.rail_1))
        self.assertEqual("B-C (BLUE, S)", str(self.rail_2))
        self.assertEqual("D-C (BLUE, N)", str(self.rail_3))


class TestLines(unittest.TestCase):
    """
    Test all the functions of the Line class
    """
    # Station objects
    station_a = Station("a", 0.5)
    station_b = Station("B", 0.001)
    station_c = Station("C", 0.02)
    station_d = Station("D", 0.09)
    station_e = Station("E", 0.04)
    station_f = Station("F", 0)
    stations = [station_a, station_b, station_c, station_d, station_e, station_f]

    # Rail objects
    rail_1 = Rail(station_a, station_b, "blue", "s")
    rail_2 = Rail(station_b, station_c, "blue", "S")
    rail_3 = Rail(station_d, station_c, "blue", "n")
    rail_4 = Rail(station_e, station_f, "red", "s")

    # Line objects
    connections = [rail_1, rail_2, rail_3, rail_4]
    lines = Lines(connections)

    def test_init_create_lines(self):  # Also test create_line function since init implements the create_line
        self.assertEqual({"BLUE": [self.station_a, self.station_b, self.station_c, self.station_d],
                            "RED": [self.station_e, self.station_f]},
                            self.lines.railways)

    def test_get_line_names(self):
        self.assertEqual(["BLUE", "RED"], self.lines.get_line_names())

    def test_str(self):
        str_line = f"BLUE: \n\t{self.station_a}\t{self.station_b}\t{self.station_c}\t{self.station_d}\n" +\
                   f"RED: \n\t{self.station_e}\t{self.station_f}\n"

        self.assertEqual(str_line, str(self.lines))


class TestTrain(unittest.TestCase):
    """
    Test all of the Train functions
    """
    station_a = Station("a", 0.5)
    train = Train("1", "BLUE", "S", station_a)

    def test_init(self):
        self.assertEqual("1", self.train.name)
        self.assertEqual("BLUE", self.train.line_name)
        self.assertEqual("S", self.train.direction)
        self.assertEqual(self.station_a, self.train.station)

    # def get_trains(lines) could not be tested since it produces random attributes
    # but since it creates train objects, we could only check if the create object has the appropriate attributes
    def test_str(self):
        self.assertEqual("Train 1 on BLUE line is at station A heading in South direction. ", str(self.train))


class RailwaySystem(unittest.TestCase):
    """
    Test all of the RailwaySystem Functions
    """
    # Station objects
    station_a = Station("a", 0.5)
    station_b = Station("B", 0.001)
    station_c = Station("C", 0.02)
    station_d = Station("D", 0.09)
    station_e = Station("E", 0.04)
    station_f = Station("F", 0)
    stations = [station_a, station_b, station_c, station_d, station_e, station_f]

    # Rail objects
    rail_1 = Rail(station_a, station_b, "blue", "s")
    rail_2 = Rail(station_b, station_c, "blue", "S")
    rail_3 = Rail(station_d, station_c, "blue", "n")
    rail_4 = Rail(station_e, station_f, "red", "s")

    # Line objects
    connections = [rail_1, rail_2, rail_3, rail_4]
    lines = Lines(connections)

    # Train objects
    train_1 = Train("1", "BLUE", "S", station_a)
    train_2 = Train("2", "BLUE", "S", station_b)
    train_3 = Train("3", "RED", "S", station_f)
    trains = [train_1, train_2, train_3]

    railway_system = RailwaySystem(lines, trains, stations)

    # def _init is just simple no need to test

    def test_update_train_direction(self):
        train_on_north_edge = Train("3", "BLUE", "N", self.station_a)
        self.railway_system.update_train_direction(train_on_north_edge)
        self.assertEqual(train_on_north_edge.direction, "S")

    def update_all_train_directions(self):
        # Station F is the southernmost edge, facing south -> should be updated to north
        self.railway_system.update_all_train_directions()
        self.assertEqual(self.railway_system.trains[2].direction, "N")

    def test_simulate_one_step(self):
        self.railway_system.simulate_one_step()
        # Train3 from station_f (no delay) should move to station_e
        self.assertEqual(self.railway_system.trains[2].station, self.station_e)

    def get_train_info(self):
        self.assertEqual("Train 3 on RED line is at station E heading in South direction. ", self.get_train_info(3))

    def test_create_graph(self):
        graph = {"A": ["B"],
                 "B": ["A", "C"],
                 "C": ["B", "D"],
                 "D": ["C"],
                 "E": ["F"],
                 "F": ["E"],
                 }
        self.assertEqual(graph, self.railway_system.create_graph())

    def test_get_route_info(self):
        # Unreachable/Unconnected
        self.assertEqual(f"\nStation D is not reachable from station F.",
                            self.railway_system.get_route_info("F", "D", 5))
        # Connected but lacks timesteps
        self.assertEqual(f"\nStation D is not reachable from station A within 2 timesteps.",
                    self.railway_system.get_route_info("A", "D", 2))
        # Connected and sufficient timesteps
        self.assertEqual(f"\nStation D is reachable from station A within 3 timesteps.",
            self.railway_system.get_route_info("A", "D", 3))


if __name__ == '__main__':
    unittest.main()
