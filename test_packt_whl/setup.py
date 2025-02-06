from setuptools import setup, find_packages

setup(
    name="test_packt_whl",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="luismacena19",
    author_email="seu@email.com",
    description="Descrição do pacote test_packt_whl",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seu_usuario/test_packt_whl",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
