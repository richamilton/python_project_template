from setuptools import find_packages, setup

setup(
    name='template',
    version='0.0.0',
    description='A short description of your package',
    author='Richard Hamilton',
    author_email='richxrdhamilton@gmail.com',
    url='https://github.com/your_username/your_package_name',
    packages=find_packages(),
    install_requires=[
        "numpy",
    ],
    extras_require={
        "dev": [
            "black>=23.1a1",
            "flake8>=3.8.4",
            "pytest>=6.2.5",
            "pytest-cov>=2.11.1",
            "isort>=5.7.0",
            "pre-commit>=2.9.3",
            "ipython>=8.8.0",
            "ipykernel>=6.20.2",
            "ipywidgets>=7.6.3",
            "build",
            "twine",
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)