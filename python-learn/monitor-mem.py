#!/usr/bin/python
#one example, a simple function to print memory usage

import os
_proc_status = '/proc/%d/status' % os.getpid()
_scale = {'kB': 1024.0, 'mB': 1024.0*1024.0,
          'KB': 1024.0, 'MB': 1024.0*1024.0}

def _VmNum(VmKey):
    try:
          t = open(_proc_status)
          v = t.read()
          t.close()
    except IOError:
          print "Failed to open " + _proc_status
          return 0.0 #might not be Linux

    i = v.index(VmKey)
    items = v[i:].split(None, 3)
    return float(items[1]) * float(_scale[items[2]])

def memory(since = 0.0):
    return _VmNum('VmSize') - since

if __name__ == '__main__' :
    m0 = memory()
    print '#1 %6d' % m0

    t = 'hello '*1024*1024
    a = t.index('hello')

    m1 = memory(m0)
    print '#2 %6d' % m1

    
    
               


          
