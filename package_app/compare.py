from packaging.version import parse

def compare_packages(first_branch_data, name_first_branch, second_branch_data, name_second_branch):
    packages_from_first_branch = {pkg['name']: pkg for pkg in first_branch_data['packages']}
    packages_from_second_branch = {pkg['name']: pkg for pkg in second_branch_data['packages']}

    in_first_not_second = set(packages_from_first_branch) - set(packages_from_second_branch)
    in_second_not_first = set(packages_from_second_branch) - set(packages_from_first_branch)

    results_by_arch = {
        arch: {
            f'in_{name_first_branch}_not_{name_second_branch}': [pkg for pkg in in_first_not_second if packages_from_first_branch[pkg]['arch'] == arch],
            f'in_{name_second_branch}_not_{name_first_branch}': [pkg for pkg in in_second_not_first if packages_from_second_branch[pkg]['arch'] == arch],
        }
        for arch in set(pkg['arch'] for pkg in first_branch_data['packages'] + second_branch_data['packages'])
    }

    return results_by_arch