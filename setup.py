import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TicTac Game",
    version="0.0.1",
    author="Nikhil Kulkarni",
    author_email="nikhilkulkarni4013@gmail.com",
    description="Now you can enjoy the game of TicTac with CLI App!!!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nikhilrkulkarni/TicTac_game",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
