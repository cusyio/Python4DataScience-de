gRPC-Beispiel
=============

Standardmäßig verwendet gRPC :doc:`../serialisation-formats/protobuf` zur
Serialisierung von Daten, obwohl sie auch mit anderen Datenformaten wie JSON
funktionieren.

Definieren der Datenstruktur
----------------------------

Der erste Schritt bei der Arbeit mit Protocol-Buffers besteht darin, die
Struktur für die Daten zu definieren, die Sie in einer ``.proto``-Datei
serialisieren möchten. Protocol-Buffers-Daten sind als *Nachrichten*
strukturiert, wobei jede Nachricht ein kleiner logischer Datensatz ist, der eine
Reihe von Name-Wert-Paaren enthält, die *fields* genannt werden.
``accounts.proto`` ist ein einfaches Beispiel hierfür:

.. literalinclude:: accounts.proto
   :language: proto
   :lines: 1-6

.. warning::
    Beachtet bitte, dass Ihr üblicherweise **nicht** einfach ``uint32`` für
    User- oder Group-IDs verwenden solltet, da diese viel zu einfach zu erraten
    wären. Hierfür könnt Ihr z.B. eine `RFC 4122
    <https://tools.ietf.org/html/rfc4122>`_-konforme Implementierung verwenden.
    Eine entsprechende Protobuf-Konfiguration findet Ihr in
    :download:`rfc4122.proto`.

Nachdem Ihr Eure Datenstruktur definiert habt, könnt Ihr das
Protocol-Buffer-Compiler-Protokoll ``protoc`` verwenden, um Deskriptoren in
Eurer bevorzugten Sprache zu erzeugen. Diese bietet einfache Zugriffsfunktionen
für jedes Feld sowie Methoden zur Serialisierung der gesamten Struktur. Wenn
Eure Sprache z.B. Python ist, werden beim Ausführen des Compilers für das obige
Beispiel Deklaratoren generiert, die Ihr dann in Eurer Anwendung zum Einpflegen,
Serialisieren und Abrufen von Protocol-Buffer-Nachrichten verwenden könnt.

Definieren des gRPC-Dienstes
----------------------------

gRPC-Dienste werden ebenfalls in den ``.proto``-Dateien definiert, wobei die
RPC-Methodenparameter und Rückgabetypen als Protocol-Buffer-Nachrichten
angegeben werden:

.. literalinclude:: accounts.proto
   :language: proto
   :lines: 8-

Generieren des gRPC-Codes
-------------------------

.. code-block:: console

    $ pipenv install grpcio grpcio-tools
    $ pipenv run python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. person.proto

Dies erzeugt zwei Dateien:

:download:`accounts_pb2.py`
    die die generierten Anfrage- und Antwortklassen enthält.
:download:`accounts_pb2_grpc.py`
    die die generierten Client- und Server-Klassen enthält.

Den Server aktualisieren
------------------------

Jetzt können wir unsere Anrede ``Salutation`` in :download:`accounts_server.py`
definieren:

.. literalinclude:: accounts_server.py
   :language: python

Aktualisieren des Clients
-------------------------

Wir erstellen :download:`accounts_client.py` mit der Methode ``run``:

.. literalinclude:: accounts_client.py
   :language: python

Client und Server ausführen
---------------------------

#. Führt den Server aus:

   .. code-block:: console

        $ pipenv run python accounts_server.py

#. Führt den Client von einem anderen Terminal aus:

   .. code-block:: console

    $ pipenv run python accounts_client.py
    Account created: tom
    account {
      account_id: 1
      account_name: "veit"
    }

    account {
      account_id: 2
      account_name: "andy"
    }
