from __future__ import division
from ftplib import FTP
from urlparse import urlparse
import os, sys
import time
import getopt

#simple progress bar based on percentage
def draw_progress(current_size, total_size, desc):
    bars = current_size/total_size*20
    
    sys.stdout.write('\r|')
    
    for i in range(int(bars)):
        sys.stdout.write("=")
    
    for i in range(20-int(bars)):
        sys.stdout.write(" ")
        
    sys.stdout.write("| {0:.2%} {1}/{2} {3}".format(current_size/total_size, current_size, total_size, desc))
    

#print len(sys.argv), sys.argv

host = sys.argv[0]

valid_args = 'vup'

verbose= False


optlist, args = getopt.getopt(sys.argv[1:], valid_args)

for opt in optlist:
    if '-v' in opt:
        print 'verbose'
        verbose = True

if verbose:
    print optlist
    print args

#if __file__ in args:
if verbose:
    print 'script', __file__



upo = urlparse(args[0])
    
if upo.netloc is None or upo.netloc is '':
    if verbose:
        print 'trying with ftp proto prefix'
    tryprefix = 'ftp://'+args[0]
    upo = urlparse(tryprefix)

if verbose:
    print upo

host = upo.netloc
path = upo.path
print 'download from', host
print 'download dir path', path

remote_dir = os.path.dirname(path)
remote_filename = os.path.basename(path)
local_filename = os.path.basename(path)
if verbose:
    print 'remote file', remote_dir, remote_filename
    print 'local file', local_filename

ftp = FTP(host)     # connect to host, default port
ftp.login()                     # user anonymous, passwd anonymous@
ftp.cwd(remote_dir)               # change into "debian" directory
#ftp.retrlines('LIST')           # list directory contents
remote_size= ftp.size(remote_filename)

local_size = 0

if os.path.exists(local_filename):
    local_size = os.stat(local_filename).st_size
else:
    resume_accepted = True
    
if verbose:
    print 'remote size', remote_size
    print 'local size', local_size

resume_cmd ='REST ' + str(local_size)

if local_size == remote_size:
    print 'file sizes match, skipping download'
    resume_accepted = False

if local_size > 0 and local_size < remote_size:
    
    print resume_cmd
    print 'resuming '

    resume_accepted = True
    try:
        ftp.retrlines(resume_cmd)
    except Exception as e:
        if '350' in e.message and str(local_size) in e.message:
            #print 'accepted'
            resume_accepted = True
        else:
            resume_accepted = False
        print e.message


    
    
if resume_accepted:
    #print 'transferring'
    o = open(local_filename, 'wb')
    o.seek(local_size)

    def download_with_progress(total_size, o, block):
        o.write(block)
        current_time = time.time()
        elapsed_time = current_time - download_with_progress.first_time
        current_size = o.tell()
        total_download = current_size - download_with_progress.first_size
        time_str = "{0:.2f}b/s {1}".format(total_download/elapsed_time, current_time)
        
        draw_progress(current_size, total_size, time_str)
    #static local variables, really just for values of first call of function to calculate elapsed and total actually downloaded vs. total file size   
    download_with_progress.first_time = time.time()
    download_with_progress.first_size = o.tell()


    #pbar = tqdm(range(remote_size), ncols=50, total=remote_size, leave=True)
    #for i in range(local_size):
    #    pbar.next()
    ftp.retrbinary('RETR '+remote_filename, lambda block: download_with_progress(remote_size, o, block))
    
    o.close()

ftp.quit()
