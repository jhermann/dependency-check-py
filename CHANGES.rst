=========
Changelog
=========

* :release:`0.6.0 <2021-06-21>`
* :support:`8` Update default upstream version to 6.2.2
* :support:`7` Changed download URLs to new GitHub hosting
* :support:`0` Changed data URLs to v1.1 JSON format
* Adapt or unset any environment variables you have, and do a full re-install
  with a full data retrieval (``rm -rf ~/.local/dependency-check/``)

* :release:`0.5.0 <2020-01-08>`
* :support:`0` Update default upstream version to 5.2.4
* :support:`0` You MUST update your local installation to a 5.x version (see README)
* :support:`0` You MUST also update ``DEPENDENCY_CHECK_NVD_URL`` in case you've set that, and the mirror it points to (use JSON compressed data files instead of XML)

* :release:`0.2.0 <2017-10-09>`
* :support:`0` Update default upstream version to 2.1.1 (from 1.3.1)
* :bug:`2` Python 3 fixes (octal literal, urlopen)
* :feature:`0` Added ``DEPENDENCY_CHECK_NVD_URL`` environment variable
* :support:`0` Travis CI for Python 3.4

* :release:`0.1.0 <2015-11-23>`
* :feature:`0` Redirect calls to .sh / .bat launcher script
* :feature:`0` Auto-install OWASP release archive
