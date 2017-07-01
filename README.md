# Obstructing Trio (GitHub Contributors)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![GitHub release](https://img.shields.io/github/release/funilrys/Obstructing-Trio.svg)](https://github.com/funilrys/Obstructing-Trio/releases/tag/1.0.1) [![GitHub commits](https://img.shields.io/github/commits-since/funilrys/Obstructing-Trio/1.0.1.svg)](https://github.com/funilrys/Obstructing-Trio/commits/master) [![Github API](https://img.shields.io/badge/GitHub%20REST%20API-v3-yellow.svg)](https://docs.transifex.com/api/introduction)

> Python module/library for saving the list of contributors of a given public Github repository into a JSON file.

## Features

- Works with Python 3.x and Python 2.x
- Access GitHub repository contributors list
- Get list of contributors username in JSON format
- Get list of contributors username in Python `dict` format
- Get list of contributors username in Python `list` format
- Exclude username from generated list

## Installation

### From Github

```shell
git clone https://github.com/funilrys/Obstructing-Trio.git
cd Obstructing-Trio && python setup.py install
```

## Examples of usage

### Common usage

The following will save the **list of contributors** into `contributors.json` in you **current location**.

```python
#!/bin/env python
from obstructing_trio import get

get('funilrys/funceble')
```

### Python `list` format

The following will not save the **list of contributors** into `contributors.json` but it'll return a _python_ `list` of contributors usernames.

```python
#!/bin/env python
from obstructing_trio import get

usernames = get('funilrys/funceble', save_in_file=False, return_list=True)
print(usernames)
```

### Python `dict` format

The following will save the **list of contributors** into `contributors.json` and it'll return a _python_ `dict` of the contributor's usernames.

**Output format:** `{'contributors':['user1','user2']}`

```python
#!/bin/env python
from obstructing_trio import get

usernames = get('funilrys/funceble', save_in_file=True, return_dict=True)
print(usernames)
```

### Exclusion

The following will exclude the usernames _**funilrys**_ and _**gitter-badger**_ from the **list of contributor's** usernames.

```python
#!/bin/env python
from obstructing_trio import get

usernames = get('EragonJ/Kaku', save_in_file=True, exluded=['gitter-badger','funilrys'])
print(usernames)
```

--------------------------------------------------------------------------------

# How to contribute?

To contribute, you have to **send a new [Pull Request](https://github.com/funilrys/Obstructing-Trio/compare)** after you **[forked](https://github.com/funilrys/Obstructing-Trio/pulls#fork-destination-box)** and edited the script(s).

## :warning: WARNING :warning:

### DO NOT FORGET

- To sign your commit(s) with **"Signed-off by: FirstName LastName < email at service dot com >"** _and/or_ simply **sign your commit(s)** with **PGP** _(Please read more [here](https://github.com/blog/2144-gpg-signature-verification))_.
- All **contributions/modifications** must be done under **the `dev` or a new branch** if you plan to **send a new [Pull Request](https://github.com/funilrys/Obstructing-Trio/compare)**.
- :warning: Every **contributions/modifications** which are under **master** _(exception for minor changes)_ **will not be merged**. :warning:

--------------------------------------------------------------------------------

# License

```
MIT License

Copyright (c) 2017 Nissar Chababy <contact at funilrys dot com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
