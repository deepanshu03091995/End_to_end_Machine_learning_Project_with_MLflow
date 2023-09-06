import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.readlines()

__version__ = "0.0.0"

REPO_NAME = "End_to_end_Machine_learning_Project_with_MLflow"

AUTHOR_USER_NAME = "deepanshu03091995"
SRC_REPO = "MLProject"

AUTHOR_EMAIL = "deepanshu.dlri@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Small python Package for ML App",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    package=setuptools.find_packages(where="src"),
)
