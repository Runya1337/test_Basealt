from packaging.version import parse

def compare_packages(first_branch_data, second_branch_data):
    packages_from_first_branch = {pkg['name']: pkg for pkg in first_branch_data['packages']}
    packages_from_second_branch = {pkg['name']: pkg for pkg in second_branch_data['packages']}

    in_p10_not_sisyphus = set(packages_from_first_branch) - set(packages_from_second_branch)
    in_sisyphus_not_p10 = set(packages_from_second_branch) - set(packages_from_first_branch)

    results_by_arch = {
        arch: {
            'in_p10_not_sisyphus': [pkg for pkg in in_p10_not_sisyphus if p10_packages[pkg]['arch'] == arch],
            'in_sisyphus_not_p10': [pkg for pkg in in_sisyphus_not_p10 if sisyphus_packages[pkg]['arch'] == arch],
        }
        for arch in set(pkg['arch'] for pkg in p10_data['packages'] + sisyphus_data['packages'])
    }

    return results_by_arch