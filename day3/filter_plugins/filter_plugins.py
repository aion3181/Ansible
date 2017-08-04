from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible import errors

def get_mongo_src(arg, os_family, os_release, mongodb_version):
    osv = os_family + os_release
    for lin in arg:
    	if (osv in lin) and (mongodb_version in lin):
    		result = lin
    		return result   		
 

class FilterModule(object):
    def filters(self):
        return {
            'get_mongo_src': get_mongo_src
        }

