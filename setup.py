from setuptools import setup

from cuba_weather_redcuba import __version__

setup(
    name='cuba_weather_redcuba',
    version=__version__,
    packages=[
        'cuba_weather_redcuba',
        'cuba_weather_redcuba/data_providers',
        'cuba_weather_redcuba/models',
        'cuba_weather_redcuba/repositories',
        'cuba_weather_redcuba/utils'
    ],
    url='https://github.com/cuba-weather/cuba-weather-redcuba-python',
    license='MIT',
    author='Cuban Open Source Community',
    description='Python3 client for (https://www.redcuba.cu) weather API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['cuba-weather-municipality'],
)
