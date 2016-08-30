#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from setuptools import setup

setup(
    name = "pylyrics3",
    version = "0.1.0",
    install_requires = ['beautifulsoup4>=4.0.0',
                        'requests>=2.0.0'],
    py_modules = ['pylyrics3'],

    # metadata for upload to PyPI
    author = "James Wenzel",
    author_email = "wenzel.james.r@gmail.com",
    description = "This is a package that downloads lyrics from LyricWiki.",
    keywords = ["lyrics", "pylyrics", "lyricwiki", "music"],
    url = "https://github.com/jameswenzel/Lyric-Wiki-Scraper",
    download_url = "https://github.com/jameswenzel/Lyric-Wiki-Scraper/tarball/0.1",
    license = "Apache License, Version 2.0"
)
