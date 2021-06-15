import os
import urllib.request
import zipfile

def download(url, output_fname):
    with urllib.request.urlopen(url) as u:
        with open(output_fname, 'bw') as o:
            o.write(u.read())

def unzip(zfname, output_dir):
    with zipfile.ZipFile(zfname, "r") as zf:
        zf.extractall(output_dir)
    os.remove(zfname)