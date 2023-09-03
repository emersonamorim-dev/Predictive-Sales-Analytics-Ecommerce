from setuptools import setup, find_packages

setup(
    name='Predictive-Sales-Analytics-Ecommerce',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'dash',
        'dash-bootstrap-components',
        'pandas',
        'plotly',
        'scikit-learn',
        'pyarrow',
        'pyspark' 
    ],
    entry_points={
       'console_scripts': [
           'Predictive-Sales-Analytics-Ecommerce=Predictive-Sales-Analytics-Ecommerce.main:main',
       ],
    },
)