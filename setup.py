from __future__ import annotations
from setuptools import find_packages
from setuptools import setup
# Read requirements.txt, ignore comments
try:
    REQUIRES = list()
    f = open("requirements.txt", "rb")
    for line in f.read().decode("utf-8").split("\n"):
        line = line.strip()
        if "#" in line:
            line = line[: line.find("#")].strip()
        if line:
            REQUIRES.append(line)
except FileNotFoundError:
    print("'requirements.txt' not found!")
    REQUIRES = list()


setup(
    name="fingpt",
    version="0.0.1",
    include_package_data=True,
    license="MIT",
    packages=find_packages(),
    platform=["any"],
    python_requires=">=3.7",
)
