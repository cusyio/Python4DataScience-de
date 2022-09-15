Deployment und Release Branches
===============================

Deployment-Branches
-------------------

Deployment-Branches empfehlen sich, wenn ihr :abbr:`z.B. (zum Beispiel)` den
Release-Zeitpunkt nicht selbst bestimmen könnt, wie bei einer iOS-Anwendung, die
die App-Store-Validierung bestehen muss, oder wenn euch nur ein bestimmtes
Zeitfenster für die Bereitstellung zur Verfügung steht. In diesen Fällen
empfiehlt sich ein *Production*-Branch, der den bereitgestellten Code
widerspiegelt. Ein solcher Arbeitsablauf verhindert dann zusätzliche
Arbeitsaufwände bei :doc:`../rebase`, :doc:`../tag` und Git merge.

Angenommen, ihr verfügt über eine ``test``-, ``stage``- und ``prod``-Umgebung,
dann wird zunächst ein Merge- oder Pull-Request für den ``test``-Branch
gestellt. Sofern alle Tests bestanden wurden, können die Änderungen auch in den
``stage``-Branch übernommen werden. Wenn die Qualitätssicherung beschließt, dass
der Code produktionsreif ist, kann er auch in den ``main``-Branch übernommen
werden. Dieser Vorgang kann sich mehrfach wiederholen, bis :abbr:`z.B. (zum
Beispiel)` der Zeitpunkt für das *Going Life* dieser Änderungen gekommen ist und
ein ``prod``-Branch erstellt werden kann.

.. _release-branches:

Release-Branches
----------------

Wenn Software an Kunden geliefert werden soll, empfehlen sich :abbr:`sog.
(sogenannte)` Release-Branches. In diesen Fällen sollte jeder Branch eine *Minor
Version* erhalten, also :abbr:`z.B. (zum Beispiel)` ``2.7`` oder ``3.10``.
Üblicherweise werden diese Branches so spät wie möglich aus dem ``main``-Branch
erzeugt um bei Bugfixes die Anzahl der Merges, die auf mehrere Branches verteilt
werden müssen, zu reduzieren. Nachdem ein neuer Release-Branch erstellt wurde,
erhält dieser nur noch Bugfixes. Meist werden diese zunächst in den
``main``-Branch übernommen und kommen anschließend von dort mit
:doc:`../cherry-pick` in den Release-Branch, :abbr:`z.B. (zum Beispiel)`:

.. code-block:: console

    $ git checkout 3.10
    $ git cherry-pick 61de025
    [3.10 b600967] Fix bug #17
     Date: Thu Sep 15 11:17:35 2022 +0200
     1 file changed, 9 insertions(+)

Dieser *upstream first*-Ansatz wird :abbr:`u.a. (unter anderem)` von `Google
<https://www.chromium.org/chromium-os/chromiumos-design-docs/upstream-first>`_
und `Red Hat
<https://www.redhat.com/en/blog/a-community-for-using-openstack-with-red-hat-rdo>`_
verwendet. Jedes Mal, wenn ein Bugfix in einen Release-Branch übernommen wurde,
wird das Release mit einem :doc:`../tag` um eine Patch-Version angehoben,
:abbr:`s.a. (siehe auch)` `Semantic Versioning <https://semver.org/>`_.
