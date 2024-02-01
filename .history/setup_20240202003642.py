import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
    
__version__ = "0.0.0" 

REPO_NAME = "End-to-End-ML-Project-with-MLflow"
AUTHOR_USER_NAME = "DohGwangSun" 
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "appdoh2007@gmail.com"


setuptools.setup(
   name=REPO_NAME,
   version=__version__,
   author=AUTHOR_USER_NAME,
   author_email=AUTHOR_EMAIL,
   description="End-to-End ML Project with MLflow",
   long_description=long_description,
   long_description_content_type="text/markdown",
   url=f"https://github/{AUTHOR_USER_NAME}/{REPO_NAME}",
   project_urls={
       "Bug Tracker": f"https://github/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
   },
   package_dir = {"": "src"},
   packages=setuptools.find_packages(where="src")
)