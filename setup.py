from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

packages = find_packages(exclude=['tests*'])

setup(
    name='chaturbate_api',
    version='0.0.1',
    license='LGPLv3',

    author='SpinPool',
    description='Api for search on Chaturbate',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SpinPool/Chaturbate-API',

    packages=packages,
    include_package_data=True,

    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],

    python_requires='>=3.7',
    install_requires=[
        'requests',
        'bs4'
    ],
)
