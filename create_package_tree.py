import os
import sys
import shutil
from pathlib import Path
import subprocess

def create_package_tree(package_name, autor="Seu Nome"):
    # Crie o diretório do pacote
    os.makedirs(package_name, exist_ok=True)
    os.makedirs(f"{package_name}/{package_name}", exist_ok=True)  # Diretório para o código do pacote

    gitignore_path = ".gitignore"
    setup_content_path = f"{package_name}/setup.py"
    readme_path = f"{package_name}/README.md"
    license_path = f"{package_name}/LICENSE"

    if not os.path.exists('./__init__.py'):
        print("Arquivo não existe")
        # Crie o arquivo __init__.py dentro do diretório do pacote
        with open(f"{package_name}/{package_name}/__init__.py", 'w') as f:
            f.write(f"# {package_name} - Pacote Python\n")

    # Crie o arquivo setup.py
    setup_content = f"""from setuptools import setup, find_packages

setup(
    name="{package_name}",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="{autor}",
    author_email="seu@email.com",
    description="Descrição do pacote {package_name}",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seu_usuario/{package_name}",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
"""

    if not os.path.exists(setup_content_path):
        with open(setup_content_path, 'w') as f:
            f.write(setup_content)

    # Crie o arquivo README.md
    readme_content = f"""# {package_name}

Este é o pacote `{package_name}`. Adicione aqui uma descrição mais detalhada do seu pacote.
"""
    if not os.path.exists(readme_path):
        print("Arquivo não existe")
    with open(readme_path, 'w') as f:
        f.write(readme_content)

    # Crie o arquivo LICENSE (pode adicionar uma licença como MIT ou qualquer outra)
    license_content = """MIT License

Copyright (c) 2025 Seu Nome

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
    with open(license_path, 'w') as f:
        f.write(license_content)

    # Arquivo .gitignore (se necessário)
    gitignore_content = """*.pyc
__pycache__
dist/
build/
*.egg-info
"""
    if not os.path.exists(gitignore_path):
        print("Arquivo não existe")
        with open(gitignore_path, 'w') as f:
            f.write(gitignore_content)

    print(f"Estrutura do pacote '{package_name}' criada com sucesso!")

def criar_pacote_whl(diretorio_projeto):
    # Verifique se o diretório do projeto existe
    if not os.path.isdir(diretorio_projeto):
        print(f"Erro: O diretório {diretorio_projeto} não existe!")
        return

    # Navegue até o diretório do projeto
    os.chdir(diretorio_projeto)

    # Verifique se o arquivo setup.py está presente
    if not os.path.isfile("setup.py"):
        print("Erro: O arquivo 'setup.py' não encontrado no diretório.")
        return

    print(f"Gerando o pacote .whl para o projeto '{diretorio_projeto}'...")

    # Execute o comando para gerar o pacote .whl usando setuptools e wheel
    try:
        subprocess.check_call([sys.executable, "setup.py", "bdist_wheel"])
        print("Pacote .whl gerado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao gerar o pacote: {e}")

if __name__ == "__main__":
    # Verifica se o nome do pacote foi fornecido como argumento
    if len(sys.argv) < 2:
        print("Uso: python create_package_tree.py <package_name> [autor]")
    else:
        package_name = sys.argv[1]
        # Verifica se o autor foi fornecido como o segundo argumento
        autor = sys.argv[2] if len(sys.argv) > 2 else "Seu Nome"
        create_package_tree(package_name, autor)

        # Move arquivos
        path = Path("./")
        destination = f"{package_name}/{package_name}/"
        for file in path.iterdir():
            if str(file).startswith(".") or str(file) == "__pycache__" or str(file) == package_name or str(file) == "create_package_tree.py":
                pass
            else:
                origin = f"./{file}"
                shutil.move(str(origin), str(destination))

    criar_pacote_whl(package_name)

