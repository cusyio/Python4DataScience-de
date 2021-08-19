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
:download:`accounts.proto` ist ein einfaches Beispiel hierfür:

.. literalinclude:: accounts.proto
   :language: proto
   :lines: 1-6

.. warning::
    Beachtet bitte, dass ihr üblicherweise **nicht** einfach ``uint32`` für
    User- oder Group-IDs verwenden solltet, da diese viel zu einfach zu erraten
    wären. Hierfür könnt ihr z.B. eine `RFC 4122
    <https://tools.ietf.org/html/rfc4122>`_-konforme Implementierung verwenden.
    Eine entsprechende Protobuf-Konfiguration findet ihr in
    :download:`rfc4122.proto`.

Nachdem ihr eure Datenstruktur definiert habt, könnt ihr das
Protocol-Buffer-Compiler-Protokoll ``protoc`` verwenden, um Deskriptoren in
eurer bevorzugten Sprache zu erzeugen. Diese bietet einfache Zugriffsfunktionen
für jedes Feld sowie Methoden zur Serialisierung der gesamten Struktur. Wenn
eure Sprache z.B. Python ist, werden beim Ausführen des Compilers für das obige
Beispiel Deklaratoren generiert, die ihr dann in eurer Anwendung zum Einpflegen,
Serialisieren und Abrufen von Protocol-Buffer-Nachrichten verwenden könnt.

Definieren des gRPC-Dienstes
----------------------------

gRPC-Dienste werden ebenfalls in den ``.proto``-Dateien definiert, wobei die
RPC-Methodenparameter und Rückgabetypen als Protocol-Buffer-Nachrichten
angegeben werden:

.. literalinclude:: accounts.proto
   :language: proto
   :lines: 8-23,32-34,36

Generieren des gRPC-Codes
-------------------------

.. code-block:: console

    $ pipenv install grpcio grpcio-tools
    $ pipenv run python -m grpc_tools.protoc --python_out=. --grpc_python_out=. accounts.proto

Dies erzeugt zwei Dateien:

:download:`accounts_pb2.py`
    enthält Klassen für die in ``accounts.proto`` definierten Messages.
:download:`accounts_pb2_grpc.py`
    enthält die definierten Klassen ``AccountsStub`` für den Aufruf von RPCs,
    ``AccountsServicer`` für die API-Definition des Services und eine Funktion
    ``add_AccountsServicer_to_server`` für den Server.

Server erstellen
----------------

Hierfür schreiben wir die Datei :download:`accounts_server.py`:

.. literalinclude:: accounts_server.py
   :language: python

Client erstellen
----------------

Hierfür schreiben wir :download:`accounts_client.py`:

.. literalinclude:: accounts_client.py
   :language: python

Client und Server starten
-------------------------

#. Starten des Server:

   .. code-block:: console

        $ pipenv run python accounts_server.py

#. Starten des Client von einem anderen Terminal aus:

   .. code-block:: console

    $ pipenv run python accounts_client.py
    Account created: tom
