import setuptools

setuptools.setup(name='user_tweet_downloader',
      version="1.0.1",
      url = "https://github.com/AdriaPadilla/user_tweet_downloader", 
      description='Download the 3.200 most recent tweets of any Twitter public account',
      author='Adrian Padilla',
      author_email='adrian.padilla.m@gmail.com',
      packages=setuptools.find_packages(),
      install_requires=["TwitterAPI", "pandas", "openpyxl"],
      classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
       ],
     )