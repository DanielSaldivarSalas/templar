import typer
from copier import run_copy
import os


app = typer.Typer()

template_directory = os.environ.get("TEMPLAR_TEMPLATE_DIRECTORY")  

@app.command()
def spring(destination: str):
    template_path = f"{template_directory}/template-spring"
    target_directory = destination
    print(f"{template_path=}")
    print(f"{target_directory=}")
    run_copy(template_path, target_directory)
    

    print(f"Succesfully created spring project")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()


