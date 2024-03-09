#
# Copyright (C) 2024 BurnedPy.
#
# BurnedPy is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

from datetime import datetime
from typing import Any
from uuid import UUID, uuid4

from geoalchemy2 import Geometry, load_spatialite
from sqlalchemy import Engine
from sqlalchemy.event import listen
from sqlmodel import Column, Field, Session, SQLModel, create_engine

from burnedpy.config import ConfigStorage


#
# Models
#
class Firespot(SQLModel, table=True):
    """Firespot table class."""

    id: str = Field(default=None, primary_key=True)
    """Queimadas DB: Database ID (`id_bdq`)"""

    uuid: UUID = Field(default_factory=uuid4, nullable=False, index=True)
    """Queimadas DB: Spot ID (`foco_id`)"""

    date: datetime = Field(default=None, nullable=False, index=True)
    """Queimadas DB: Spot Date (`data_pas`)"""

    country: str = Field(default=None, nullable=False, index=True)
    """Queimadas DB: Country where fire spot was identified (`pais`)"""

    state: str = Field(default=None, nullable=True, index=True)
    """Queimadas DB: State where fire spot was identified (`estado`)"""

    city: str = Field(default=None, nullable=True, index=True)
    """Queimadas DB: State where fire spot was identified (`municipio`)"""

    biom: str = Field(default=None, nullable=True, index=True)
    """Queimadas DB: Biome where fire spot was identified (`bioma`)"""

    geom: Any = Field(sa_column=Column(Geometry("POINT")))
    """Queimadas DB: Fire Spot location (`lat`, and `lon`)"""


#
# Utilities
#
def db_engine_factory() -> Engine:
    """Create a database connection engine."""
    db_uri = ConfigStorage.get("sqlalchemy_database_uri")
    db_use_spatialite = ConfigStorage.get("use_spatialite")

    engine = create_engine(db_uri, echo=False)

    if db_use_spatialite:
        listen(engine, "connect", load_spatialite)

    return engine


def db_session_factory() -> Session:
    """Create session using `sqlachemy.orm.sessionmaker`."""
    engine = db_engine_factory()
    return Session(bind=engine)


def db_create_tables() -> None:
    """Create tables in the database."""
    db_engine = db_engine_factory()
    SQLModel.metadata.create_all(bind=db_engine, checkfirst=True)
