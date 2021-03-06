from setuptools import setup
from distutils.core import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='alvonCV',  # How you named your package folder (MyLib)
    packages=['alvonCV'],  # Chose the same as "name"
    version='0.2.1',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Computer Vision Helper Package',  # Give a short description about your library
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Deepak Singh',  # Type in your name
    author_email='deepaksinghgs30@gmail.com',  # Type in your E-Mail
    url='https://github.com/alvon-X/alvonCV',  # Provide either the link to your github or to your website
    download_url='https://github.com/alvon-X/alvonCV/archive/refs/tags/v_02.tar.gz',  # I explain this later on
    keywords=['Computer Vision', 'Face Mesh', 'Face Detection', 'alvon'],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        'opencv-python',
        'mediapipe',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3.6',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
