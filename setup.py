import setuptools, json

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("info.txt", "r") as f:
    info = json.loads(f.readline())
    ver = info['version']
    desc = info['desc']

with open("info.txt", "w") as f:
    newver = ver.split(".")
    last = newver[2]
    newver[2] = str(int(last)+1)
    info['version'] = newver
    f.write(json.dumps(info))

setuptools.setup(
    name="Num2Kor",
    version=ver,
    author="Steve28",
    author_email="holiday28784@gmail.com",
    description=desc,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pl-Steve28-lq/Num2Kor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
