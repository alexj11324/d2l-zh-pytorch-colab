from setuptools import find_packages, setup

requirements = [
    'jupyter',
    'numpy',
    'matplotlib',
    'matplotlib-inline',
    'requests',
    'pandas',
    'pillow',
    'torch',
    'torchvision',
]

setup(
    name='d2l',
    version='1.0.3.post1',
    python_requires='>=3.10',
    author='D2L Developers',
    author_email='d2l.devs@gmail.com',
    url='https://d2l.ai',
    description='Dive into Deep Learning',
    license='MIT-0',
    packages=find_packages(),
    zip_safe=True,
    install_requires=requirements,
)
