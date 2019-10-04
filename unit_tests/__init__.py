# Copyright 2019 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys

# Mock out charmhelpers so that we can test without it.
import charms_openstack.test_mocks  # noqa
charms_openstack.test_mocks.mock_charmhelpers()

_path = os.path.dirname(os.path.realpath(__file__))
_src = os.path.abspath(os.path.join(_path, 'src'))
_lib = os.path.abspath(os.path.join(_path, 'src/lib'))


def _add_path(path):
    if path not in sys.path:
        sys.path.insert(1, path)

_add_path(_src)
_add_path(_lib)