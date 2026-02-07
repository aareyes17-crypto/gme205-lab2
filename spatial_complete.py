# src/spatial.py
"""
Lab 2: Simple Spatial Objects in Python (Classic Style)

This module defines spatial objects using explicit object-oriented design.
Focus: identity, validation, and spatial behavior.
"""

import math, csv
from typing import Any, Dict, Optional


class Point:
    """
    A simple spatial point with identity and meaning.

    Required:
      - id: unique identifier (string)
      - lon: longitude in decimal degrees (float)
      - lat: latitude in decimal degrees (float)

    Optional:
      - name: human-readable label
      - tag: category (e.g., "poi", "sensor", "gate", "landmark")
    """

    def __init__(
        self,
        id: str,
        lon: float,
        lat: float,
        name: Optional[str] = None,
        tag: Optional[str] = None,
    ) -> None:
        """
        Initialize a Point object and enforce spatial validity.

        Validation is performed here to ensure that
        invalid spatial objects cannot exist.
        """

        # --- Validation ---
        if not isinstance(id, str):
            raise TypeError("Point id must be a string")

        if not (-180.0 <= lon <= 180.0):
            raise ValueError(f"Invalid longitude {lon}. Must be between -180 and 180.")

        if not (-90.0 <= lat <= 90.0):
            raise ValueError(f"Invalid latitude {lat}. Must be between -90 and 90.")

        # --- State assignment ---
        self.id = id
        self.lon = float(lon)
        self.lat = float(lat)
        self.name = name
        self.tag = tag

    # ------------------------------------------------------------------
    # Instance methods (behavior belongs to the object)
    # ------------------------------------------------------------------
    def to_tuple(self) -> tuple[float, float]:
        """
        Return the coordinate as a (lon, lat) tuple.
        """
        return (self.lon, self.lat)

    def distance_to(self, other: "Point") -> float:
        """
        Compute the great-circle distance to another Point in meters.

        This represents spatial interaction between two objects.
        """
        if not isinstance(other, Point):
            raise TypeError("distance_to expects another Point object")

        return Point.euclidean(self.lon, self.lat, other.lon, other.lat)

    # ------------------------------------------------------------------
    # Static method (pure spatial math)
    # ------------------------------------------------------------------
    @staticmethod
    def haversine_m(
        lon1: float, lat1: float, lon2: float, lat2: float
    ) -> float:
        """
        Compute the Haversine distance between two lon/lat pairs in meters.

        Static method because it does not depend on object state.
        """
        R = 6_371_000.0  # Earth radius in meters

        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)

        a = (
            math.sin(dphi / 2) ** 2
            + math.cos(phi1)
            * math.cos(phi2)
            * math.sin(dlambda / 2) ** 2
        )
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c

    @staticmethod
    def euclidean(x1, y1, x2, y2):
        """
        Compute Pythagorean (Euclidean) distance
        between two coordinate pairs.
        """
        dx = x2 - x1
        dy = y2 - y1
        return math.sqrt(dx * dx + dy * dy)

    # ------------------------------------------------------------------
    # Class method (constructing objects from data)
    # ------------------------------------------------------------------
    @classmethod
    def from_row(cls, row: Dict[str, Any]) -> "Point":
        """
        Create a Point object from a dictionary-like row
        (e.g., csv.DictReader or pandas row.to_dict()).
        """
        pid = str(row["id"])
        lon = float(row["lon"])
        lat = float(row["lat"])
        name = row.get("name")
        tag = row.get("tag")

        # Normalize empty strings
        name = name if name not in ("", None) else None
        tag = tag if tag not in ("", None) else None

        return cls(pid, lon, lat, name=name, tag=tag)

    # ------------------------------------------------------------------
    # Semantic convenience methods
    # ------------------------------------------------------------------
    def is_poi(self) -> bool:
        """
        Return True if this point represents a Point of Interest.
        """
        return (self.tag or "").strip().lower() == "poi"

    def __repr__(self) -> str:
        """
        Developer-friendly string representation.
        """
        return (
            f"Point(id={self.id!r}, lon={self.lon}, lat={self.lat}, "
            f"name={self.name!r}, tag={self.tag!r})"
        )
    

class PointSet:
    def __init__(self, points):
        self.points = points

    @classmethod
    def from_csv(cls, path):
        points = []
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    points.append(Point.from_row(row))
                except ValueError:
                    continue
        return cls(points)

    def count(self):
        return len(self.points)

    def bbox(self):
        lons = [p.lon for p in self.points]
        lats = [p.lat for p in self.points]
        return min(lons), min(lats), max(lons), max(lats)

    def filter_by_tag(self, tag):
        return PointSet([p for p in self.points if p.tag == tag])