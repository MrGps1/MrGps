import setuptools

with open("README.md", "r", encoding="utf-8")
    long_description = fh.read()

with open("requirements.txt",'r') as fr:
    requires = fr.read().split('\n')
    
setuptools.setup(
    name="MrGps",
    version="0.0.1",
    author="MrGps1",
    author_email="author@example.com",
    description="Short EveryThing In Seconds",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MrGps",
    project_urls={
        "Bug Tracker": "https://github.com/MrGps1/MrGps/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=requires,
)
