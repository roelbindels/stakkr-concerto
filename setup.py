from setuptools import setup

setup(
    name='StakkrConcerte',
    version='3.5',
    packages=['concerto'],
    entry_points='''
        [stakkr.plugins]
        concerto=concerto.core:concerto
    '''
)
