Changelog
=========

2.2.0
-----

* Removes any jQuery code from this project's JavaScript


2.0.0
-----

* Add support for Django 1.11
* Add support for Django 1.10
* Drop support for Django < 1.8 as it is no `longer officially supported <https://www.djangoproject.com/download/#supported-versions>`__.
* Switch to pytest


Prior 1.1
---------

* **1.0.12** added German translation thanks to dated_
* **1.0.11** added Catalan translation thanks to joansv_
* **1.0.9** added unofficial support for Django 1.10 thanks to farin_
* **1.0.8** added Spanish translation thanks to jonashagstedt_
* **1.0.7** added Russian translation thanks to paschembri_
* **1.0.6** ``django.core.context_processors.request`` is still required but if not available in template context a
  warning will be raise instead of a ``KeyError``
* **1.0.5** added Dutch translation thanks to douwevandermeij_
* **1.0.4** context_instance is now passed to the banner template
* **1.0.3** added Italian translation thanks to Jiloc_

Some very minor changes have not been listed.


.. _dated: https://github.com/dated
.. _douwevandermeij: https://github.com/douwevandermeij
.. _farin: https://github.com/farin
.. _Jiloc: https://github.com/Jiloc
.. _joansv: https://github.com/joansv
.. _jonashagstedt: https://github.com/jonashagstedt
.. _paschembri: https://github.com/paschembri
