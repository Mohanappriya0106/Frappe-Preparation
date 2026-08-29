import click

@click.command()
@click.argument("name")
def hello(name):
    print(f"hello {name}!")

commands=[hello]