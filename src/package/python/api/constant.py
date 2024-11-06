from pathlib import Path

STYLEDIR = Path(__file__).resolve().parent.parent.parent / "style"



if __name__ == "__main__":
    print(STYLEDIR)