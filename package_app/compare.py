from typing import Dict
from .models import PackageData
import re
from pkg_resources import parse_version


def compare_versions(version1: str, version2: str) -> int:
    try:
        return parse_version(version1) > parse_version(version2)
    except:
        return 0


def compare_packages(
    first_branch_data: PackageData,
    name_first_branch: str,
    second_branch_data: PackageData,
    name_second_branch: str,
) -> Dict[str, Dict]:
    packages_from_first_branch = {pkg.name: pkg for pkg in first_branch_data.packages}
    packages_from_second_branch = {pkg.name: pkg for pkg in second_branch_data.packages}

    in_first_not_second = set(packages_from_first_branch) - set(
        packages_from_second_branch
    )
    in_second_not_first = set(packages_from_second_branch) - set(
        packages_from_first_branch
    )
    common_packages = set(packages_from_first_branch) & set(packages_from_second_branch)

    results_by_arch = {
        arch: {
            f"in_{name_first_branch}_not_{name_second_branch}": [
                pkg
                for pkg in in_first_not_second
                if packages_from_first_branch[pkg].arch == arch
            ],
            f"in_{name_second_branch}_not_{name_first_branch}": [
                pkg
                for pkg in in_second_not_first
                if packages_from_second_branch[pkg].arch == arch
            ],
            f"ver-release_packages_more_{name_second_branch}_than_{name_first_branch}": [
                pkg
                for pkg in common_packages
                if packages_from_second_branch[pkg].arch == arch
                and compare_versions(
                    packages_from_second_branch[pkg].release,
                    packages_from_first_branch[pkg].release,
                )
                > 0
            ],
        }
        for arch in set(
            pkg.arch for pkg in first_branch_data.packages + second_branch_data.packages
        )
    }

    return results_by_arch
