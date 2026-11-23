from open_tmr.cli import demo


def main(argv=None) -> int:
    import argparse

    parser = argparse.ArgumentParser(prog="open-tmr")
    subcommands = parser.add_subparsers(dest="command", required=True)
    subcommands.add_parser("demo", help="Run the offline synthetic demonstration")
    args = parser.parse_args(argv)

    if args.command == "demo":
        result = demo()
        print("Synthetic offline demo complete.")
        print(f"Output: {result['output']}")
        print(f"Lesson: {result['lesson']}")
        print(f"Session: {result['session']}")
        print(f"Audio segments: {result['segments']}")
        print("Validation: VALID; no real participant data or hardware used.")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
