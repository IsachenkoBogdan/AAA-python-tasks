from abc import ABC, abstractmethod
from time import sleep
from time_config import baking_time, delivery_time, waiting_time, chunk_size
from menu_class import MenuObject
from helper_funcs import Logging
from tqdm import tqdm

loggers = {
    "bake": Logging("Your pizza is 🔥baked🔥 in {}s"),
    "delivery": Logging("Your pizza is 🏃delivered🏃 in {}s"),
    "pickup": Logging("Your 🍕pizza🍕 is served in {}s"),
}


# convenient way to use loggers for functions from the pizza module


class Pizza(ABC):
    """
    abstract pizza class
    """

    sizes: list[str] = ["XL", "L"]

    def __init__(self, size: str):
        if size not in self.sizes:
            raise ValueError(f"There are no {size} size.")
            # raises error if somebody trying to
            # create pizza with not implemented size
        self.size = size

    @property
    @abstractmethod
    def recipes_dict(self) -> dict:
        """
        returns a dictionary from ingredients to recipe quantities with sizes
        it is abstract, because we want to prohibit to make classes of Pizza
        without recipe
        """
        return {"ingredient": "mass"}

    @property
    @abstractmethod
    def icon(self) -> str:
        """
        pizza icon in cli
        """
        return "smile"

    @abstractmethod
    def bake(self) -> None:
        """
        implements pizza baking logic
        """
        pass

    @staticmethod
    def deliver() -> None:
        """
        implements the logic of pizza delivery to the customer
        """
        # Some Delivering logic, emulating delivering time with sleep
        for _ in tqdm(range(chunk_size)):
            sleep(delivery_time / chunk_size)

    @staticmethod
    def pickup() -> None:
        """
        implements the pickup logic for the customer
        """
        # Some logic of pizza giving to customer
        for _ in tqdm(range(chunk_size)):
            sleep(waiting_time / chunk_size)

    @classmethod
    def get_name(cls) -> str:
        """
        returns the name of the pizza that the class corresponds to.
        uses for simplifications, in general, one could do without it,
        but this method can be useful when using the module
        """
        return cls.__name__

    @classmethod
    def ingredients(cls) -> list:
        """
        returns a list of ingredients in a recipe
        """
        return cls.recipes_dict[cls.sizes[0]].keys()

    @classmethod
    def to_str(cls) -> str:
        return f"{cls.get_name()} {cls.icon}"

    def dict(self) -> dict:
        """
        returns the pizza recipe as a dictionary,
        where the keys are the ingredients
        and the values are the quantity in grams
        """
        return self.recipes_dict[self.size]

    def __eq__(self, other) -> bool:
        """
        method for comparing two pizzas
        """
        return self.dict() == other.dict()

    def __str__(self):
        return self.to_str()


class Margherita(Pizza):
    icon: str = "🧀"
    recipes_dict = {
        "XL": {"tomato sauce": 100, "mozzarella": 100, "tomatoes": 100},
        "L": {"tomato sauce": 100, "mozzarella": 100, "tomatoes": 100},
    }

    def bake(self) -> None:
        # Some logic for Margherita baking
        for _ in tqdm(range(chunk_size)):
            sleep(baking_time[self.get_name()][self.size] / chunk_size)


class Pepperoni(Pizza):
    icon: str = "🍕"
    recipes_dict = {
        "XL": {"tomato sauce": 100, "mozzarella": 100, "pepperoni": 100},
        "L": {"tomato sauce": 100, "mozzarella": 100, "pepperoni": 100},
    }

    def bake(self) -> None:
        # Some logic for Pepperoni baking
        for _ in tqdm(range(chunk_size)):
            sleep(baking_time[self.get_name()][self.size] / chunk_size)


class Hawaiian(Pizza):
    icon: str = "🍍"
    recipes_dict = {
        "XL": {
            "tomato sauce": 100,
            "mozzarella": 100,
            "chicken": 100,
            "pineapples": 100,
        },
        "L": {
            "tomato sauce": 100,
            "mozzarella": 100,
            "chicken": 100,
            "pineapples": 100,
        },
    }

    def bake(self) -> None:
        # Some logic for Hawaiian baking
        for _ in tqdm(range(chunk_size)):
            sleep(baking_time[self.get_name()][self.size] / chunk_size)


menu = MenuObject(menu_text="PIZZA MENU",
                  menu_width=80,
                  module_name=__name__,
                  food_base_class=Pizza)
