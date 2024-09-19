from pydantic import BaseModel, Field
from typing import List, Optional


class Package(BaseModel):
    name: str
    epoch: Optional[int] = None
    version: str
    release: str
    arch: str
    disttag: str
    buildtime: int
    source: str


class PackageData(BaseModel):
    packages: List[Package]
