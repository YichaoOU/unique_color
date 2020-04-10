from setuptools import setup, find_packages

setup(
    name='unique_color',
    version='1.0',
    author='Yichao Li',
    author_email='yl079811@ohio.edu',
    url='https://github.com/YichaoOU/unique_color',
	packages=['unique_color'],
    license='LICENSE',
    description='Provide 33 unique colors in hex or rgb format',
	long_description=long_description,
	long_description_content_type='text/markdown'	,
)


# python setup.py sdist
# python setup.py bdist_wheel --universal
# test the distributions
# twine upload dist/*