from setuptools import setup

setup(
    name="classifier",
    version="1.4",
    description="Classify the files in your Downloads folder into suitable destinations.",
    url="http://github.com/bhrigu123/classifier",
    author="Bhrigu Srivastava",
    author_email="captain.bhrigu@gmail.com",
    license='MIT',
    install_requires=['click'],
    packages=["classifier"],
    package_dir={'classifier': 'classifier'},
    entry_points={
        'console_scripts': [
            'classifier = classifier.cli:main',
        ]
    },
    include_package_data=True,
    zip_safe=False
)
