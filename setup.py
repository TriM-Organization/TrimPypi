# -*- coding: utf-8 -*-
import setuptools
import Musicreater

with open("requirements.txt", "r", encoding="utf-8") as fh:
    dependences = fh.read().strip().split("
")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read().replace(
        "./docs/", "https://github.com/TriM-Organization/Musicreater/blob/master/docs/"
    )

setuptools.setup(
    name="Musicreater",
    version=Musicreater.__version__,
    author="Eilles Wan, bgArray",
    author_email="TriM-Organization@hotmail.com",
    description="һ����ѿ�Դ�� ���ҵ����硷 mid����ת���⡣
"
    "A free open-source python library used to convert midi into Minecraft.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TriM-Organization/Musicreater",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: Chinese (Simplified)",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    # ��Ҫ��װ������
    install_requires=dependences,
)