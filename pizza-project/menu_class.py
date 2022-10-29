from helper_funcs import get_classes_from_module


class MenuObject:
    """
    class for storing the menu. Aimed at easier scalability,
    you can create menus for different food modules.

    bound_text this is what will be written above and below
    when the menu is displayed.

    bound_width - menu width
    """

    def __init__(self,
                 menu_text: str,
                 menu_width: int,
                 module_name: str,
                 food_base_class):
        """
        initializes the menu with all pizzas
        that are created as classes in this module.
        This is convenient because the end user
        does not need to think about whether
        there is a pizza on the menu - as soon as the customer adds a new pizza
        with a new recipe here as a class - everything will already work.
        In addition to this it is a separate class
        that does not shit the module
        """
        self.bound_text = menu_text
        self.bound_width = menu_width
        self.menu: dict = {}
        for cls in get_classes_from_module(module_name):
            if cls != food_base_class:
                self.update(cls)

    def update(self, eat_cls) -> None:
        self.menu.update({eat_cls.to_str(): ", ".join(eat_cls.ingredients())})

    def __str__(self) -> str:
        text = self.bound_text.center(self.bound_width, "-") + "\n"
        for position, recipe in self.menu.items():
            text += f"- {position}: {recipe}".ljust(self.bound_width) + "✅\n"
        return text + text[: self.bound_width]
