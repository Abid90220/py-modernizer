# Python Project Audit Report

- **Generated:** 2025-09-24T16:19:16+00:00
- **Repo Path:** `/var/folders/xs/z59w57g118v32dht04blnmbc0000gn/T/repo_6uijuw4u`

## Packaging
- `pyproject.toml`: Yes ✅
- `setup.py`: Yes ✅
- `setup.cfg`: Yes ✅

## Dependencies
- Found dependency files:
  - `requirements-dev.txt`
  - `pyproject.toml`

## Tests
- Test directories:
  - `tests`
- Pytest config present: Yes ✅

## Test Run Results
- Test run skipped.

## Ruff Linting
```
E402 Module level import not at top of file
   --> src/requests/__init__.py:143:1
    |
142 | # urllib3's DependencyWarnings should be silenced.
143 | from urllib3.exceptions import DependencyWarning
    | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
144 |
145 | warnings.simplefilter("ignore", DependencyWarning)
    |

E402 Module level import not at top of file
   --> src/requests/__init__.py:148:1
    |
147 | # Set default logging handler to avoid "No handler found" warnings.
148 | import logging
    | ^^^^^^^^^^^^^^
149 | from logging import NullHandler
    |

E402 Module level import not at top of file
   --> src/requests/__init__.py:149:1
    |
147 | # Set default logging handler to avoid "No handler found" warnings.
148 | import logging
149 | from logging import NullHandler
    | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
150 |
151 | from . import packages, utils
    |

E402 Module level import not at top of file
   --> src/requests/__init__.py:151:1
    |
149 | from logging import NullHandler
150 |
151 | from . import packages, utils
    | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
152 | from .__version__ import (
153 |     __author__,
    |

F401 `.packages` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:151:15
    |
149 | from logging import NullHandler
150 |
151 | from . import packages, utils
    |               ^^^^^^^^
152 | from .__version__ import (
153 |     __author__,
    |
help: Use an explicit re-export: `packages as packages`

F401 `.utils` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:151:25
    |
149 | from logging import NullHandler
150 |
151 | from . import packages, utils
    |                         ^^^^^
152 | from .__version__ import (
153 |     __author__,
    |
help: Use an explicit re-export: `utils as utils`

E402 Module level import not at top of file
   --> src/requests/__init__.py:152:1
    |
151 |   from . import packages, utils
152 | / from .__version__ import (
153 | |     __author__,
154 | |     __author_email__,
155 | |     __build__,
156 | |     __cake__,
157 | |     __copyright__,
158 | |     __description__,
159 | |     __license__,
160 | |     __title__,
161 | |     __url__,
162 | |     __version__,
163 | | )
    | |_^
164 |   from .api import delete, get, head, options, patch, post, put, request
165 |   from .exceptions import (
    |

F401 `.__version__.__author__` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:153:5
    |
151 | from . import packages, utils
152 | from .__version__ import (
153 |     __author__,
    |     ^^^^^^^^^^
154 |     __author_email__,
155 |     __build__,
    |
help: Use an explicit re-export: `__author__ as __author__`

F401 `.__version__.__author_email__` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:154:5
    |
152 | from .__version__ import (
153 |     __author__,
154 |     __author_email__,
    |     ^^^^^^^^^^^^^^^^
155 |     __build__,
156 |     __cake__,
    |
help: Use an explicit re-export: `__author_email__ as __author_email__`

F401 `.__version__.__build__` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:155:5
    |
153 |     __author__,
154 |     __author_email__,
155 |     __build__,
    |     ^^^^^^^^^
156 |     __cake__,
157 |     __copyright__,
    |
help: Use an explicit re-export: `__build__ as __build__`

F401 `.__version__.__cake__` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:156:5
    |
154 |     __author_email__,
155 |     __build__,
156 |     __cake__,
    |     ^^^^^^^^
157 |     __copyright__,
158 |     __description__,
    |
help: Use an explicit re-export: `__cake__ as __cake__`

F401 `.__version__.__copyright__` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:157:5
    |
155 |     __build__,
156 |     __cake__,
157 |     __copyright__,
    |     ^^^^^^^^^^^^^
158 |     __description__,
159 |     __license__,
    |
help: Use an explicit re-export: `__copyright__ as __copyright__`

F401 `.__version__.__description__` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:158:5
    |
156 |     __cake__,
157 |     __copyright__,
158 |     __description__,
    |     ^^^^^^^^^^^^^^^
159 |     __license__,
160 |     __title__,
    |
help: Use an explicit re-export: `__description__ as __description__`

F401 `.__version__.__license__` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:159:5
    |
157 |     __copyright__,
158 |     __description__,
159 |     __license__,
    |     ^^^^^^^^^^^
160 |     __title__,
161 |     __url__,
    |
help: Use an explicit re-export: `__license__ as __license__`

F401 `.__version__.__title__` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:160:5
    |
158 |     __description__,
159 |     __license__,
160 |     __title__,
    |     ^^^^^^^^^
161 |     __url__,
162 |     __version__,
    |
help: Use an explicit re-export: `__title__ as __title__`

F401 `.__version__.__url__` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:161:5
    |
159 |     __license__,
160 |     __title__,
161 |     __url__,
    |     ^^^^^^^
162 |     __version__,
163 | )
    |
help: Use an explicit re-export: `__url__ as __url__`

F401 `.__version__.__version__` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:162:5
    |
160 |     __title__,
161 |     __url__,
162 |     __version__,
    |     ^^^^^^^^^^^
163 | )
164 | from .api import delete, get, head, options, patch, post, put, request
    |
help: Use an explicit re-export: `__version__ as __version__`

E402 Module level import not at top of file
   --> src/requests/__init__.py:164:1
    |
162 |     __version__,
163 | )
164 | from .api import delete, get, head, options, patch, post, put, request
    | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
165 | from .exceptions import (
166 |     ConnectionError,
    |

F401 `.api.delete` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:164:18
    |
162 |     __version__,
163 | )
164 | from .api import delete, get, head, options, patch, post, put, request
    |                  ^^^^^^
165 | from .exceptions import (
166 |     ConnectionError,
    |
help: Use an explicit re-export: `delete as delete`

F401 `.api.get` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:164:26
    |
162 |     __version__,
163 | )
164 | from .api import delete, get, head, options, patch, post, put, request
    |                          ^^^
165 | from .exceptions import (
166 |     ConnectionError,
    |
help: Use an explicit re-export: `get as get`

F401 `.api.head` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:164:31
    |
162 |     __version__,
163 | )
164 | from .api import delete, get, head, options, patch, post, put, request
    |                               ^^^^
165 | from .exceptions import (
166 |     ConnectionError,
    |
help: Use an explicit re-export: `head as head`

F401 `.api.options` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:164:37
    |
162 |     __version__,
163 | )
164 | from .api import delete, get, head, options, patch, post, put, request
    |                                     ^^^^^^^
165 | from .exceptions import (
166 |     ConnectionError,
    |
help: Use an explicit re-export: `options as options`

F401 `.api.patch` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:164:46
    |
162 |     __version__,
163 | )
164 | from .api import delete, get, head, options, patch, post, put, request
    |                                              ^^^^^
165 | from .exceptions import (
166 |     ConnectionError,
    |
help: Use an explicit re-export: `patch as patch`

F401 `.api.post` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:164:53
    |
162 |     __version__,
163 | )
164 | from .api import delete, get, head, options, patch, post, put, request
    |                                                     ^^^^
165 | from .exceptions import (
166 |     ConnectionError,
    |
help: Use an explicit re-export: `post as post`

F401 `.api.put` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:164:59
    |
162 |     __version__,
163 | )
164 | from .api import delete, get, head, options, patch, post, put, request
    |                                                           ^^^
165 | from .exceptions import (
166 |     ConnectionError,
    |
help: Use an explicit re-export: `put as put`

F401 `.api.request` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:164:64
    |
162 |     __version__,
163 | )
164 | from .api import delete, get, head, options, patch, post, put, request
    |                                                                ^^^^^^^
165 | from .exceptions import (
166 |     ConnectionError,
    |
help: Use an explicit re-export: `request as request`

E402 Module level import not at top of file
   --> src/requests/__init__.py:165:1
    |
163 |   )
164 |   from .api import delete, get, head, options, patch, post, put, request
165 | / from .exceptions import (
166 | |     ConnectionError,
167 | |     ConnectTimeout,
168 | |     FileModeWarning,
169 | |     HTTPError,
170 | |     JSONDecodeError,
171 | |     ReadTimeout,
172 | |     RequestException,
173 | |     Timeout,
174 | |     TooManyRedirects,
175 | |     URLRequired,
176 | | )
    | |_^
177 |   from .models import PreparedRequest, Request, Response
178 |   from .sessions import Session, session
    |

F401 `.exceptions.ConnectionError` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:166:5
    |
164 | from .api import delete, get, head, options, patch, post, put, request
165 | from .exceptions import (
166 |     ConnectionError,
    |     ^^^^^^^^^^^^^^^
167 |     ConnectTimeout,
168 |     FileModeWarning,
    |
help: Use an explicit re-export: `ConnectionError as ConnectionError`

F401 `.exceptions.ConnectTimeout` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:167:5
    |
165 | from .exceptions import (
166 |     ConnectionError,
167 |     ConnectTimeout,
    |     ^^^^^^^^^^^^^^
168 |     FileModeWarning,
169 |     HTTPError,
    |
help: Use an explicit re-export: `ConnectTimeout as ConnectTimeout`

F401 `.exceptions.HTTPError` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:169:5
    |
167 |     ConnectTimeout,
168 |     FileModeWarning,
169 |     HTTPError,
    |     ^^^^^^^^^
170 |     JSONDecodeError,
171 |     ReadTimeout,
    |
help: Use an explicit re-export: `HTTPError as HTTPError`

F401 `.exceptions.JSONDecodeError` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:170:5
    |
168 |     FileModeWarning,
169 |     HTTPError,
170 |     JSONDecodeError,
    |     ^^^^^^^^^^^^^^^
171 |     ReadTimeout,
172 |     RequestException,
    |
help: Use an explicit re-export: `JSONDecodeError as JSONDecodeError`

F401 `.exceptions.ReadTimeout` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:171:5
    |
169 |     HTTPError,
170 |     JSONDecodeError,
171 |     ReadTimeout,
    |     ^^^^^^^^^^^
172 |     RequestException,
173 |     Timeout,
    |
help: Use an explicit re-export: `ReadTimeout as ReadTimeout`

F401 `.exceptions.RequestException` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:172:5
    |
170 |     JSONDecodeError,
171 |     ReadTimeout,
172 |     RequestException,
    |     ^^^^^^^^^^^^^^^^
173 |     Timeout,
174 |     TooManyRedirects,
    |
help: Use an explicit re-export: `RequestException as RequestException`

F401 `.exceptions.Timeout` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:173:5
    |
171 |     ReadTimeout,
172 |     RequestException,
173 |     Timeout,
    |     ^^^^^^^
174 |     TooManyRedirects,
175 |     URLRequired,
    |
help: Use an explicit re-export: `Timeout as Timeout`

F401 `.exceptions.TooManyRedirects` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:174:5
    |
172 |     RequestException,
173 |     Timeout,
174 |     TooManyRedirects,
    |     ^^^^^^^^^^^^^^^^
175 |     URLRequired,
176 | )
    |
help: Use an explicit re-export: `TooManyRedirects as TooManyRedirects`

F401 `.exceptions.URLRequired` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:175:5
    |
173 |     Timeout,
174 |     TooManyRedirects,
175 |     URLRequired,
    |     ^^^^^^^^^^^
176 | )
177 | from .models import PreparedRequest, Request, Response
    |
help: Use an explicit re-export: `URLRequired as URLRequired`

E402 Module level import not at top of file
   --> src/requests/__init__.py:177:1
    |
175 |     URLRequired,
176 | )
177 | from .models import PreparedRequest, Request, Response
    | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
178 | from .sessions import Session, session
179 | from .status_codes import codes
    |

F401 `.models.PreparedRequest` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:177:21
    |
175 |     URLRequired,
176 | )
177 | from .models import PreparedRequest, Request, Response
    |                     ^^^^^^^^^^^^^^^
178 | from .sessions import Session, session
179 | from .status_codes import codes
    |
help: Use an explicit re-export: `PreparedRequest as PreparedRequest`

F401 `.models.Request` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:177:38
    |
175 |     URLRequired,
176 | )
177 | from .models import PreparedRequest, Request, Response
    |                                      ^^^^^^^
178 | from .sessions import Session, session
179 | from .status_codes import codes
    |
help: Use an explicit re-export: `Request as Request`

F401 `.models.Response` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:177:47
    |
175 |     URLRequired,
176 | )
177 | from .models import PreparedRequest, Request, Response
    |                                               ^^^^^^^^
178 | from .sessions import Session, session
179 | from .status_codes import codes
    |
help: Use an explicit re-export: `Response as Response`

E402 Module level import not at top of file
   --> src/requests/__init__.py:178:1
    |
176 | )
177 | from .models import PreparedRequest, Request, Response
178 | from .sessions import Session, session
    | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
179 | from .status_codes import codes
    |

F401 `.sessions.Session` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:178:23
    |
176 | )
177 | from .models import PreparedRequest, Request, Response
178 | from .sessions import Session, session
    |                       ^^^^^^^
179 | from .status_codes import codes
    |
help: Use an explicit re-export: `Session as Session`

F401 `.sessions.session` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:178:32
    |
176 | )
177 | from .models import PreparedRequest, Request, Response
178 | from .sessions import Session, session
    |                                ^^^^^^^
179 | from .status_codes import codes
    |
help: Use an explicit re-export: `session as session`

E402 Module level import not at top of file
   --> src/requests/__init__.py:179:1
    |
177 | from .models import PreparedRequest, Request, Response
178 | from .sessions import Session, session
179 | from .status_codes import codes
    | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
180 |
181 | logging.getLogger(__name__).addHandler(NullHandler())
    |

F401 `.status_codes.codes` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
   --> src/requests/__init__.py:179:27
    |
177 | from .models import PreparedRequest, Request, Response
178 | from .sessions import Session, session
179 | from .status_codes import codes
    |                           ^^^^^
180 |
181 | logging.getLogger(__name__).addHandler(NullHandler())
    |
help: Use an explicit re-export: `codes as codes`

F401 [*] `json` imported but unused
  --> src/requests/compat.py:64:12
   |
62 |     has_simplejson = True
63 | except ImportError:
64 |     import json
   |            ^^^^
65 |
66 | if has_simplejson:
   |
help: Remove unused import: `json`

F401 [*] `json.JSONDecodeError` imported but unused
  --> src/requests/compat.py:69:22
   |
67 |     from simplejson import JSONDecodeError
68 | else:
69 |     from json import JSONDecodeError
   |                      ^^^^^^^^^^^^^^^
70 |
71 | # Keep OrderedDict for backwards compatibility.
   |
help: Remove unused import: `json.JSONDecodeError`

E402 Module level import not at top of file
  --> src/requests/compat.py:72:1
   |
71 | # Keep OrderedDict for backwards compatibility.
72 | from collections import OrderedDict
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
73 | from collections.abc import Callable, Mapping, MutableMapping
74 | from http import cookiejar as cookielib
   |

F401 [*] `collections.OrderedDict` imported but unused
  --> src/requests/compat.py:72:25
   |
71 | # Keep OrderedDict for backwards compatibility.
72 | from collections import OrderedDict
   |                         ^^^^^^^^^^^
73 | from collections.abc import Callable, Mapping, MutableMapping
74 | from http import cookiejar as cookielib
   |
help: Remove unused import: `collections.OrderedDict`

E402 Module level import not at top of file
  --> src/requests/compat.py:73:1
   |
71 | # Keep OrderedDict for backwards compatibility.
72 | from collections import OrderedDict
73 | from collections.abc import Callable, Mapping, MutableMapping
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
74 | from http import cookiejar as cookielib
75 | from http.cookies import Morsel
   |

F401 [*] `collections.abc.Callable` imported but unused
  --> src/requests/compat.py:73:29
   |
71 | # Keep OrderedDict for backwards compatibility.
72 | from collections import OrderedDict
73 | from collections.abc import Callable, Mapping, MutableMapping
   |                             ^^^^^^^^
74 | from http import cookiejar as cookielib
75 | from http.cookies import Morsel
   |
help: Remove unused import

F401 [*] `collections.abc.Mapping` imported but unused
  --> src/requests/compat.py:73:39
   |
71 | # Keep OrderedDict for backwards compatibility.
72 | from collections import OrderedDict
73 | from collections.abc import Callable, Mapping, MutableMapping
   |                                       ^^^^^^^
74 | from http import cookiejar as cookielib
75 | from http.cookies import Morsel
   |
help: Remove unused import

F401 [*] `collections.abc.MutableMapping` imported but unused
  --> src/requests/compat.py:73:48
   |
71 | # Keep OrderedDict for backwards compatibility.
72 | from collections import OrderedDict
73 | from collections.abc import Callable, Mapping, MutableMapping
   |                                                ^^^^^^^^^^^^^^
74 | from http import cookiejar as cookielib
75 | from http.cookies import Morsel
   |
help: Remove unused import

E402 Module level import not at top of file
  --> src/requests/compat.py:74:1
   |
72 | from collections import OrderedDict
73 | from collections.abc import Callable, Mapping, MutableMapping
74 | from http import cookiejar as cookielib
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
75 | from http.cookies import Morsel
76 | from io import StringIO
   |

F401 [*] `http.cookiejar` imported but unused
  --> src/requests/compat.py:74:31
   |
72 | from collections import OrderedDict
73 | from collections.abc import Callable, Mapping, MutableMapping
74 | from http import cookiejar as cookielib
   |                               ^^^^^^^^^
75 | from http.cookies import Morsel
76 | from io import StringIO
   |
help: Remove unused import: `http.cookiejar`

E402 Module level import not at top of file
  --> src/requests/compat.py:75:1
   |
73 | from collections.abc import Callable, Mapping, MutableMapping
74 | from http import cookiejar as cookielib
75 | from http.cookies import Morsel
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
76 | from io import StringIO
   |

F401 [*] `http.cookies.Morsel` imported but unused
  --> src/requests/compat.py:75:26
   |
73 | from collections.abc import Callable, Mapping, MutableMapping
74 | from http import cookiejar as cookielib
75 | from http.cookies import Morsel
   |                          ^^^^^^
76 | from io import StringIO
   |
help: Remove unused import: `http.cookies.Morsel`

E402 Module level import not at top of file
  --> src/requests/compat.py:76:1
   |
74 | from http import cookiejar as cookielib
75 | from http.cookies import Morsel
76 | from io import StringIO
   | ^^^^^^^^^^^^^^^^^^^^^^^
77 |
78 | # --------------
   |

F401 [*] `io.StringIO` imported but unused
  --> src/requests/compat.py:76:16
   |
74 | from http import cookiejar as cookielib
75 | from http.cookies import Morsel
76 | from io import StringIO
   |                ^^^^^^^^
77 |
78 | # --------------
   |
help: Remove unused import: `io.StringIO`

E402 Module level import not at top of file
  --> src/requests/compat.py:81:1
   |
79 |   # Legacy Imports
80 |   # --------------
81 | / from urllib.parse import (
82 | |     quote,
83 | |     quote_plus,
84 | |     unquote,
85 | |     unquote_plus,
86 | |     urldefrag,
87 | |     urlencode,
88 | |     urljoin,
89 | |     urlparse,
90 | |     urlsplit,
91 | |     urlunparse,
92 | | )
   | |_^
93 |   from urllib.request import (
94 |       getproxies,
   |

F401 [*] `urllib.parse.quote` imported but unused
  --> src/requests/compat.py:82:5
   |
80 | # --------------
81 | from urllib.parse import (
82 |     quote,
   |     ^^^^^
83 |     quote_plus,
84 |     unquote,
   |
help: Remove unused import

F401 [*] `urllib.parse.quote_plus` imported but unused
  --> src/requests/compat.py:83:5
   |
81 | from urllib.parse import (
82 |     quote,
83 |     quote_plus,
   |     ^^^^^^^^^^
84 |     unquote,
85 |     unquote_plus,
   |
help: Remove unused import

F401 [*] `urllib.parse.unquote` imported but unused
  --> src/requests/compat.py:84:5
   |
82 |     quote,
83 |     quote_plus,
84 |     unquote,
   |     ^^^^^^^
85 |     unquote_plus,
86 |     urldefrag,
   |
help: Remove unused import

F401 [*] `urllib.parse.unquote_plus` imported but unused
  --> src/requests/compat.py:85:5
   |
83 |     quote_plus,
84 |     unquote,
85 |     unquote_plus,
   |     ^^^^^^^^^^^^
86 |     urldefrag,
87 |     urlencode,
   |
help: Remove unused import

F401 [*] `urllib.parse.urldefrag` imported but unused
  --> src/requests/compat.py:86:5
   |
84 |     unquote,
85 |     unquote_plus,
86 |     urldefrag,
   |     ^^^^^^^^^
87 |     urlencode,
88 |     urljoin,
   |
help: Remove unused import

F401 [*] `urllib.parse.urlencode` imported but unused
  --> src/requests/compat.py:87:5
   |
85 |     unquote_plus,
86 |     urldefrag,
87 |     urlencode,
   |     ^^^^^^^^^
88 |     urljoin,
89 |     urlparse,
   |
help: Remove unused import

F401 [*] `urllib.parse.urljoin` imported but unused
  --> src/requests/compat.py:88:5
   |
86 |     urldefrag,
87 |     urlencode,
88 |     urljoin,
   |     ^^^^^^^
89 |     urlparse,
90 |     urlsplit,
   |
help: Remove unused import

F401 [*] `urllib.parse.urlparse` imported but unused
  --> src/requests/compat.py:89:5
   |
87 |     urlencode,
88 |     urljoin,
89 |     urlparse,
   |     ^^^^^^^^
90 |     urlsplit,
91 |     urlunparse,
   |
help: Remove unused import

F401 [*] `urllib.parse.urlsplit` imported but unused
  --> src/requests/compat.py:90:5
   |
88 |     urljoin,
89 |     urlparse,
90 |     urlsplit,
   |     ^^^^^^^^
91 |     urlunparse,
92 | )
   |
help: Remove unused import

F401 [*] `urllib.parse.urlunparse` imported but unused
  --> src/requests/compat.py:91:5
   |
89 |     urlparse,
90 |     urlsplit,
91 |     urlunparse,
   |     ^^^^^^^^^^
92 | )
93 | from urllib.request import (
   |
help: Remove unused import

E402 Module level import not at top of file
   --> src/requests/compat.py:93:1
    |
 91 |       urlunparse,
 92 |   )
 93 | / from urllib.request import (
 94 | |     getproxies,
 95 | |     getproxies_environment,
 96 | |     parse_http_list,
 97 | |     proxy_bypass,
 98 | |     proxy_bypass_environment,
 99 | | )
    | |_^
100 |
101 |   builtin_str = str
    |

F401 [*] `urllib.request.getproxies` imported but unused
  --> src/requests/compat.py:94:5
   |
92 | )
93 | from urllib.request import (
94 |     getproxies,
   |     ^^^^^^^^^^
95 |     getproxies_environment,
96 |     parse_http_list,
   |
help: Remove unused import

F401 [*] `urllib.request.getproxies_environment` imported but unused
  --> src/requests/compat.py:95:5
   |
93 | from urllib.request import (
94 |     getproxies,
95 |     getproxies_environment,
   |     ^^^^^^^^^^^^^^^^^^^^^^
96 |     parse_http_list,
97 |     proxy_bypass,
   |
help: Remove unused import

F401 [*] `urllib.request.parse_http_list` imported but unused
  --> src/requests/compat.py:96:5
   |
94 |     getproxies,
95 |     getproxies_environment,
96 |     parse_http_list,
   |     ^^^^^^^^^^^^^^^
97 |     proxy_bypass,
98 |     proxy_bypass_environment,
   |
help: Remove unused import

F401 [*] `urllib.request.proxy_bypass` imported but unused
  --> src/requests/compat.py:97:5
   |
95 |     getproxies_environment,
96 |     parse_http_list,
97 |     proxy_bypass,
   |     ^^^^^^^^^^^^
98 |     proxy_bypass_environment,
99 | )
   |
help: Remove unused import

F401 [*] `urllib.request.proxy_bypass_environment` imported but unused
  --> src/requests/compat.py:98:5
   |
96 |     parse_http_list,
97 |     proxy_bypass,
98 |     proxy_bypass_environment,
   |     ^^^^^^^^^^^^^^^^^^^^^^^^
99 | )
   |
help: Remove unused import

F401 [*] `io` imported but unused
 --> tests/compat.py:6:18
  |
4 |     import StringIO
5 | except ImportError:
6 |     import io as StringIO
  |                  ^^^^^^^^
7 |
8 | try:
  |
help: Remove unused import: `io`

Found 77 errors.
[*] 25 fixable with the `--fix` option.
```

## Code Formatting (Black)
```
would reformat /private/var/folders/xs/z59w57g118v32dht04blnmbc0000gn/T/repo_6uijuw4u/src/requests/_internal_utils.py
would reformat /private/var/folders/xs/z59w57g118v32dht04blnmbc0000gn/T/repo_6uijuw4u/src/requests/hooks.py
would reformat /private/var/folders/xs/z59w57g118v32dht04blnmbc0000gn/T/repo_6uijuw4u/docs/_themes/flask_theme_support.py
would reformat /private/var/folders/xs/z59w57g118v32dht04blnmbc0000gn/T/repo_6uijuw4u/docs/conf.py
would reformat /private/var/folders/xs/z59w57g118v32dht04blnmbc0000gn/T/repo_6uijuw4u/src/requests/exceptions.py
would reformat /private/var/folders/xs/z59w57g118v32dht04blnmbc0000gn/T/repo_6uijuw4u/tests/test_lowlevel.py
would reformat /private/var/folders/xs/z59w57g118v32dht04blnmbc0000gn/T/repo_6uijuw4u/src/requests/sessions.py
would reformat /private/var/folders/xs/z59w57g118v32dht04blnmbc0000gn/T/repo_6uijuw4u/src/requests/models.py
would reformat /private/var/folders/xs/z59w57g118v32dht04blnmbc0000gn/T/repo_6uijuw4u/tests/test_requests.py

Oh no! 💥 💔 💥
9 files would be reformatted, 27 files would be left unchanged.
```

## Pyupgrade
```
diff --git a/docs/conf.py b/docs/conf.py
index 9b81db0..dacd36f 100644
--- a/docs/conf.py
+++ b/docs/conf.py
@@ -1,4 +1,3 @@
-# -*- coding: utf-8 -*-
 #
 # Requests documentation build configuration file, created by
 # sphinx-quickstart on Fri Feb 19 00:05:47 2016.
@@ -57,9 +56,9 @@ source_suffix = ".rst"
 master_doc = "index"
 
 # General information about the project.
-project = u"Requests"
-copyright = u'MMXVIX. A Kenneth Reitz Project'
-author = u"Kenneth Reitz"
+project = "Requests"
+copyright = 'MMXVIX. A Kenneth Reitz Project'
+author = "Kenneth Reitz"
 
 # The version info for the project you're documenting, acts as replacement for
 # |version| and |release|, also used in various other places throughout the
@@ -247,7 +246,7 @@ latex_elements = {
 # (source start file, target name, title,
 #  author, documentclass [howto, manual, or own class]).
 latex_documents = [
-    (master_doc, "Requests.tex", u"Requests Documentation", u"Kenneth Reitz", "manual")
+    (master_doc, "Requests.tex", "Requests Documentation", "Kenneth Reitz", "manual")
 ]
 
 # The name of an image file (relative to this directory) to place at the top of
@@ -275,7 +274,7 @@ latex_documents = [
 
 # One entry per manual page. List of tuples
 # (source start file, name, description, authors, manual section).
-man_pages = [(master_doc, "requests", u"Requests Documentation", [author], 1)]
+man_pages = [(master_doc, "requests", "Requests Documentation", [author], 1)]
 
 # If true, show URL addresses after external links.
 # man_show_urls = False
@@ -290,7 +289,7 @@ texinfo_documents = [
     (
         master_doc,
         "Requests",
-        u"Requests Documentation",
+        "Requests Documentation",
         author,
         "Requests",
         "One line description of project.",
```

## Security Audit
- ✅ No known vulnerabilities found.
