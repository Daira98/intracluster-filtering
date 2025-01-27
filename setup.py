from typing import List
import setuptools
from pathlib import Path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def get_install_requires() -> List[str]:
    """Returns requirements.txt parsed to a list"""
    fname = Path(__file__).parent / 'requirements.txt'
    targets = []
    if fname.exists():
        with open(fname, 'r') as f:
            targets = f.read().splitlines()
    return targets

setuptools.setup(
    name='intraclusterfiltering',
    version='1.1.0',
    author='Sebastian Jara, Juan Zamora, Pascal Sigel, Kerlyns Martínez',
    author_email='',
    description='Detection Intra-class Outliers with Neural Networks (DIONN) algorithm',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/juanzamorai/intracluster-filtering',
    license='MIT',
    packages=['intracluster_filtering', 'utils'],
    install_requires=get_install_requires(),
)
