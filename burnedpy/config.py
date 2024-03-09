#
# Copyright (C) 2024 BurnedPy.
#
# BurnedPy is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Configuration storage."""

from typing import Any, Dict

from pydash import py_

from burnedpy import constants, fs


#
# Utilities
#
def _get_default_database_location() -> str:
    """Utility to get the default location for the database."""
    database_path = fs.fs_get_user_cache_dir(constants.BURNEDPY_APP_NAME)
    database_path.mkdir(parents=True, exist_ok=True)

    database_path = database_path / "storage.db"

    return f"sqlite:///{database_path}"


#
# Storage
#
class ConfigStorage:
    """Configuration storage class."""

    _configs = {
        "use_spatialite": True,
        "sqlalchemy_database_uri": _get_default_database_location(),
    }
    """Configurations storage attribute."""

    _valid_configs = ["sqlalchemy_database_uri", "use_sqlite"]
    """Valid configurations."""

    @classmethod
    def _is_config_valid(cls, config_name):
        """Check is a given configuration is valid for the storage."""
        if config_name not in cls._configs:
            raise ValueError(f"Invalid configuration: {config_name}")

    @classmethod
    def view(cls):
        """View the current configurations."""
        return py_.map(
            cls._configs.keys(), lambda x: dict(name=x, value=cls._configs.get(x))
        )

    @classmethod
    def update(cls, config_name: str, config_value: Any) -> bool:
        """Update a given configuration.

        Args:
            config_name (str): Configuration name (e.g., database).

            config_value (Any): Value for the configuration `config_name`.

        Returns:
            bool: Flag indicating if the configuration was updated.

        Raises:
            ValueError: When the configuration name is not valid for the storage.
        """
        cls._is_config_valid(config_name)
        cls._configs[config_name] = config_value

        return True

    @classmethod
    def update_many(cls, configurations: Dict[str, Any]) -> bool:
        """Update many configurations at once.

        Args:
            configurations (Dict[str, Any]): Configuration dictionary.

        Returns:
            bool: Flag indicating if the configuration was updated.

        Raises:
            ValueError: When the configuration name is not valid for the storage.
        """
        [cls._is_config_valid(k) for k in configurations.keys()]
        cls._configs.update(configurations)

        return True

    @classmethod
    def get(cls, config_name: str) -> Any:
        """Get a given configuration.

        Args:
            config_name (str): Configuration name (e.g., database).

        Returns:
            Any: Value for the given configuration.

        Raises:
            ValueError: When the configuration name is not valid for the storage.
        """
        cls._is_config_valid(config_name)
        return cls._configs.get(config_name)
