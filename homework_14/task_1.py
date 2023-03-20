"""
This module implements parent and child transport classes that can calculate
the cost and time of a trip.
It also includes a function to get an integer distance input from the user to
calculate the travel time and cost for that distance on different
types of transport.
"""


class Transport:
    """
    The transport class is a parent class that describes the basic properties
    of the transport and calculates the time to overcome the distance
    """
    kind_of_transport = "Transport"

    def __init__(self, speed, count_of_seats):
        self.speed = speed
        self.count_of_seats = count_of_seats

    def display_info(self):
        """ Displays the main parameters of the vehicle """
        print(f"Kind of transport: {self.kind_of_transport}")
        print(f"Speed: {self.speed} km/h")
        print(f"Count of seats: {self.count_of_seats}")

    def calculate_travel_time(self, distance):
        """
        The parameter takes the distance for which it calculates the
        time to overcome it in hours and minutes
        """
        travel_time = (distance / self.speed) * 60
        hours = travel_time // 60
        minutes = travel_time % 60
        return f"{round(hours)}h {round(minutes)}m"


class Train(Transport):
    """
    The train class is a child class of transport and inherits its attributes
    and methods, and also has additional attributes and a method for
    calculating the cost of the trip
    """
    kind_of_transport = "Train"

    def __init__(self, speed, count_of_wagons=10, wagon_type=None,
                 count_seats_per_wagon=40, bed_linen_cost=0):
        super().__init__(speed, count_seats_per_wagon * count_of_wagons)
        self.count_of_wagons = count_of_wagons
        self.wagon_type = wagon_type
        self.count_seats_per_wagon = count_seats_per_wagon
        self.bed_linen_cost = bed_linen_cost

    def get_travel_cost(self, distance):
        """
        Calculates the cost of the trip, taking into account the class of the wagon.
        """
        if self.wagon_type == "compartment":
            # approximate ticket price per kilometer for compartment
            ticket_price = 0.05
        elif self.wagon_type == "sitting":
            # approximate ticket price per kilometer for sitting car
            ticket_price = 0.03
        else:
            total_cost_travel = 0
            return total_cost_travel

        total_cost_travel = ticket_price * distance + self.bed_linen_cost

        return round(total_cost_travel, 2)

    def calculate_travel_time(self, distance):
        """
        The parameter accepts a distance for which the time to overcome
        it in hours and minutes is calculated for this type of transport
        """
        # add 30 minutes for stops
        travel_time = (distance / self.speed + 0.5) * 60
        hours = travel_time // 60
        minutes = travel_time % 60
        return f"{round(hours)}h {round(minutes)}m"


class Airplane(Transport):
    """
    The aircraft class is a child of the transport class and inherits its
    attributes and methods, and also has additional attributes and a method for
    calculation of the cost of the trip, as well as informs about the
    additional cost of baggage
    """
    kind_of_transport = "Airplane"

    def __init__(self, speed, count_of_seats, fuel_cost_for_one_km,
                 cost_per_kilogram_of_baggage):
        super().__init__(speed, count_of_seats)
        self.fuel_cost_for_one_km = fuel_cost_for_one_km
        self.cost_per_kilogram_of_baggage = cost_per_kilogram_of_baggage

    def get_travel_cost(self, distance):
        """
        Calculates the cost of the trip, taking into account the cost of fuel
        and the airline's surcharge.
        """
        total_cost_travel = ((self.fuel_cost_for_one_km * distance) / self.count_of_seats) * 3

        return round(total_cost_travel, 2)

    def cost_kilogram_of_baggage(self):
        """ informs about the additional cost of baggage """
        print(f"The price of one kg of luggage: "
              f"${self.cost_per_kilogram_of_baggage}")

    def calculate_travel_time(self, distance):
        """
        The parameter accepts a distance for which the time to overcome
        it in hours and minutes is calculated for this type of transport
        """
        # add 1 hour for check-in and security
        travel_time = (distance / self.speed + 1) * 60
        hours = travel_time // 60
        minutes = travel_time % 60
        return f"{round(hours)}h {round(minutes)}m"


def get_transport_options(distance: float, train_compartment: Train,
                          train_sitting: Train, airplane: Airplane):
    """
    The function takes an object of classes and a distance.
    Initializes the work of each class for the given distance.
    """
    train_compartment_time = train_compartment.calculate_travel_time(distance)
    train_compartment_cost = train_compartment.get_travel_cost(distance)

    train_sitting_time = train_sitting.calculate_travel_time(distance)
    train_sitting_cost = train_sitting.get_travel_cost(distance)

    airplane_time = airplane.calculate_travel_time(distance)
    airplane_cost = airplane.get_travel_cost(distance)

    options = {
        "train compartment": {"time": train_compartment_time,
                              "cost": train_compartment_cost},
        "train sitting": {"time": train_sitting_time,
                          "cost": train_sitting_cost},
        "airplane": {"time": airplane_time, "cost": round(airplane_cost, 2)},
    }

    return options


def get_input_float_from_user():
    """ Accepts a distance from the user and validates the input """
    while True:
        try:
            value = float(input("Enter the distance you need to cover (km): "))
            return value
        except ValueError:
            print("Input Error! Enter the number")


def print_transport_option(options, key):
    """ Displays trip data for the user """
    print("\n--------------------------\n")
    print(f"{key.capitalize()}:\nTime - {options[key]['time']} "
          f"\nCost - ${options[key]['cost']}")
    print("\nAdditional information:")


def main():
    """
    Creates class objects and for each class displays the calculated
    information about the time and cost of the trip for the distance received
    from the user, as well as additional information about the transport.
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
    train_compartment.display_info()
    print_transport_option(options, "train sitting")
    train_sitting.display_info()
    print_transport_option(options, "airplane")
    airplane.display_info()
    airplane.cost_kilogram_of_baggage()


if __name__ == "__main__":
    main()
