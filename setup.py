from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

VERSION = "0.0.1"
DESCRIPTION = 'First of its Kind Programming Language - Codesi'

setup(
    name="codesi-lang",
    version=VERSION,
    author="Rishaank Gupta",
    author_email="site.rishaank@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/codesi-lang",
    packages=find_packages(),
    install_requires=[],  
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=3.0.0',
            'black>=22.0.0',
            'flake8>=4.0.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'codesi=codesi.cli:main',
            'cds=codesi.cli:main',  
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Interpreters",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Natural Language :: Hindi",
        "Natural Language :: English",
    ],
    keywords=[
        'codesi', 'hinglish', 'hindi', 'programming-language', 
        'interpreter', 'indian', 'language', 'education'
    ],
    python_requires='>=3.7',
    include_package_data=True,
    zip_safe=False,
)