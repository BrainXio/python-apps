
import click

@click.group()
def cli():
    pass

@click.command()
def hello():
    click.echo("Hello from CLI!")

cli.add_command(hello)

if __name__ == "__main__":
    cli()
