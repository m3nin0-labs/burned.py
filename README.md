# Burned.py 🔥

The `burned.py` library is a powerful tool designed to index and search data from the Brazilian fire identification program conducted by the National Institute for Space Research (INPE) - Programa de Queimadas do INPE. This library is an essential resource for researchers, developers, and analysts working with environmental data related to fire events in Brazil.

> Note: This is a hobby project.

## Structure

The library is divided into two main components:

**1. Core**

The core of `burned.py` provides the fundamental functionalities of indexing and searching for fire data. Built on top of technologies like Spatialite and SQLModel, the core is versatile enough to support the development of RESTful APIs, CLI applications, and more.

**2. High-level API**

The high-level API abstracts the complexities of the core functionalities using GeoPandas, enabling users to easily index and search for fire data without needing to interact directly with the underlying components.

## Installation

You can install `burned.py` using:

```
pip install git+https://github.com/m3nin0-labs/burned.py
```

## Usage

To use the High-level API, two steps are required:

**Indexing Data**

Indexing is the process of organizing data in a way that makes it easier to retrieve. In the context of `burned.py`, indexing involves reading and storing data from CSV files into Spatialite, allowing for efficient searching. To index data, users can utilize the following example code:

```python
from burnedpy.manager import FirespotsDataManager

# Create the data manager
manager = FirespotsDataManager()

# Index the data
status = manager.index("/path/to/focos_ams_ref_XXXX.csv")
print(status)  # Outputs: (success, error)
```

**Searching Data**

Once data is indexed, it can be searched using coordinates:

```python
from burnedpy.manager import FirespotsDataManager

# Create the data manager (data must be already indexed)
manager = FirespotsDataManager()

# Perform a search within a geographical bounding box
results = manager.search((-26.470573, -54.536133, -21.902278, -48.471680))
results.head(5)
```

## Contributing

We welcome contributions! If you have suggestions for improvements or bug fixes, please feel free to fork the repository and submit a pull request.

## License

`burned.py` is distributed under the MIT license. See `LICENSE` for more details.
