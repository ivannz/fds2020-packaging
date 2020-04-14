from setuptools import setup

setup(
    name='example7',
    version='0.1',
    packages=[
        'project',
        'project.data',
        'project.model',
        # 'project.model.tools',
    ],
    package_data={
        'project.data': [
            'samples/default.npz',
            'samples/template.json',
        ]
    },
)
