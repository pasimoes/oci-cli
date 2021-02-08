# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.database_management import DbManagementClient

MODULE_TO_TYPE_MAPPINGS["database_management"] = oci.database_management.models.database_management_type_mapping
if CLIENT_MAP.get("database_management") is None:
    CLIENT_MAP["database_management"] = {}
CLIENT_MAP["database_management"]["db_management"] = DbManagementClient
