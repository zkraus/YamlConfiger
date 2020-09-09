# yacfg --- YAML Assisted Content Focused Generator

This tool can generate a set of configuration files or any documents in fact
from a template and a set of data called profile. Originally it was created
to help with configuring Apache ActiveMQ Artemis Broker, but it was modified
then to be used as general templating tool. Internally it uses jinja2, and
it can server as easy to use Command line interface to jinja2 if you want.

yacfg has a user facing Command Line Tool for quick and easy command line usage.
Furthermore, it is possible to use its API in your python code.

## Documentation

Formatted documentation can be viewed at [rh-messaging-qe.github.io/yacfg/index.html](https://rh-messaging-qe.github.io/yacfg/index.html).

## Contributing

If you find a bug or room for improvement, submit either a ticket or PR.

## Maintainers

_Alphabetically ordered_

* Dominik Lenoch <dlenoch@redhat.com>
* Zdenek Kraus <zkraus@redhat.com>

See GitHub statistics for an [up-to-date list of contributors](https://github.com/rh-messaging-qe/yacfg/graphs/contributors).

## License

Copyright 2018 Red Hat Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Acknowledgments

* [jinja2](http://jinja.pocoo.org/docs/2.10/) -- awesome templating engine
* [yaml](http://yaml.org/) -- very convenient user readable format
* [learn_yaml](https://learnxinyminutes.com/docs/yaml/) -- great YAML cheat sheet
* [pyyaml](https://github.com/yaml/pyyaml) -- python YAML parser
* [jq](https://stedolan.github.io/jq/) -- great tool for working with structured data (JSON)
* [yq](https://yq.readthedocs.io/en/latest/) -- YAML variant of jq
