"""
This module implements parent and child transport classes that can calculate
the cost and time of a trip.
It also includes a function to get an integer distance input from the user to
calculate the travel time and cost for that distance on different
types of transport.
"""
from enum import Enum


class Transport:
    """Parent class representing basic properties of a mode of transport
    and calculating travel time.
    """

    kind_of_transport = "Transport"
    extra_travel_time = 0

    def __init__(self, speed: float, count_of_seats: int) -> None:
        """Initializes a new instance of the Transport class.

        Args:
        speed (float): The speed of the transport in km/h.
        count_of_seats (int): The number of seats in the transport.
        """
        self.speed = speed
        self.count_of_seats = count_of_seats

    def display_info(self) -> str:
        """Returns a string containing the main parameters of the transport.

        Returns:
        str: A string containing the transport's kind, speed,
        and count of seats.
        """
        info = []
        info.append(f"Kind of transport: {self.kind_of_transport}")
        info.append(f"Speed: {self.speed} km/h")
        info.append(f"Count of seats: {self.count_of_seats}")
        return "\n".join(info)

    def calculate_travel_time(self, distance: float) -> float:
        """Calculates the time it will take to travel a given distance
        at the transport's speed.

        Args:
        distance (float): The distance to be traveled.
        Returns:
        float: The time it will take to travel the distance in minutes.
        """
        travel_time = (distance / self.speed + self.extra_travel_time) * 60
        return travel_time


class WagonType(Enum):
    """A simple enumeration representing different types of wagons."""
    compartment = {'ticket_price': 0.05}
    sitting = {'ticket_price': 0.03}


class Train(Transport):
    """The train class is a child class of transport and inherits its
    attributes and methods, and also has additional attributes and a method for
    calculating the cost of the trip.
    """

    kind_of_transport = "Train"
    extra_travel_time = 0.5   # add 30 minutes for stops

    def __init__(self, speed: float, count_of_wagons: int = 10,
                 wagon_type: str = None, count_seats_per_wagon: int = 40,
                 bed_linen_cost: float = 0) -> None:
        super().__init__(speed, count_seats_per_wagon * count_of_wagons)
        self.count_of_wagons = count_of_wagons
        self.wagon_type = wagon_type
        self.count_seats_per_wagon = count_seats_per_wagon
        self.bed_linen_cost = bed_linen_cost

    def get_travel_cost(self, distance: float) -> float:
        """Calculates the cost of the trip, taking into account the class of the wagon.

        Args:
            distance (float): The distance to be traveled.
        Returns:
            float: The cost of the trip in dollars.
        """

        for wagon in WagonType:
            if self.wagon_type == wagon.name:
                total_cost_travel = wagon.value['ticket_price'] * distance \
                                    + self.bed_linen_cost
                break
        else:
            total_cost_travel = 0

        return round(total_cost_travel, 2)


class Airplane(Transport):
    """
    The aircraft class is a child of the transport class and inherits its
    attributes and methods, and also has additional attributes and a method for
    calculation of the cost of the trip, as well as informs about the
    additional cost of baggage
    """

    kind_of_transport = "Airplane"
    extra_travel_time = 1   # add 1 hour for check-in and security
    airline_surcharge = 3

    def __init__(self, speed, count_of_seats, fuel_cost_for_one_km,
                 cost_per_kilogram_of_baggage) -> None:
        """
        Initializes the attributes of the Airplane object.

        Args:
        speed (int): The speed of the airplane in kilometers per hour.
        count_of_seats (int): The number of seats in the airplane.
        fuel_cost_for_one_km (float): The fuel cost for one kilometer of travel.
        cost_per_kilogram_of_baggage (float): The cost per kilogram of baggage.
        """
        super().__init__(speed, count_of_seats)
        self.fuel_cost_for_one_km = fuel_cost_for_one_km
        self.cost_per_kilogram_of_baggage = cost_per_kilogram_of_baggage

    def get_travel_cost(self, distance) -> float:
        """
        Calculates the cost of the trip, taking into account the cost of fuel
        and the airline's surcharge.

        Args:
        distance (float): The distance of the trip in kilometers.
        Returns:
        float: The cost of the trip.
        """
        total_cost_travel = ((self.fuel_cost_for_one_km * distance) /
                             self.count_of_seats) * self.airline_surcharge

        return round(total_cost_travel, 2)

    def cost_kilogram_of_baggage(self) -> str:
        """
        Informs about the additional cost of baggage

        Returns:
        str: A string containing the cost per kilogram of baggage.
        """
        return(f"The price of one kg of luggage: "
               f"${self.cost_per_kilogram_of_baggage}")


def get_transport_options(distance: float, train_compartment: Train,
                          train_sitting: Train, airplane: Airplane) -> dict:
    """
    Returns a dictionary of options for different types of transportation
    for the given distance.

    Args:
    distance (float): The distance of the trip in kilometers.
    train_compartment (Train): A Train object representing a compartment train.
    train_sitting (Train): A Train object representing a sitting train.
    airplane (Airplane): An Airplane object representing an airplane.
    Returns:
    dict: A dictionary containing information about the travel time, cost, and
    """
    train_compartment_time = train_compartment.calculate_travel_time(
        distance)
    train_compartment_travel_time = converting_time_to_hours_minutes(
        train_compartment_time)
    train_compartment_cost = train_compartment.get_travel_cost(
        distance)

    train_sitting_time = train_sitting.calculate_travel_time(distance)
    train_sitting_travel_time = converting_time_to_hours_minutes(train_sitting_time)
    train_sitting_cost = train_sitting.get_travel_cost(distance)

    airplane_time = airplane.calculate_travel_time(distance)
    airplane_travel_time = converting_time_to_hours_minutes(airplane_time)
    airplane_cost = airplane.get_travel_cost(distance)

    options = {
        "train compartment": {"time": train_compartment_travel_time,
                              "cost": train_compartment_cost,
                              "info": train_compartment.display_info()},
        "train sitting": {"time": train_sitting_travel_time,
                          "cost": train_sitting_cost,
                          "info": train_sitting.display_info()},
        "airplane": {"time": airplane_travel_time,
                     "cost": airplane_cost,
                     "info": airplane.display_info()},
    }

    return options


def converting_time_to_hours_minutes(travel_time: float) -> str:
    """
    Convert travel time in minutes to hours and minutes.

    Args:
    travel_time (int): The travel time in minutes.
    Returns:
    str: A string representation of the travel time in hours and minutes.
    """
    hours = travel_time // 60
    minutes = travel_time % 60
    return f"{round(hours)}h {round(minutes)}m"


def get_input_float_from_user() -> float:
    """
    Get input distance in kilometers from the user and validate the input.

    Returns:
        float: The distance in kilometers entered by the user.
    """
    while True:
        try:
            value = float(input("Enter the distance you need to cover (km): "))
            return value
        except ValueError:
            print("Input Error! Enter a number.")


def print_transport_option(options: dict, key: str) -> None:
    """
    Print trip data for the user.

    Args:
    options (dict): A dictionary containing the different transport options.
    key (str): The key of the transport option to display.
    Returns:
    None
    """
    print("\n--------------------------\n")
    print(f"{key.capitalize()}:\nTime - {options[key]['time']} "
          f"\nCost - ${options[key]['cost']}")
    print("\nAdditional information:")
    print(options[key]['info'])


def main() -> None:
    """
    Compare travel time and cost of travel by different kinds of transport
    for a given distance.

    Returns:
        None
    """
    train_compartment = Train(80, 14, "compartment", 40, 20)
    train_sitting = Train(100, 8, "sitting", 60)
    airplane = Airplane(400, 300, 1.6, 2)

    print("Compare travel time and cost of travel by different kinds of transport")

    distance = get_input_float_from_user()
    options = get_transport_options(distance, train_compartment,
                                    train_sitting, airplane)

    print("\n~ Transport options ~")
    print_transport_option(options, "train compartment")
    print_transport_option(options, "train sitting")
    train_sitting.display_info()
    print_transport_option(options, "airplane")
    print(airplane.cost_kilogram_of_baggage())


if __name__ == "__main__":
    main()

