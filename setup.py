from setuptools import setup, find_packages



VERSION = '0.4'
DESCRIPTION = "GeminiAI-Chat enables easy integration of AI Chat functionalities into Python projects."


# Setting up
setup(
    name="geminiai-chat-python",
    version=VERSION,
    author="mominiqbal1234",
    author_email="<mominiqbal1214@gmail.com>",
    description=DESCRIPTION,
    long_description="""
    
### Downloads geminiai-chat-python
[![Downloads](https://static.pepy.tech/badge/geminiai-chat-python)](https://pepy.tech/project/geminiai-chat-python)

![image](https://github.com/MominIqbal-1234/geminiai-chat-python/assets/61788052/15e838f4-d6ff-41da-b2b1-366c72c30107)

GeminiAI-Chat – the revolutionary Python library designed to power up your applications with advanced conversational AI capabilities
GeminiAI-Chat, developers can effortlessly integrate AI-driven chat functionalities into their projects,
# How to install geminiai-chat

```python
pip install geminiai-chat-python --upgrade
```
# Documentation
GeminiAI-Chat offers a seamless way to incorporate intelligent, responsive AI chat features
```python
from GeminiAIChat.core import API


res = API("your_api_key") # https://aistudio.google.com/app/apikey
res.prompt("what is python")
print(res.response())

```
## Get API KEY
https://aistudio.google.com/app/apikey
![image](https://github.com/MominIqbal-1234/geminiai-chat-python/assets/61788052/6b573d4a-5d3d-4370-96dc-eca0d327292f)



# Issues
https://github.com/MominIqbal-1234/geminiai-chat-python/issues


# Repository
https://github.com/MominIqbal-1234/geminiai-chat-python



Check Our Site : https://mefiz.com/about </br>
Developed by : Momin Iqbal



    """,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['.env']},
    install_requires=["httpx","google-generativeai","google-api-python-client"],
    keywords=['geminiai-chat-python','python', 'geminiai-chat', 'geminiai'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)