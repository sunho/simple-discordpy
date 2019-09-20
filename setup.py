import setuptools

setuptools.setup(
     name='simple-discordpy',  
     version='0.1',
     author="Sunho Kim",
     author_email="ksunhokim123@naver.com",
     description="Hello world",
     long_description="Helloooo world",
     long_description_content_type="text/markdown",
     url="https://github.com/sunho/simple-discordpy",
     packages=["sd"],
     install_requires=[    
         "discord.py"
     ],
     classifiers=[
         "License :: OSI Approved :: MIT License",
     ],
 )