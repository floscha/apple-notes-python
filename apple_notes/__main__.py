import sys

from apple_notes import cli


def main() -> None:
    args: list[str] = sys.argv[1:]
    cli.run(args)


if __name__ == "__main__":
    main()
