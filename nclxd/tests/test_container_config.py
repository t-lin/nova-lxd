# Copyright 2015 Canonical Ltd
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_config import cfg

from nova import test

from nclxd.nova.virt.lxd import container_config

CONF = cfg.CONF


class LXDTestContainerConfig(test.NoDBTestCase):

    def setUp(self):
        super(LXDTestContainerConfig, self).setUp()
        self.container_config = container_config.LXDContainerConfig()
