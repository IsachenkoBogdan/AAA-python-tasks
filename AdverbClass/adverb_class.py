from keyword import iskeyword


class ColorizeMixin:
    def __str__(self) -> str:
        return f"\033[1;{self.repr_color_code}m{self.__repr__()}"


class NestedAttribute:
    def __init__(self, dictionary: dict):
        self.__dict__ = \
            {k + '_' * iskeyword(k): NestedAttribute(v) if isinstance(v, dict)
             else v for k, v in dictionary.items()}


class Advert(ColorizeMixin, NestedAttribute):
    repr_color_code: int = 33

    def __init__(self, dictionary: dict):
        super().__init__(dictionary)
        self.price: int = self.__dict__.get('price', 0)
        print(self.__dict__)

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, value: int):
        if value < 0:
            raise ValueError("Price must be >= 0")
        self._price = value

    def __repr__(self) -> str:
        return f'{self.title} | {self.price} ₽'
