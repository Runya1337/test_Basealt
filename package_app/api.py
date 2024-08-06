import requests

def fetch_packages(branch):
    url = f"https://rdb.altlinux.org/api/export/branch_binary_packages/{branch}"
    response = requests.get(url)
    response.raise_for_status()
    packages = response.json()

    return packages
