.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Protocol Buffers (Protobuf)
===========================

Überblick
---------

+-----------------------+-------+-------------------------------------------------------+
| Unterstützung für     | \+    | Protobuf erlaubt euch Datenstrukturen in              |
| Datenstrukturen       |       | ``*.proto``-Dateien zu definieren. Dabei unterstützt  |
|                       |       | Protobuf viele primitive Datentypen, die zu           |
|                       |       | verschachtelten Datentypen kombiniert werden können.  |
+-----------------------+-------+-------------------------------------------------------+
| Standardisierung      | +-    | Protobuf ist ein stark typisierter flexibler Standard.|
+-----------------------+-------+-------------------------------------------------------+
| Schema-IDL            | ++    | Eingabauter IDL-Compiler                              |
+-----------------------+-------+-------------------------------------------------------+
| Sprachunterstützung   | ++    | Das protobuf-Format wird gut von den meisten          |
|                       |       | Programmiersprachen unterstützt.                      |
+-----------------------+-------+-------------------------------------------------------+
| Menschliche Lesbarkeit| -\-   | Protobuf ist nicht für Menschen lesbar.               |
+-----------------------+-------+-------------------------------------------------------+
| Geschwindigkeit       | ++    | Protobuf ist sehr schnell, vor allem in C++.          |
+-----------------------+-------+-------------------------------------------------------+
| Dateigröße            | ++    | Protobuf ist das kompakteste Format.                  |
+-----------------------+-------+-------------------------------------------------------+

.. seealso::

    * `Home <https://protobuf.dev>`__
    * `GitHub <https://github.com/protocolbuffers/protobuf>`__
    * `Language Guide (proto3)
      <https://protobuf.dev/programming-guides/proto3/>`_
    * Buf

      * `Home <https://buf.build/>`__
      * `Docs <https://buf.build/docs/introduction>`__
      * `GitHub <https://github.com/bufbuild/buf>`__

    * :doc:`../apis/grpc/index`
