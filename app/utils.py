from datetime import datetime

class Console:

    @staticmethod
    def line():

        print("=" * 70)

    @staticmethod
    def title(text):

        print()

        Console.line()

        print(text)

        Console.line()

    @staticmethod
    def info(text):

        print(f"ℹ {text}")

    @staticmethod
    def success(text):

        print(f"✅ {text}")

    @staticmethod
    def warning(text):

        print(f"⚠ {text}")

    @staticmethod
    def error(text):

        print(f"❌ {text}")

    @staticmethod
    def now():

        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")