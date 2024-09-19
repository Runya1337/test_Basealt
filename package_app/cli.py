import argparse
import json
from .api import fetch_packages
from .compare import compare_packages


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Получение и сравнение данных пакета из двух бранчей."
    )
    parser.add_argument("--branch1", type=str, default="p10", help="Первая ветка")
    parser.add_argument("--branch2", type=str, default="sisyphus", help="Вторая ветка")
    args = parser.parse_args()

    try:
        packages_branch1 = fetch_packages(args.branch1)
        with open("branch1.json", "w") as f:
            json.dump(packages_branch1.dict(), f, indent=4)
        packages_branch2 = fetch_packages(args.branch2)
        comparison_results = compare_packages(
            packages_branch1, args.branch1, packages_branch2, args.branch2
        )
        with open("comparison_results.json", "w") as f:
            json.dump(comparison_results, f, indent=4)
    except Exception as e:
        print(f"An error occurred: {e}")
