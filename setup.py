from setuptools import setup

setup(
    name="tracim_api",
    version="0.1.0",
    packages=["tracim_api"],
    install_requires=[
        "requests",
        "types-requests"
    ],
    extras_require={
        "dev": [
            "isort"
            "flake8",
            "ruff",
            "mypy",
            "black"
        ],
    },
)