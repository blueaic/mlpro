from setuptools import setup


setup(name='mlpro',
version='2.2.1',
description='MLPro - The integrative middleware framework for standardized machine learning',
author='blueAIC',
author_mail='mlpro@blueaic.com',
license='Apache Software License (http://www.apache.org/licenses/LICENSE-2.0)',
packages=['mlpro'],

# Package dependencies for full installation
extras_require={
    "full": [
        "dill>=0.4.1",
        "multiprocess>=0.70.19",
        "numpy>=2.5.2",
        "torch>=2.7.0",
        "PySide6>=6.11.2",
        "matplotlib>=3.11.1",
        "scipy>=1.18.0",
        "pandas>=3.0.5"
    ],
},

zip_safe=False)