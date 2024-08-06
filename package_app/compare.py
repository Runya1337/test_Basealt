from packaging.version import parse

def compare_packages(p10_data: dict, sisyphus_data) -> dict:
    p10_packages = {pkg['name']: pkg for pkg in p10_data['packages']}
    sisyphus_packages = {pkg['name']: pkg for pkg in sisyphus_data['packages']}

    in_p10_not_sisyphus = set(p10_packages) - set(sisyphus_packages)
    in_sisyphus_not_p10 = set(sisyphus_packages) - set(p10_packages)

    results_by_arch = {
        arch: {
            'in_p10_not_sisyphus': [pkg for pkg in in_p10_not_sisyphus if p10_packages[pkg]['arch'] == arch],
            'in_sisyphus_not_p10': [pkg for pkg in in_sisyphus_not_p10 if sisyphus_packages[pkg]['arch'] == arch],
        }
        for arch in set(pkg['arch'] for pkg in p10_data['packages'] + sisyphus_data['packages'])
    }

    return results_by_arch