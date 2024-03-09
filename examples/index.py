#
# Copyright (C) 2024 BurnedPy.
#
# BurnedPy is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Index Queimadas data with Burned.py"""

from burnedpy.manager import FirespotsDataManager

#
# 1. Creating the data manager
#
manager = FirespotsDataManager()

#
# 2. Indexing the data
#
status = manager.index("/path/to/focos_ams_ref_XXXX.csv")
print(status)  # (success, error)
