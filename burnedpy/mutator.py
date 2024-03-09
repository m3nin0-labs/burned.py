#
# Copyright (C) 2024 BurnedPy.
#
# BurnedPy is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Mutator functions."""

from datetime import datetime
from typing import Dict, Union

from burnedpy.db import Firespot


#
# Utilities
#
def _strip(value: Union[str, None]) -> str:
    """Strip value."""
    return value.strip() if value else None


#
# High-level operations.
#
def mutate_fire_spot(firespot: Dict) -> Firespot:
    """Mutate fire spot dictionary into FireSpot object.

    Args:
        firespot (Dict): Firespot dictionary.

    Returns:
        FireSpot: Fireobject object.
    """
    # ID and UUID
    spot_id = firespot["id_bdq"]
    spot_uuid = firespot["foco_id"]

    # Location
    lat = firespot["lat"].strip()
    lon = firespot["lon"].strip()

    spot_location = f"POINT ({lat} {lon})"

    # Date
    spot_date = datetime.strptime(firespot["data_pas"], "%Y-%m-%d %H:%M:%S")

    # Country
    spot_country = firespot["pais"]

    # State
    spot_state = firespot["estado"]

    # City
    spot_city = firespot["municipio"]

    # Biom
    spot_biom = firespot["bioma"]

    return Firespot(
        id=_strip(spot_id),
        uuid=_strip(spot_uuid),
        country=_strip(spot_country),
        city=_strip(spot_city),
        state=_strip(spot_state),
        biom=_strip(spot_biom),
        date=spot_date,
        geom=spot_location,
    )
