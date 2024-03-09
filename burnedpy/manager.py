#
# Copyright (C) 2024 BurnedPy.
#
# BurnedPy is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Index utilities."""

from pathlib import Path
from typing import Any, Dict, Tuple, Union

from burnedpy import db, service
from burnedpy.config import ConfigStorage

try:
    import geopandas as gpd

except ModuleNotFoundError:
    raise ModuleNotFoundError(
        """
    The manager module was designed as a high-level API for the Burned.py. 
    So, some of its dependencies are not included in the package by default. 
    Please install the dependencies, including the flag `api`.
    """
    )


class FirespotsDataManager:
    """Firespots data manager.

    This is a high-level class to manage Firespots from the Queimadas
    Database (INPE-BR). If you want to use the low-level (e.g., index,
    search) and manipulate them to create a service, please check the
    `burnedpy.service` module.
    """

    def __init__(self, config: Union[Dict[str, Any], None] = None):
        """Initializer.

        Args:
            config (Union[Dict[str, Any], None]): Extra configuration for
                                                  the `ConfigStorage`.
        """
        ConfigStorage.update_many(config or {})
        db.db_create_tables()

        self._session = db.db_session_factory()

    def index(self, fire_spot_csv_file: Union[str, Path]) -> Tuple[int, int]:
        """Index fire spot from CSV.

        Args:
            fire_spot_csv_file (Union[str, Path]): Path to the fire spots file.

        Returns:
            Tuple[int, int]: Tuple with (successes, errors).
        """
        return service.index(self._session, fire_spot_csv_file)

    def search(self, bbox: Tuple[int, int, int, int]) -> gpd.GeoDataFrame:
        """Search firespots.

        Args:
            bbox (Tuple[int, int, int, int]): bbox as a tuple (xmin, ymin, xmax, ymax).

        Returns:
            geopandas.GeoDataFrame: DataFrame with the firesposts.
        """
        results = service.search(self._session, bbox)

        return gpd.GeoDataFrame(map(lambda x: x.model_dump(), results))
