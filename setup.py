from setuptools import setup

setup(
    name='collate',
    version='1.0',
    py_modules=['collatemd'],
    install_requires=[
        # list dependencies here if needed, e.g.,
        # 'requests',
    ],
    entry_points={
        'console_scripts': [
            'collate = collatemd:main',
        ],
    }
)
