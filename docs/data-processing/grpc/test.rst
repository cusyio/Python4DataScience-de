gRPC testen
===========

gRPC lässt sich automatisiert testen mit pytest-grpc.

#. Zunächst installieren wir pytest-grpc:

   .. code-block:: console

    $ pipenv install pytest-grpc
    Installing pytest-grpc…
    Adding pytest-grpc to Pipfile's [packages]…
    ✔ Installation Succeeded
    …

#. Dann erstellen wir für unser :doc:`example` ein :term:`Test Fixture <Test
   Fixture (Prüfvorrichtung)>` mit:

   .. literalinclude:: tests/test_accounts.py
      :language: python
      :lines: 2,4-25

   .. seealso::
      * `pytest fixtures <https://docs.pytest.org/en/latest/fixture.html>`_

#. Anschließend können wir Tests schreiben, z.B.:

   .. literalinclude:: tests/test_accounts.py
      :language: python
      :lines: 28-44

#. Auch die Authentifizierung lässt sich testen, z.B. mit:

   .. literalinclude:: tests/test_accounts.py
      :language: python
      :lines: 1,3,47-97

#. Anschließend können wir gegen einen realen gRPC-Server testen mit:

   .. code-block:: console

    $ pipenv run pytest --fixtures tests/

   oder direkt gegen den Python-Code:

   .. code-block:: console

    $ pipenv run pytest --fixtures tests/ --grpc-fake-server
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.3, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
    rootdir: /Users/veit/cusy/trn/jupyter-tutorial/docs/data/grpc
    plugins: grpc-0.8.0
    collected 2 items

    tests/test_accounts.py .F                                                [100%]
    …

.. seealso::
   * `PyPI <https://pypi.org/project/pytest-grpc/>`_
   * `GitHub <https://github.com/kataev/pytest-grpc>`_
   * `Beispiel
     <https://github.com/kataev/pytest-grpc/blob/master/example/test_example.py>`_
