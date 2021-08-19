**A**\pplication **P**\rogramming **I**\nterface (API)
======================================================

APIs können genutzt werden um die Daten bereitstellen zu können. Mit
:doc:`fastapi/index` steht euch eine Bibliothek zur Verfügung, die basierend auf
`OpenAPI <https://www.openapis.org/>`_ und `JSON Schema
<http://json-schema.org/>`_ APIs und Dokumentationen generieren kann.
:doc:`grpc/index` ist hingegen ein modernes Open-Source-RPC-Framework, das
HTTP/2 und QUIC verwendet.

Um das Design eurer API festzulegen, könnt ihr euch an `Zalandos API Styleguide
<https://opensource.zalando.com/restful-api-guidelines/>`_ orientieren. Später
könnt ihr dann mit `Zally <https://github.com/zalando/zally>`_ automatisiert
die Qualität eurer API überprüfen. Darüberhinaus könnt ihr auch eure eigenen
Regeln für Zally definieren, siehe `Rule Development Manual
<https://github.com/zalando/zally/blob/master/documentation/rule-development.md>`_.

.. see also::
   * `REST API Design – Resource Modeling
     <https://www.thoughtworks.com/insights/blog/rest-api-design-resource-modeling>`_
   * `Richardson Maturity Model – steps toward the glory of REST
     <https://martinfowler.com/articles/richardsonMaturityModel.html>`_
   * `Irresistible APIs – Designing web APIs that developers will love
     <https://www.manning.com/books/irresistible-apis>`_
   * `REST in Practice
     <https://www.oreilly.com/library/view/rest-in-practice/9781449383312/>`_
   * `Build APIs You Won’t Hate <https://leanpub.com/build-apis-you-wont-hate>`_
   * `Representational State Transfer (REST)
     <https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm>`_

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    fastapi/index
    grpc/index
