from setuptools import setup, find_packages

setup(
    name='langchainbridge',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'langchain-google-genai',
        'langchain-openai',
        'langchain-anthropic',
        'requests'
    ],
    description='A unified wrapper for various LLM providers using LangChain.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Mahesh Awasare',
    author_email='maheshawasare@gmail.com',
    url='https://github.com/MaheshAwasare/langchainbridge',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
