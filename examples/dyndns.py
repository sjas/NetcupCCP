#!/usr/bin/env python3
# coding: utf8

# Copyright (C) 2018 MrKrabat
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import netcup


# start api connection
ccp = netcup.dns.CCPConnection(cachepath="mysession", debug=False)
ccp.start(username="<CCP NAME>", password="<CCP PASSWORD>")

# get domain infos
mydomain = ccp.getDomain("<CCP DOMAIN ID>")

# check if exists
dyndns = mydomain.searchRecord("dyndns", "A")

if not dyndns:
    # add record
    mydomain.addRecord("dyndns", "A", "<NEW IPv4>")
else:
    # update record
    # assuming we only have one record
    mydomain.setRecord(list(dyndns.keys())[0], "dyndns", "A", "<NEW IPv4>")

# save changes
ccp.saveDomain("<CCP DOMAIN ID>", mydomain)

# cleanup
ccp.close()
