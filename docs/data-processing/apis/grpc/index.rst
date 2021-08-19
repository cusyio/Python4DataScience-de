gRPC
====

gRPC ist ein modernes Open-Source-RPC (Remote Procedure Call)-Framework.
Standardmäßig verwendet gRPC :doc:`../serialisation-formats/protobuf` als
Interface Definition Language (IDL) zur Beschreibung sowohl des Interfaces als
auch der Struktur der *Payload Messages*. In gRPC kann eine Clientanwendung
direkt eine Methode auf einer entfernten Serveranwendung aufrufen als wäre es
ein lokales Objekt, sodass verteilte Anwendungen und Dienste einfacher erstellt
werden können. Wie in vielen RPC-Systemen basiert gRPC auf der Idee, einen
Service zu definieren und die Methoden anzugeben, die mit ihren Parametern und
Rückgabetypen aus der Ferne aufgerufen werden können. Der Server implementiert
dieses Interface, um die Client-Aufrufe zu verarbeiten. Für den Client wurde
ein sog. *Stub* generiert, der dieselben Methoden wie der Server bereitstellt.

Im folgenden die wesentlichen Design-Prinzipien von gRPC:

* gRPC kann auf allen gängigen Entwicklungsplattformen und in vielen
  verschiedenen Sprachen erstellt werden.
* Es ist auf Geräten mit geringer CPU- und Speicherfähigkeiten funktionsfähig
  sein, so neben Android [#]_- und iOS-Geräten auch auf MicroPython-Boards und
  in Browsern [#]_ [#]_.
* Es ist lizenziert unter Apache License 2.0 und nutzt offene Standards wie z.B.
  HTTP/2 und Quick UDP Internet Connections (QUIC).
* gRPC ist interoperabel und kann daher z.B. auch im LoRaWan (Long Range Wide
  Area  Network) genutzt werden.
* Die einzelnen Layer können unabhängig voneinander entwickelt werden. So kann
  z.B. der Transport-Layer (OSI-Layer 4) unabhängig vom Application-Layer
  (OSI-Layer 7) entwickelt werden.
* gRPC unterstützt unterschiedliche Serialisierungsformate, u.a.
  :doc:`../serialisation-formats/protobuf`,
  :doc:`../serialisation-formats/json` [#]_, :doc:`../serialisation-formats/xml` und
  Thrift)
* Asynchrone und synchrone (blockierende) Verarbeitung werden in den meisten
  Sprachen unterstützt.
* Das Streaming von Nachrichten in einem einzelnen RPC-Aufruf wird unterstützt.
* gRPC erlaubt Protokollerweiterungen für Sicherheit, Integritätsprüfung,
  Lastausgleich, Failover etc.

.. graphviz::

    digraph grpc_concept {
        rankdir="LR";
        graph [fontname = "Calibri", fontsize="16", penwidth="5px", overlap=false];
        node [fontname = "Calibri", fontsize="16", style="bold", penwidth="5px"];
        edge [fontname = "Calibri", fontsize="16", style="bold", penwidth="5px"];
        tooltip="gRPC concept";

        // C++ service
        subgraph "cluster_cpp_service" {
            label="C++ Service";
            fontcolor="#2D7BFD";
            shape=box;
            style= "rounded";
            color="#2D7BFD";
            "grpc_server" [
                label="gRPC server",
                fontcolor="#640FFB"
                shape=box,
                style= "rounded",
                color="#640FFB"
                ];
            }

        // Python-Stub
        subgraph cluster_python_client {
            label="Python client";
            fontcolor="#2D7BFD";
            shape=box;
            style= "rounded";
            color="#2D7BFD";
            grpc_python_stub [
                label="gRPC Python-Stub",
                fontcolor="#640FFB"
                shape=box,
                style= "rounded",
                color="#640FFB"
                ];
            }

        // Android-Java-Stub
        subgraph cluster_android_java_client {
            label="Android-Java client";
            fontcolor="#2D7BFD";
            shape=box;
            style= "rounded";
            color="#2D7BFD";
            grpc_android_java_stub [
                label="gRPC Android-Java-Stub",
                fontcolor="#640FFB"
                shape=box,
                style= "rounded",
                color="#640FFB"
                ];
            }

        grpc_python_stub -> grpc_server [label="Proto-Request", fontcolor="#640FFB", color="#7539FC"]
        grpc_android_java_stub -> grpc_server [label="Proto-Request", fontcolor="#640FFB", color="#7539FC"]
        grpc_server -> grpc_python_stub [label="Proto-Response", fontcolor="#300099", color="#300099"]
        grpc_server -> grpc_android_java_stub [label="Proto-Response", fontcolor="#300099", color="#300099"]

    }

Ausgehend von einer Schnittstellendefinition in einer ``.proto``-Datei bietet
gRPC Protocol-Compiler-Plugins, die clientseitige und serverseitige APIs
generieren.  Das `gRPC-Protokoll
<https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md>`_ gibt abstrakt
die Kommunikation zwischen Clients und Servern an:

#. Zuerst wird der Stream vom Client mit einem obligatorischen ``Call Header``
   gestartet

   #. gefolgt von optionalen ``Initial-Metadata``
   #. gefolgt von optionalen ``Payload Messages``.

   Die Inhalte von ``Call Header`` und ``Initial Metadata`` werden als
   HTTP/2-Headers mit ``HPACK`` komprimiert.

#. Der Server antwortet mit optionalen ``Initial-Metadata``

   #. gefolgt von ``Payload Messages``
   #. und schließlich mit obligatorischem ``Status`` und optionalen
      ``Status-Metadata``.

   Payload-Nachrichten werden in einen Byte-Stream serialisiert, der in
   HTTP/2-Frames fragmentiert ist. ``Status`` und ``Trailing-Metadata`` werden
   als HTTP/2-Trailing-Headers gesendet.

Im Gegensatz zu :doc:`../fastapi/index` kann die gRPC-API jedoch nicht einfach
auf der Kommandozeile mit cURL getestet werden. Ggf. könnt ihr jedoch `grpcurl
<https://github.com/fullstorydev/grpcurl>`_ verwenden. Dies setzt jedoch voraus,
dass der gRPC-Server das `GRPC Server Reflection Protocol
<https://grpc.github.io/grpc/core/md_doc_server-reflection.html>`_ unterstützt.
Üblicherweise sollte *Reflection* jedoch nur in der Entwicklungsphase zur
Verfügung stehen. Dann könnt ihr jedoch ``grpcurl`` aufrufen, z.B. mit:

.. code-block:: console

    $ grpcurl localhost:9111 list

.. seealso::
    * `Home <https://grpc.io/>`_
    * `GitHub <https://github.com/grpc/grpc>`_
    * `gRPC Blog <https://grpc.io/blog/>`_

----

.. [#] `gRPC in Android Java <https://grpc.io/docs/platforms/android/java/quickstart/>`_
.. [#] `gRPC-Web is Generally Available <https://grpc.io/blog/grpc-web-ga/>`_
.. [#] `gRPC-Web Client Runtime Library <https://www.npmjs.com/package/grpc-web>`_
.. [#] `gRPC + JSON <https://grpc.io/blog/grpc-with-json/>`_

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    install
    example
    test
