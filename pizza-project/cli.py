import click
import pizza


@click.group()
def cli():
    pass


@cli.command()
@click.option("--delivery", "-d", default=False, is_flag=True)
@click.option(
    "--size",
    "-s",
    required=True,
    type=click.Choice(pizza.Pizza.sizes, case_sensitive=False),
)
@click.argument("pizza_name", nargs=1)
def order(pizza_name: str, delivery: bool, size: str) -> None:
    """prepares and delivers pizza"""
    pizza_name = pizza_name.title()
    try:
        pizza_obj = getattr(pizza, pizza_name)(size)
    except AttributeError:
        raise ValueError(f"There are no {pizza_name} in our menu")

    print(f"Your order is {pizza_obj} with size {size}")
    pizza.loggers["bake"](pizza_obj.bake)()
    if delivery:
        pizza.loggers["delivery"](pizza_obj.deliver)()
    else:
        pizza.loggers["pickup"](pizza_obj.pickup)()


@cli.command()
def menu() -> None:
    """displays a menu"""
    print(pizza.menu)


if __name__ == "__main__":
    cli()
