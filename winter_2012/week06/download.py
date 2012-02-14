"""
File downloader web clients
Solutions to week 5 lab exercise, and homework assignment options 1 and 2 are all here
"""

import os
import sys
import json
import urllib2
import urlparse
from pprint import pprint
from BeautifulSoup import BeautifulSoup


# data

# url of web page to scrape
course_url = 'http://jon-jacky.github.com/uw_python/winter_2012/index.html'

# github api v2 call to retrieve dictionary of blob name:sha from repo
course_blobs_url = 'http://github.com/api/v2/json/blob/all/jon-jacky/uw_python/gh-pages'

# github api v2 call to retrieve a particular blob, append its sha after final '/'
retrieve_blob_url = 'http://github.com/api/v2/json/blob/show/jon-jacky/uw_python/'

# building block functions

# for screen scraper using BeautifulSoup

def soup_find_urls(page_url, prefix, suffix):
    """
    return list of URLs (strings) that begin with prefix, end with suffix
    found in anchor tags in page at page_url
    set prefix or suffix to '' to accept any 
    """
    contents = urllib2.urlopen(page_url).read()
    soup = BeautifulSoup(contents)
    anchors = soup.findAll('a', attrs={'href':(lambda a: a and a.startswith(prefix)
                                               and a.endswith(suffix))})
    # anchors is list of BeautfulSoup.Tag objects
    # access tag attributes like a dictionary
    return [ str(a['href']) for a in anchors ] # extract urls and convert from unicode

def url_download(url, path):
    """
    Download contents of URL and save in file named in path
    """
    contents = urllib2.urlopen(url).read()
    f = open(path, "w")
    f.write(contents)
    f.close()
    return len(contents)

def url_download_many(nfiles, siteurl, urls):
    """
    Download files from each url in urls (list of strings)
    If url is relative, download it from siteurl (string)
    Save file in current default directory, use same file basename but omit subdirs path
    Download no more than nfiles, even if urls list is longer 
    Return number of files downloaded
    """
    surl = urlparse.urlparse(siteurl)
    dirpath = os.path.dirname(surl.path) + '/' # must add '/' suffix here
    baseurl = urlparse.urlunparse((surl.scheme, surl.netloc, dirpath,
                                   surl.params, surl.query, surl.fragment))
    for i, url in enumerate(urls):
        if i == nfiles:
            break
        purl = urlparse.urlparse(url)
        if not purl.scheme: # must be relative URL
            url = baseurl + purl.path # relative URL does not begin with '/'
        fname = os.path.basename(purl.path)
        print 'downloading from %s to %s' % (url, fname)
        url_download(url, fname)
    return nfiles


# building block functions for gibhub api

def github_find_blobs(blobs_url, prefix, suffix):
    """
    return dictionary of blob name:sha where name begins with prefix, end with suffix
    found in the blobs retrieved by blobs_url (a string), using github v2 api
    set prefix or suffix to '' to accept any 
    """
    handle = urllib2.urlopen(blobs_url)
    data = json.load(handle)
    blobs = data['blobs']
    # dictionary comprehension works in 2.7+ or 3.x
    return { str(n):str(blobs[n]) for n in blobs  # convert from unicode
             if n.startswith(prefix) and n.endswith(suffix) }

def github_download(retrieve_blob_url, sha, path):
    """
    Download file from blob in github using its sha and save in file named fname
    """
    contents = urllib2.urlopen(retrieve_blob_url + sha).read()
    f = open(path, "w")
    f.write(contents)
    f.close()
    return len(contents)

def github_download_many(nfiles, retrieve_blob_url, blobs):
    """
    Download files corresponding to each blob in blobs (dict of name:sha)
    using github api v2 command retriev_blob_url
    Save file in current default directory, use same file basename but omit subdirs path    Download no more than nfiles, even if blobs has more elements
    Return number of files downloaded
    """
    for i, name in enumerate(blobs):
        if i == nfiles:
            break
        fname = os.path.basename(name)
        print 'downloading from %s to %s' % (name, fname)
        github_download(retrieve_blob_url, blobs[name], fname)
    return nfiles


# Solutions to lab exercises and assignments, use functions above.  Also tests

def scrape(url):
    """
    Solution to week 5 lab exercise in /scrape.txt:
    'Write a script that prints every http url in a page at a given url'
    """
    pprint(soup_find_urls(url, 'http', ''))


def test_download():
    """
    Demo url_download function. Usage: python download.py url path
    """
    # defaults, use if command line arg missing
    url = 'http://localhost'
    path = 'downloaded.txt'
    # get command line args
    if len(sys.argv) > 1:
        url = sys.argv[1]
    if len(sys.argv) > 2:
        path = sys.argv[2]
    # download!
    print "%s bytes downloaded" % url_download(url, path)


def webclient1(nfiles):
    """
    Solution for week 5 assignment in webclient.txt, part 1:

    1. File downloader using screen scraping: write a script that scrapes
    our Python Winter 2012 course page for the URLs of all the Python
    source files, then downloads them all.

    This version takes one argument, nfiles, the maximum number of files to download.
    For testing set nfiles to a very small number
    """
    pyurls = soup_find_urls(course_url, '', '.py')  # list of URLs that end in '.py'
    n = url_download_many(nfiles, course_url, pyurls)
    print '%s files downloaded' % n


def webclient2(nfiles):
    """
    Solution for week 5 assignment in webclient.txt, part 2:

    2.  File downloader using web API: same as 1, but find the Python source
    files using the GitHub API.  Hints: you need to look in the repo at
    https://github.com/jon-jacky/uw_python/tree/gh-pages, not the web
    pages.  Git calls the files in a repository "blobs", see the "get all blobs"
    example about halfway down this page: http://develop.github.com/p/object.html

    This version takes one argument, nfiles, the maximum number of files to download.
    For testing set nfiles to a very small number
    """
    pyblobs = github_find_blobs(course_blobs_url, 'winter_2012', '.py')
    n = github_download_many(nfiles, retrieve_blob_url, pyblobs)
    print '%s files downloaded' % n


if __name__ == '__main__':
    #
    # uncomment just one line below, each is a separate program or test
    # 
    # scrape(course_url) # lab assignment
    # test_download()
    # webclient1(3) # use soup, just download the first three .py files
    webclient2(3) # use github api
    # pass # uncomment this to work interactively after python -i download.py
