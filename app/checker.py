import shutil
import sys
from config import TWITTER_AUTH_TOKEN
from utils import Console


def check_python():

    Console.title("CHECK PYTHON")

    version = sys.version.split()[0]

    Console.success(f"Python {version}")


def check_node():

    Console.title("CHECK NODEJS")

    if shutil.which("node"):

        Console.success("NodeJS ditemukan")

    else:

        Console.error("NodeJS belum terinstall")

        exit()


def check_npx():

    Console.title("CHECK NPX")

    if shutil.which("npx"):

        Console.success("NPX ditemukan")

    else:

        Console.error("NPX tidak ditemukan")

        exit()


def check_token():

    Console.title("CHECK TOKEN")

    if TWITTER_AUTH_TOKEN.strip() == "":

        Console.error("Twitter Auth Token masih kosong")

        exit()

    Console.success("Twitter Token tersedia")


def run_all():

    check_python()

    check_node()

    check_npx()

    check_token()