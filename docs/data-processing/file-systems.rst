.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Dateisysteme
============

High-Level-APIs
---------------

`PyFilesystem <https://www.pyfilesystem.org>`_
    arbeitet mit Dateien und Verzeichnissen in Archiven, in Storages, in der
    Cloud :abbr:`usw (und so weiter)`.

    .. image::
       https://raster.shields.io/github/stars/pyfilesystem/pyfilesystem2
    .. image::
       https://raster.shields.io/github/contributors/pyfilesystem/pyfilesystem2
    .. image::
       https://raster.shields.io/github/commit-activity/y/pyfilesystem/pyfilesystem2
    .. image::
       https://raster.shields.io/github/license/pyfilesystem/pyfilesystem2

    Integrierte Dateisysteme:

    * `AppFS <https://www.pyfilesystem.org/page/appfs/>`_ für in
      Betriebssystemen vordefinierte Speicherorte, in denen Anwendungen Daten
      speichern können
    * `FTPFS <https://www.pyfilesystem.org/page/ftpfs/>`_ für die Arbeit mit
      FTP-Servern
    * `MemoryFS <https://www.pyfilesystem.org/page/memoryfs/>`_ für Caches,
      temporäre Datenspeicher, Unit-Tests :abbr:`usw. (und so weiter)`, die
      im Arbeitsspeicher existieren
    * `MountFS <https://www.pyfilesystem.org/page/mountfs/>`_ für ein virtuelles
      Dateisystem, das andere Dateisysteme
      einhängen kann
    * `MultiFS <https://www.pyfilesystem.org/page/multifs/>`_ für ein virtuelles
      Dateisystem, das andere Dateisysteme
      kombiniert
    * `OSFS <https://www.pyfilesystem.org/page/osfs/>`_ für das OS-Dateisystem
    * `TarFS <https://www.pyfilesystem.org/page/tarfs/>`_ liest und schreibt
      komprimierte Tar-Archive
    * `TempFS <https://www.pyfilesystem.org/page/tempfs/>`_ enthält temporäre
      Daten
    * `ZipFS <https://www.pyfilesystem.org/page/zipfs/>`_ ließt und schreibt
      Zip-Dateien

    Dateisysteme der PyFilesystem Organisation auf GitHub:

    * `DropBoxFS <https://www.pyfilesystem.org/page/dropboxfs/>`_
    * `S3FS <https://www.pyfilesystem.org/page/s3fs/>`_
    * `WebDavFS <https://www.pyfilesystem.org/page/index-of-filesystems/>`_

    Dateisysteme von Drittentwicklern:

    * `fs_basespace <https://github.com/emedgene/fs_basespace>`_ für lesende
      Zugriffe auf den Illumina Basespace
    * `fs.dropboxfs <https://github.com/rkhwaja/fs.dropboxfs>`_ für Dropbox
    * `fs.imapfs <https://github.com/Maggi-Andrea/fs.imapfs>`_ für Imap
    * `fs.googledrivefs <https://github.com/rkhwaja/fs.googledrivefs>`_ für
      Google Drive
    * `fs.onedrivefs <https://github.com/rkhwaja/fs.onedrivefs>`_ für OneDrive
    * `fs.smbfs <https://github.com/althonos/fs.smbfs>`_ für Samba
    * `fs.sshfs <https://github.com/althonos/fs.sshfs>`_ für  SSH mit
      :ref:`paramiko`
    * `mp-fs-wsgidav <https://github.com/mikespub-org/mp-fs-wsgidav>`_ für
      WsgiDAV

.. _fsspec:

`fsspec <https://filesystem-spec.readthedocs.io/en/latest/>`__
    Einheitliche Python-Schnittstelle für viele lokale, entfernte und
    eingebettete Dateisysteme und Byte-Storages. Wenn ihr in eurem Projekt
    :abbr:`z.B. (zum Beispiel)` bereits :doc:`/workspace/pandas/index`,
    :doc:`/data-processing/intake/index`, :doc:`/performance/dask` oder
    :doc:`DVC </productive/dvc/index>` verwendet, ist ``fsspec`` bereits
    vorhanden.

    .. image::
       https://raster.shields.io/github/stars/fsspec/filesystem_spec
    .. image::
       https://raster.shields.io/github/contributors/fsspec/filesystem_spec
    .. image::
       https://raster.shields.io/github/commit-activity/y/fsspec/filesystem_spec
    .. image::
       https://raster.shields.io/github/license/fsspec/filesystem_spec

    Neben den `integrierten Implementierungen
    <https://filesystem-spec.readthedocs.io/en/latest/api.html#built-in-implementations>`_ gibt es auch viele Erweiterungen, :abbr:`z.B. (zum Beispiel)` für:

    * `abfs <https://github.com/fsspec/adlfs>`_ für den Azure Blob-Service
    * `adl <https://github.com/fsspec/adlfs>`_ für den Azure DataLake-Storage
    * `alluxiofs <https://github.com/fsspec/alluxiofs>`_ für den verteilten
      Cache von Alluxio
    * `boxfs <https://github.com/IBM/boxfs>`_ für den Zugriff auf
      Box-Dateispeicher
    * `dropbox <https://github.com/fsspec/dropboxdrivefs>`_ für den Zugriff auf
      Dropbox-Freigaben
    * `dvc <https://github.com/iterative/dvc>`_ für den Zugriff auf ein
      DVC-Repository als Dateisystem
    * `gcsfs <https://github.com/fsspec/gcsfs>`_ für Google Cloud Storage
    * `gdrive <https://github.com/fsspec/gdrivefs>`_ für den Zugriff auf Google
      Drive und Freigaben
    * `huggingface_hub
      <https://huggingface.co/docs/huggingface_hub/main/en/guides/hf_file_system>`_
      für den Zugriff auf das Hugging Face Hub Dateisystem
    * `lakefs <https://github.com/aai-institute/lakefs-spec>`_ für lakeFS
      Datalakes
    * `ocifs <https://github.com/oracle/ocifs>`_ für den Zugriff auf den Oracle
      Cloud Object Storage
    * `ossfs <https://github.com/fsspec/ossfs>`_ für das Alibaba Cloud (Aliyun)
      Objektspeichersystem (OSS)
    * `p9fs <https://github.com/pbchekin/p9fs-py>`_ für :abbr:`9P (Plan 9
      Filesystem Protocol)`-Server
    * `s3fs <https://github.com/fsspec/s3fs>`__ für Amazon S3 und andere
      kompatible Speicher.
    * `wandbfs <https://github.com/jkulhanek/wandbfs>`_ für den Zugriff auf
      Wandb-Daten
    * `webdav4 <https://github.com/skshetry/webdav4>`_ für WebDAV

.. seealso::
   `Rclone <https://rclone.org>`_ ist ein Befehlszeilenprogramm zur Verwaltung
   von Dateien auf einem Cloud-Speicher. Es unterstützt mehr als 70
   Cloud-Storages. Ein Beispiel für die Verwendung mit Python findet ihr in
   `rclone.py
   <https://github.com/rclone/rclone/blob/master/librclone/python/rclone.py>`_.

Spezialisierte Bibliotheken
---------------------------

`PyArrow <https://arrow.apache.org/docs/python/>`_
    Apache Arrow Python Bindings für das `Hadoop Distributed File System (HDFS)
    <https://arrow.apache.org/docs/python/filesystems.html#hadoop-distributed-file-system-hdfs>`_
    und weitere :ref:`fsspec`-kompatible Dateisysteme.

    .. seealso::
       `Using fsspec-compatible filesystems with Arrow
       <https://arrow.apache.org/docs/python/filesystems.html#filesystem-fsspec>`_

    .. image::
       https://raster.shields.io/github/stars/apache/arrow
    .. image::
       https://raster.shields.io/github/contributors/apache/arrow
    .. image::
       https://raster.shields.io/github/commit-activity/y/apache/arrow
    .. image::
       https://raster.shields.io/github/license/apache/arrow

.. _paramiko:

`paramiko <https://www.paramiko.org>`__
    Python--Implementierung des SSHv2-Protokolls, die sowohl Client- als auch
    Serverfunktionen bietet. Sie bildet die Grundlage für die
    High-Level-SSH-Bibliothek `Fabric <https://www.fabfile.org>`_.

    .. image::
       https://raster.shields.io/github/stars/paramiko/paramiko
    .. image::
       https://raster.shields.io/github/contributors/paramiko/paramiko
    .. image::
       https://raster.shields.io/github/commit-activity/y/paramiko/paramiko
    .. image::
       https://raster.shields.io/github/license/paramiko/paramiko

`boto3 <https://aws.amazon.com/de/sdk-for-python/>`_
    AWS SDK für Python erleichtert die Integration in Amazon S3, Amazon EC2,
    Amazon DynamoDB und andere.

    .. image::
       https://raster.shields.io/github/stars/boto/boto3
    .. image::
       https://raster.shields.io/github/contributors/boto/boto3
    .. image::
       https://raster.shields.io/github/commit-activity/y/boto/boto3
    .. image::
       https://raster.shields.io/github/license/boto/boto3

`azure-storage-blob <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob>`_
    Azure Storage Blobs client library für Python.

    .. image::
       https://raster.shields.io/github/stars/Azure/azure-sdk-for-python
    .. image::
       https://raster.shields.io/github/contributors/Azure/azure-sdk-for-python
    .. image::
       https://raster.shields.io/github/commit-activity/y/Azure/azure-sdk-for-python
    .. image::
       https://raster.shields.io/github/license/Azure/azure-sdk-for-python

`oss2 <https://pypi.org/project/oss2/>`_
    Python SDK für den Alibaba Cloud Object Storage.

    .. image::
       https://raster.shields.io/github/stars/aliyun/aliyun-oss-python-sdk
    .. image::
       https://raster.shields.io/github/contributors/aliyun/aliyun-oss-python-sdk
    .. image::
       https://raster.shields.io/github/commit-activity/y/aliyun/aliyun-oss-python-sdk
    .. image::
       https://raster.shields.io/github/license/aliyun/aliyun-oss-python-sdk

`minio <https://min.io/docs/minio/linux/developers/python/minio-py.html>`_
    MinIO Python Client SDK für Amazon S3 kompatiblen Cloud-Speicher.

    .. image::
       https://raster.shields.io/github/stars/minio/minio-py
    .. image::
       https://raster.shields.io/github/contributors/minio/minio-py
    .. image::
       https://raster.shields.io/github/commit-activity/y/minio/minio-py
    .. image::
       https://raster.shields.io/github/license/minio/minio-py

`PyDrive2 <https://docs.iterative.ai/PyDrive2/>`_
    Python Wrapper-Bibliothek des `google-api-python-client
    <https://github.com/googleapis/google-api-python-client>`_, die viele
    gängige Google Drive API-Aufgaben vereinfacht.

    .. image::
       https://raster.shields.io/github/stars/iterative/PyDrive2
    .. image::
       https://raster.shields.io/github/contributors/iterative/PyDrive2
    .. image::
       https://raster.shields.io/github/commit-activity/y/iterative/PyDrive2
    .. image::
       https://raster.shields.io/github/license/iterative/PyDrive2

`Qcloud COSv5 SDK <https://www.tencentcloud.com/document/product/436/12268>`_
    Python SDK für den Tencent Cloud Object Storage (COS).

    .. image::
       https://raster.shields.io/github/stars/tencentyun/cos-python-sdk-v5
    .. image::
       https://raster.shields.io/github/contributors/tencentyun/cos-python-sdk-v5
    .. image::
       https://raster.shields.io/github/commit-activity/y/tencentyun/cos-python-sdk-v5
    .. image::
       https://raster.shields.io/github/license/tencentyun/cos-python-sdk-v5

`linode_api4 <https://linode-api4.readthedocs.io/en/latest/>`_
    Python bindings für die Linode API v4.

    .. image::
       https://raster.shields.io/github/stars/linode/linode_api4-python
    .. image::
       https://raster.shields.io/github/contributors/linode/linode_api4-python
    .. image::
       https://raster.shields.io/github/commit-activity/y/linode/linode_api4-python
    .. image::
       https://raster.shields.io/github/license/linode/linode_api4-python

`airfs <https://jgoutin.dev/airfs/>`_
    bringt Standard-Python-I/O zu verschiedenen Storages (wie Alibaba Cloud OSS,
    Amazon Web Services S3, GitHub, Microsoft Azure Blobs Storage und Files
    Storage, OpenStack Swift/Object Store.

    .. image::
       https://raster.shields.io/github/stars/JGoutin/airfs
    .. image::
       https://raster.shields.io/github/contributors/JGoutin/airfs
    .. image::
       https://raster.shields.io/github/commit-activity/y/JGoutin/airfs
    .. image::
       https://raster.shields.io/github/license/JGoutin/airfs

`yandex-s3 <https://pypi.org/project/yandex-s3/>`_
    Asyncio-kompatibles SDK für Yandex Object Storage.

    .. image::
       https://raster.shields.io/github/stars/mrslow/yandex-s3
    .. image::
       https://raster.shields.io/github/contributors/mrslow/yandex-s3
    .. image::
       https://raster.shields.io/github/commit-activity/y/mrslow/yandex-s3
    .. image::
       https://raster.shields.io/github/license/mrslow/yandex-s3

Ruhende Projekte
----------------

`PyDrive <https://pypi.org/project/PyDrive/>`_
    Python Wrapper-Bibliothek des `google-api-python-client
    <https://github.com/googleapis/google-api-python-client>`__, die viele
    gängige Google Drive API-Aufgaben vereinfacht.

    .. image::
       https://raster.shields.io/github/stars/googlearchive/PyDrive
    .. image::
       https://raster.shields.io/github/contributors/googlearchive/PyDrive
    .. image::
       https://raster.shields.io/github/commit-activity/y/googlearchive/PyDrive
    .. image::
       https://raster.shields.io/github/license/googlearchive/PyDrive

`digital-ocean-spaces <https://pypi.org/project/digital-ocean-spaces/>`_
    Python-Client für Digital Ocean Spaces mit einer eingebauten Shell.

    .. image::
       https://raster.shields.io/github/stars/ChariotDev/digital-ocean-spaces
    .. image::
       https://raster.shields.io/github/contributors/ChariotDev/digital-ocean-spaces
    .. image::
       https://raster.shields.io/github/commit-activity/y/ChariotDev/digital-ocean-spaces
    .. image::
       https://raster.shields.io/github/license/ChariotDev/digital-ocean-spaces
