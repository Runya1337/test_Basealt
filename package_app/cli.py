import argparse
import json
from .api import fetch_packages

def main():
    parser = argparse.ArgumentParser(description="Fetch and compare package data from two branches.")
    parser.add_argument('--branch1', type=str, default="p10", help='First branch to fetch data for')
    parser.add_argument('--branch2', type=str, default="sisyphus", help='Second branch to fetch data for')
    args = parser.parse_args()

    try:
        packages_branch1 = fetch_packages(args.branch1)
        packages_branch2 = fetch_packages(args.branch2)
    except Exception as e:
        print(f"An error occurred: {e}")