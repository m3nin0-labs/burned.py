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
manager = FirespotsDataManager()  # data must be already indexed

#
# 2. Searching the data
#
results = manager.search((-26.470573, -54.536133, -21.902278, -48.471680))
results.head(5)
