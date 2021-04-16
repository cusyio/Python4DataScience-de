gRPC testen
===========

``pytest-grpc``
---------------

gRPC lässt sich automatisiert testen z.B. mit `pytest-grpc
<https://pypi.org/project/pytest-grpc>`_.

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
   * `GitHub <https://github.com/kataev/pytest-grpc>`_
   * `Beispiel
     <https://github.com/kataev/pytest-grpc/blob/master/example/test_example.py>`_

Wireshark
---------

`Wireshark <https://www.wireshark.org/>`_ ist ein Open-Source-Tool zur Analyse
von Netzwerkprotokollen. Im Folgenden zeigen wir Euch, wie Ihr den `gRPC
<https://gitlab.com/wireshark/wireshark/-/wikis/gRPC>`_- und den `Protobuf
<https://gitlab.com/wireshark/wireshark/-/wikis/Protobuf>`_-Dissectors verwenden
könnt. Sie erleichtern Euch das Zerlegen (Dekodieren) von gRPC-Nachrichten, die
im :doc:`Protobuf <../serialisation-formats/protobuf>`- oder
:doc:`../serialisation-formats/json`-Format serialisiert sind. Zudem könnt Ihr
damit das Server-, Client- und bidirektionales gRPC-Streaming analysieren.

.. note::
    Üblicherweise kann Wireshark nur gRPC-Messages im Klartext analysieren. Für
    das Sezieren von TLS-Session benötigt Wireshark den geheimen Schlüssel,
    deren Export jedoch zum heutigen Zeitpunkt nur `Go gRPC
    <https://grpc.io/docs/languages/go/>`_ unterstützt [#]_.

.. seealso::
    * `Analyzing gRPC messages using Wireshark
      <https://grpc.io/blog/wireshark/>`_

----

.. [#] `How to Export TLS Master keys of gRPC
       <https://gitlab.com/wireshark/wireshark/-/wikis/How-to-Export-TLS-Master-keys-of-gRPC>`_
