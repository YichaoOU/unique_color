from setuptools import setup, find_packages

# 10 unique dark colors
# color_list=["#ad4545","#379e7d","#1c7caf","#000000","#6f1a52","#476aae","#e6521c","#e1609f","#149c98","#3b0056"]
# sns.palplot(color_list)

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
