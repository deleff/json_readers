#!/usr/bin/env python

import urllib, json

url = "http://maps.googleapis.com/maps/api/geocode/json?address=google"
response = urllib.urlopen(url)
data = json.loads(response.read())
response.close()

#print data['results'][0]['address_components'][0]

f = open('auditd_profile.pp', 'w')
#f.write('# This file contains the auditctl rules that are loaded\n')
#f.write('# whenever the audit daemon is started via the initscripts.\n')
#f.write('# The rules are simply the parameters that would be passed to auditctl.\n')
#f.write('\n# First rule - delete all\n')
#f.write('-D\n')
#f.write('\n# Increase the buffers to survive stress events.\n')
#f.write('# Make this bigger for busy systems\n')
#f.write('-b 320\n')
#f.write('\n# Feel free to add below this line. See auditctl man page\n')

f.write('class profile::auditd_profile () {\n')
f.write('  class { \'auditd\':\n')
f.write('    rules => {')
i = 1
for criteria in data['results'][0]['address_components']:
#    print 'Address ', i
    for key, value in criteria.iteritems():
        keynum = 'key_number_'+ str(i)
        f.write('\n')
	f.write('      \'watch for changes to file ')
	f.write(str(value))
	f.write('\' => {\n')
	f.write('        content => \'-w ')
        f.write(str(value))
	f.write(' -p rxwa -k ')
	f.write(keynum)
	f.write('\',')
	f.write('\n        order   => ')
	f.write(str(i))
	f.write(',')
	f.write('\n      },')
        i = i + 1
#        f.write('\n')
f.write('\n\n    }, #end rules')
f.write('\n\n  } #end class auditd')
f.write('\n} #end class auditd_profile')
f.close()   
        
