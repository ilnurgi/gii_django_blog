"""
инсталятор
"""

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt') as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name='gii_django_blog',
    version='0.0.40',
    author='Ильнур Гайфутдинов',
    author_email='ilnurgi87@gmail.com',
    description='Блог',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ilnurgi/gii_django_blog/',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=requirements,
)
