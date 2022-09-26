from keyword import iskeyword


class ColorizeMixin:
    def __str__(self):
        return f"\033[1;{self.repr_color_code}m{self.__repr__()}"


class Advert(ColorizeMixin):
    repr_color_code = 33

    def __init__(self, dictionary: dict):
        self.__dict__ = \
            {k + '_' * iskeyword(k): Advert(v) if isinstance(v, dict) else v
             for k, v in dictionary.items()}
        self.price = self.__dict__.get('price', 0)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be >= 0")
        self._price = value

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'
