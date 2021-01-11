=================
Pydantic QuantLib
=================


.. image:: https://img.shields.io/pypi/v/pydantic_quantlib.svg
        :target: https://pypi.python.org/pypi/pydantic_quantlib

.. image:: https://github.com/gecBurton/inference_logic/workflows/PythonPackage/badge.svg
        :target: https://github.com/gecBurton/inference_logic/workflows/PythonPackage/badge.svg

.. image:: https://readthedocs.org/projects/pydantic-quantlib/badge/?version=latest
        :target: https://pydantic-quantlib.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




QuantLib Python Objects with Typing


* Free software: MIT license
* Documentation: https://pydantic-quantlib.readthedocs.io.


Features
--------

This package uses pydantic_ to wrap QuantLib_ to provide a set of Typed class factories.

The pydantic models are auto-generated from the QuantLib SWIG bindings. The autogen code is available on request.

In the following example we construct a European Option.

.. code-block:: python

    import pydantic_quantlib as pql

    payoff = pql.PlainVanillaPayoff(type=pql.OptionType.Put, strike=40)

    european_exercise = pql.EuropeanExercise(date=pql.Date(d=4, m=1, y=2022))

    european_option = pql.VanillaOptionBase(payoff=payoff, exercise=european_exercise)

The option can be converted to the usual QuantLib_ object for computation as seen in this fuller example_.

.. code-block:: python

    >>> european_option.to_quantlib()
    '<QuantLib.QuantLib.VanillaOption; proxy of <Swig Object of type 'ext::shared_ptr< VanillaOption > *' at 0x7f6559ddabd0> >'


it can also be printed:

.. code-block:: python

    >>> print(european_option)
    'PlainVanillaPayoff(type=<OptionType.Put: -1>, strike=40.0) exercise=EuropeanExercise(date=Date0(d=4.0, m=1.0, y=2022.0))'

it can be converted to JSON:

.. code-block:: python

    >>> european_option.json()
    '{"resource_name": "VanillaOption", "payoff": {"resource_name": "PlainVanillaPayoff", "type": -1, "strike": 40.0}, "exercise": {"resource_name": "EuropeanExercise", "date": {"resource_name": "Date", "d": 4, "m": 1, "y": 2022}}}'

and it can be loaded from JSON:

.. code-block:: python

    >>> json_repr = '{"resource_name": "VanillaOption", "payoff": {"resource_name": "PlainVanillaPayoff", "type": -1, "strike": 40.0}, "exercise": {"resource_name": "EuropeanExercise", "date": {"resource_name": "Date", "d": 4, "m": 1, "y": 2022}}}'
    >>> pql.VanillaOption.parse_obj(json.loads(json_repr))


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _pyql: https://github.com/enthought/pyql/blob/master/examples/basic_example.py
.. _pydantic: https://pydantic-docs.helpmanual.io/
.. _QuantLib: https://pypi.org/project/QuantLib/
.. _example: https://github.com/gecBurton/pydantic-quantlib/blob/main/tests/test_basic.py
