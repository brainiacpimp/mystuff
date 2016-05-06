import sys
import os
import os.path
import hashlib


def walk_dir(dir_path):
    """ Walks given directory and calculates checksums for all files in it"""
    checksums = {}

    for root, subdir, files in os.walk(dir_path):
        for f in files:
            if not os.path.islink(os.path.join(root, f)):
                csum = hashfile(os.path.join(root, f))
                if csum in checksums:
                    checksums[csum].append(os.path.join(root, f))
                else:
                    checksums[csum] = [os.path.join(root, f)]

            else:
                pass
        #print((checksums))


    return checksums


def hashfile(path, hashtype='md5', blocksize=65536):
    """ Creates file checksum """
    with open(path, 'rb') as afile:

        if hashtype == 'md5':
            hasher = hashlib.md5()
        elif hashtype == 'sha256':
            hasher = hashlib.sha256()
        elif hashtype == 'sha512':
            hasher = hashlib.sha512()

        buf = afile.read(blocksize)

        while len(buf) > 0:

            hasher.update(buf)
            buf = afile.read(blocksize)

    return hasher.hexdigest()

if __name__ == '__main__':
    path_to = '/home/john/projects/filededup'
    file1 = 'test1.txt'
    file2 = 'test2.txt'
    file3 = 'test3.txt'

    w1 = walk_dir('/home/john')
    w2 = walk_dir('/home/john/projects/filededup')

    for v in w2.values():
        if len(v) > 1:
            print((v))