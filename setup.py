from setuptools import setup
import ezflags

readme = ""
with open("README.rst") as f:
    readme = f.read()

extras_require = {
    'docs': [
        'sphinx',
        'sphinx-rtd-theme'
    ]
}

setup(
    name="ezflags",
    version=ezflags.__version__,
    packages=["ezflags"],
    url="https://github.com/karx1/ezflags",
    project_urls={
        "Documentation": "https://ezflags.readthedocs.io/en/latest"
    },
    license="MIT",
    author="karx",
    author_email="nerdstep710@gmail.com",
    description="A tool that makes creating command line flags super easy.",
    long_description=readme,
    python_requires=">=3.2",
    extras_require=extras_require,
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
)
