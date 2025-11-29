from setuptools import setup, find_packages

setup(
    name="proyecto-ci-cd",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "python-dateutil>=2.8.2",
        "requests>=2.31.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "bandit>=1.7.5",
            "black>=23.7.0",
            "flake8>=6.0.0",
        ],
    },
    python_requires=">=3.9",
    author="Tu Nombre",
    author_email="tu.email@example.com",
    description="Proyecto CI/CD Pipeline Multi-Plataforma",
    keywords="ci-cd, python, github-actions",
)
