from packaging.version import parse
from typing import Dict
from .models import PackageData, Package

def compare_packages(first_branch_data: PackageData, name_first_branch: str, 
                     second_branch_data: PackageData, name_second_branch: str) -> Dict[str, Dict]:
    packages_from_first_branch = {pkg.name: pkg for pkg in first_branch_data.packages}
    packages_from_second_branch = {pkg.name: pkg for pkg in second_branch_data.packages}

    in_first_not_second = set(packages_from_first_branch) - set(packages_from_second_branch)
    in_second_not_first = set(packages_from_second_branch) - set(packages_from_first_branch)
    common_packages = set(packages_from_first_branch) & set(packages_from_second_branch)
    
    results_by_arch = {
        arch: {
            f'in_{name_first_branch}_not_{name_second_branch}': [pkg for pkg in in_first_not_second if packages_from_first_branch[pkg].arch == arch],
            f'in_{name_second_branch}_not_{name_first_branch}': [pkg for pkg in in_second_not_first if packages_from_second_branch[pkg].arch == arch],
            f'ver-release_packages_more_{name_second_branch}_than_{name_first_branch}': [pkg for pkg in common_packages if packages_from_second_branch[pkg].arch == arch and version_compare(packages_from_first_branch[pkg], packages_from_second_branch[pkg]) == -1]
        }
        for arch in set(pkg.arch for pkg in first_branch_data.packages + second_branch_data.packages)
    }

    return results_by_arch

def version_compare(pkg1: Package, pkg2: Package) -> int:
    if pkg1.release > pkg2.release:
        return 1
    elif pkg1.release < pkg2.release:
        return -1
    return 0