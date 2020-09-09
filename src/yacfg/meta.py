# Copyright 2018 Red Hat Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

NAME = 'yacfg'
VERSION = '0.8.0'
SHORT_DESCRIPTION = 'Template based configuration generator'
DESCRIPTION = (
    'Template based configuration files generator based on jinja2 and yaml'
    ' or it may be used as user direct command line interface to jinja2 for'
    ' documents. this is just a core command line tool and pre-made templates'
    ' and profiles should be available via additional packages, alternatively,'
    ' you always can create custom.'
)
TEMPLATES = 'templates'
PROFILES = 'profiles'
