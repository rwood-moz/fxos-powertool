# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time

from powertool.device import Flame

# Test box has single Firefox OS device with battery harness/ammeter
fxos_device = Flame()

print "Powering off Firefox OS device..."
fxos_device.power_off()
print "Sleeping 30 seconds..."
time.sleep(30)
print "Powering on device..."
fxos_device.power_on()
