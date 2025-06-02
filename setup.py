import os
from typing import List

import setuptools


# requirements
def load_requirements(path: str) -> List[str]:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as requirements_file:
            return requirements_file.readlines()
    else:
        return []


setup_requirements = load_requirements('requirements-setup.txt')
install_requirements = load_requirements('requirements.txt')
test_requirements = load_requirements('requirements-test.txt')

# version
if os.path.exists('VERSION'):
    with open('VERSION', 'r', encoding='utf-8') as version_file:
        version = version_file.read()
else:
    version = '0.0.1'

# long description
with open('README.md', 'r', encoding='utf-8') as readme_file:
    long_description = readme_file.read()

# setup
setuptools.setup(
    name='plant-image-classification',
    version=version,
    license='tbd',
    author='AnhaltAI',
    author_email='christian.haenig@hs-anhalt.de',
    url='http://www.anhalt.ai',
    description='Image classification models for plant detection.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(where='src'),
    package_dir={"": 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    setup_requires=setup_requirements,
    install_requires=install_requirements,
    tests_require=test_requirements,
)
