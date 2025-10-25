import sys
import argparse
from codesi.repl import repl
from codesi.runner import run_file

__version__ = "0.0.1"

def main():
    """Main entry point for the Codesi interpreter"""
    parser = argparse.ArgumentParser(
        prog="Codesi",
        description=f"Codesi v{__version__} - The first of its kind Programming Language.",
        epilog="Made with love in India."
    )

    parser.add_argument(
        'filename',
        nargs='?',
        default=None,
        help="The path to a .cds file to execute. If not provided, the interactive REPL will start."
    )

    parser.add_argument(
        '--jaadu',
        action='store_true',
        help="Enable JAADU mode for auto-correction of common typos."
    )

    parser.add_argument(
        '-d', '--debug',
        action='store_true',
        help="Enable debug mode to see tokens and AST."
    )

    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f"%(prog)s {__version__}"
    )

    args = parser.parse_args()

    if args.filename:
        # If a filename is provided, run the file
        success = run_file(args.filename, args.debug, args.jaadu)
        sys.exit(0 if success else 1)
    else:
        # If no filename, start the REPL
        repl(jaadu_mode=args.jaadu)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted! Bye!")
        sys.exit(0)
    except Exception as e:
        print(f"Fatal Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
