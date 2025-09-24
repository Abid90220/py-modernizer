# Python Project Audit Report

- **Generated:** 2025-09-24T16:16:10+00:00
- **Repo Path:** `/var/folders/xs/z59w57g118v32dht04blnmbc0000gn/T/repo__2y6j7mx`

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

F401 `simplejson` imported but unused; consider using `importlib.util.find_spec` to test for availability
  --> src/requests/compat.py:60:26
   |
58 | has_simplejson = False
59 | try:
60 |     import simplejson as json
   |                          ^^^^
61 |
62 |     has_simplejson = True
   |
help: Remove unused import: `simplejson`

F401 `StringIO` imported but unused; consider using `importlib.util.find_spec` to test for availability
 --> tests/compat.py:4:12
  |
3 | try:
4 |     import StringIO
  |            ^^^^^^^^
5 | except ImportError:
6 |     pass
  |
help: Remove unused import: `StringIO`

Found 73 errors (26 fixed, 47 remaining).
```

## Code Formatting (Black)
```
reformatted /private/var/folders/xs/z59w57g118v32dht04blnmbc0000gn/T/repo__2y6j7mx/src/requests/_internal_utils.py
reformatted /private/var/folders/xs/z59w57g118v32dht04blnmbc0000gn/T/repo__2y6j7mx/src/requests/hooks.py
reformatted /private/var/folders/xs/z59w57g118v32dht04blnmbc0000gn/T/repo__2y6j7mx/docs/_themes/flask_theme_support.py
reformatted /private/var/folders/xs/z59w57g118v32dht04blnmbc0000gn/T/repo__2y6j7mx/src/requests/exceptions.py
reformatted /private/var/folders/xs/z59w57g118v32dht04blnmbc0000gn/T/repo__2y6j7mx/docs/conf.py
reformatted /private/var/folders/xs/z59w57g118v32dht04blnmbc0000gn/T/repo__2y6j7mx/tests/test_lowlevel.py
reformatted /private/var/folders/xs/z59w57g118v32dht04blnmbc0000gn/T/repo__2y6j7mx/src/requests/sessions.py
reformatted /private/var/folders/xs/z59w57g118v32dht04blnmbc0000gn/T/repo__2y6j7mx/src/requests/models.py
reformatted /private/var/folders/xs/z59w57g118v32dht04blnmbc0000gn/T/repo__2y6j7mx/tests/test_requests.py

All done! ✨ 🍰 ✨
9 files reformatted, 27 files left unchanged.
```

## Pyupgrade
```
pyupgrade available but not applied (use --check-fixes or --apply-fixes).
```

## Security Audit
- ✅ No known vulnerabilities found.
