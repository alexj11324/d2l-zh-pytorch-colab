from setuptools import find_packages, setup

requirements = [
    'jupyter>=1.0.0',
    'numpy>=2.0',
    'matplotlib>=3.8',
    'matplotlib-inline>=0.1',
    'requests>=2.31',
    'pandas>=2.2',
    'pillow>=10.0',
    'torch>=2.12',
    'torchvision>=0.27',
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
