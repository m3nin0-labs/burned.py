#
# Copyright (C) 2024 BurnedPy.
#
# BurnedPy is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Service operations."""


import shapely
from sqlmodel import func, select

from burnedpy import db, fs, mutator


def index(session, fire_spot_csv_file):
    """Index fire spot from CSV.

    Args:
        session (sqlmodel.orm.session.Session): Database session manager.

        fire_spot_csv_file (Union[str, Path]): Path to the fire spots file.

    Returns:
        Tuple[int, int]: Tuple with (successes, errors).
    """
    success, error, idx = 0, 0, 0

    for fire_spot_row in fs.fs_read_csv(fire_spot_csv_file):
        try:
            fire_spot = mutator.mutate_fire_spot(fire_spot_row)

            session.add(fire_spot)

            if idx % 1000 == 0:
                session.flush()

            success += 1
        except:  # noqa
            error += 1
        idx += 1

    session.commit()
    return (success, error)


def search(session, bbox):
    """Search firespot.

    Args:
        session (sqlmodel.orm.session.Session): Database session manager.

        bbox (Tuple[int, int, int, int]): bbox as a tuple (xmin, ymin, xmax, ymax).

    Returns:
        List[Firespot]: List with the search result.
    """
    bbox_geom = shapely.box(*bbox)
    bbox_geom = func.ST_GeomFromText(str(bbox_geom))

    # building the spatial query
    spatial_query = select(db.Firespot).where(
        func.ST_Intersects(db.Firespot.geom, bbox_geom)
    )

    return session.exec(spatial_query).all()
