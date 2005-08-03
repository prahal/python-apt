#!/usr/bin/python
# example how to deal with the depcache

import apt_pkg
import sys, os
import copy

from apt.progress import OpProgress, FetchProgress, InstallProgress


# init
apt_pkg.init()

progress = OpProgress()
cache = apt_pkg.GetCache(progress)
print "Available packages: %s " % cache.PackageCount

# get depcache
depcache = apt_pkg.GetDepCache(cache)
depcache.ReadPinFile()
depcache.Init(progress)

# do something
fprogress = FetchProgress()
iprogress = InstallProgress()

# can be used to set a custom fork method (like vte.Terminal.forkpty)
#iprogress.fork = os.fork

iter = cache["base-config"]
print "\n%s"%iter

# install or remove, the importend thing is to keep us busy :)
if iter.CurrentVer == None:
	depcache.MarkInstall(iter)
else:
	depcache.MarkDelete(iter)
res = depcache.Commit(fprogress, iprogress)
print res

print "Exiting"
sys.exit(0)



