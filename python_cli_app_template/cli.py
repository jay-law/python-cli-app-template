import click


@click.group
def actions():
    pass


@click.command()
def create():
    click.echo("create")


@click.command()
def read():
    click.echo("read")


@click.command()
def update():
    click.echo("update")


@click.command()
def delete():
    click.echo("delete")


actions.add_command(create)
actions.add_command(read)
actions.add_command(update)
actions.add_command(delete)


def main():
    actions()


if __name__ == "__main__":
    main()
