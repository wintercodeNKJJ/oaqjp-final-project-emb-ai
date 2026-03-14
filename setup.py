from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="0.1.0",
    description="Python package for emotion detection using IBM Watson Emotion API",
    packages=find_packages(),
    install_requires=[
        "requests>=2.30.0"
    ],
    python_requires='>=3.7',
    author="Jordan Junior",
)