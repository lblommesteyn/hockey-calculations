from setuptools import setup, find_packages

setup(
    name='hockey_gap_analysis',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scipy',
        'matplotlib',
        'plotly',  # Add other dependencies as needed
    ],
    author='Sean Farquson',
    author_email='lukeblommesteyn@gmail.com',
    description='A package for gap analysis in hockey games.',
    keywords='hockey analysis',
)
