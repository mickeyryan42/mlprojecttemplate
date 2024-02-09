from setuptools import find_packages, setup
from typing import List

def get_requirements(path: str)->List[str]:
    requirements=[]

    with open(path) as file:
        requirements=file.readlines()
        requirements=[line.replace("\n", "") for line in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

        return requirements

setup(
   name='mlprojecttemplate',
   version='0.0.1',
   author='Mickey Ryan',
   packages=find_packages(),
   install_requires=get_requirements('requirements.txt'),
)