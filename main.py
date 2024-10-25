import signal
import sys
from command_parser import read_command, HELP_TEXT


def shutdown_handler():
    print("\nShutdown signal received...")
    cleanup()
    sys.exit(0)


def cleanup():
    print("Cleaning up...")
    # TODO : Implement cleanup to move in memory hash indices to disk


def main():
    signal.signal(signal.SIGINT, shutdown_handler)
    
    print("DB is running... Press Ctrl + C to exit", end='\n\n')
    print(HELP_TEXT, end="\n\n")
    
    try:
        while True:
            read_command()
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        cleanup()
        sys.exit(1)


if __name__ == "__main__":
    main()