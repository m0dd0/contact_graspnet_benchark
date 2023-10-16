import setuptools

setuptools.setup(
    name="contact_graspnet",
    version="0.0.1",
    author="Moritz Hesche",
    author_email="mo.hesche@gmail.com",
    # description="",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    # url="",
    classifiers=["Programming Language :: Python :: 3"],
    packages=setuptools.find_packages(),
    # python version == 3.7.9
    install_requires=[
        "numpy",
        # "opencv-python",
        "opencv-python-headless",
        "tensorflow",
        "pyyaml==5.3.1",
        "Pillow",
        "trimesh",
        "scipy",
        "pyrender==0.1.43",
        "pyglet==1.5.9",
        "tqdm",
        "matplotlib",
        # the dependencies below have been added during refactoring
        "nptyping",  # for tf tensors we use string annotations for now
        "appdirs",
        "tabulate",
        "scikit-image",
    ],
    extras_require={
        "dev": ["black", "pylint", "jupyter", "ipykernel", "ipympl"],
        "visualization": ["mayavi", "pyqt5"],
    },
    include_package_data=True,
    use_scm_version=True,
)
