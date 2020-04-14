from setuptools import setup

setup(
    name='CharmingCerf',
    version='0.1',
    package_dir={
        'project.core': 'src'
    },
    packages=[
        'project',
        'project.core',
    ],
)
