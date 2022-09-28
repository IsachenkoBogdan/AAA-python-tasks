from keyword import iskeyword


class ColorizeMixin:
    """
    Mixin class which, when inherited, 
    changes the color of __str__ result to yellow.
    """
    def __str__(self) -> str:
        return f"\033[1;{self.repr_color_code}m{self.__repr__()}"


class NestedAttribute:
    """
    Inside-class for attributes of Advert.
    """
    def __init__(self, dictionary: dict):
        self.__dict__ = \
            {k + '_' * iskeyword(k): NestedAttribute(v) if isinstance(v, dict)
             else v for k, v in dictionary.items()}


class Advert(ColorizeMixin, NestedAttribute):
    """
    creates ad advert-objects
    with dynamic attributes and the following conditions:
    
    1) 'title' attribute exists at creation
    2) 'price' attribute is non-negative
    
    if the nested attribute name is a keyword, 
    then the attribute is created with the suffix '_'
    """
    repr_color_code: int = 33

    def __init__(self, dictionary: dict):
        super().__init__(dictionary)
        if 'title' not in self.__dict__.keys():
            raise AttributeError('Advert object must have a title attribute')
        self.price: int = self.__dict__.get('price', 0)

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, value: int):
        if value < 0:
            raise ValueError('Price must be >= 0')
        self._price = value

    def __repr__(self) -> str:
        return f'{self.title} | {self.price} ₽'
