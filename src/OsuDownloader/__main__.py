import requests
import os
import sys
from tqdm import tqdm
import cli
from __init__ import __app_name__


def main():
    cli.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()