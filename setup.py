"""
инсталятор
"""

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='django_gii_blog',
    version='0.0.1',
    author='Ильнур Гайфутдинов',
    author_email='ilnurgi87@gmail.com',
    description='Блог',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ilnurgi/вофтпщ_пшш_идщп/',
    packages=setuptools.find_packages(),
)
