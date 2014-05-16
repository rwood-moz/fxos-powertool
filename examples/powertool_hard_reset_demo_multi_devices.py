# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time
import sys

from powertool.device import Flame, Pool

# Test box has multiple Firefox OS devices with battery harness/ammeter on each
# Serial number of which device to reset received as command line argument

if len(sys.argv) < 2:
    print "Please provide serial number on command line"
    exit(1)

print "Mapping Firefox OS devices and ammeters"
fxos_device_pool = Pool(device_class=Flame)
print "Sleeping 30 seconds..."
time.sleep(30)

# Hard reset the device as indicated by the provided s/n
fxos_device_to_reset = str(sys.argv[1])
print "Powering off Firefox OS device with s/n '%s'..." %fxos_device_to_reset
fxos_device_pool[fxos_device_to_reset].power_off()
print "Sleeping 30 seconds..."
time.sleep(30)
print "Powering on Firefox OS device with s/n '%s'..." %fxos_device_to_reset
fxos_device_pool[fxos_device_to_reset].power_on()
