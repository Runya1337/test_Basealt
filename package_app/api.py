import requests
from .models import PackageData
from pydantic import TypeAdapter


def fetch_packages(branch: str) -> PackageData:
    url = f"https://rdb.altlinux.org/api/export/branch_binary_packages/{branch}"
    response = requests.get(url)
    response.raise_for_status()
    package_data_adapter = TypeAdapter(PackageData)
    return package_data_adapter.validate_python(response.json())
