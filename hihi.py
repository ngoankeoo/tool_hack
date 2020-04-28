import optparse
import parser
import zipfile
from threading import Thread


def extract_zip(zfile, password):
    try:
        zfile.extractall(pwd=password)
        print("[+] Password found: " + password + '\n')
    except:
        pass


if __name__ == '__main__':
    parser = optparse.OptionParser("usage %prog " + \
                                   "-f <zipfile> -d <dicctionary>")
    parser.add_option('-f', dest='zname', type='string', \
                      help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', \
                      help='specify dictionary file')
    (options, arg) = parser.parse_args()
    print('ell')
    if (options.zname is None) or (options.dname is None):
	    print (parser.usage)
	    exit(0)
    else:
	    zname = options.zname
	    dname = options.dname
