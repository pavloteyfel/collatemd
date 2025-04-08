from setuptools import setup

setup(
    name='collate',
    version='1.0',
    py_modules=['collate'],
    install_requires=[
        # list dependencies here if needed, e.g.,
        # 'requests',
    ],
    entry_points={
        'console_scripts': [
            'collate = collate:main',
        ],
    }
)
