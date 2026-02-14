# Project Title
# How to set up the virtual environment
# How to run Python Scripts

# REFLECTION

# Object vs Geometry
- Modeling points as objects changed the way I viewed data from being simple coordinates, to seeing each point as an entity with identity, meaning, and behavior. Instead of treating the data as lon, lat values only, I now see each Point become a self-contained spatial unit that knows how to validate itself, represent its coordinates, interact with other points such as computing the distance, and perform its own spatial math, the Haversine formula in Part B. It no longer relied on an outside script to handle the trigonometry. The data is now structured and has meaning, it is no longer just numerical values stored in a dataset.

# Responsibility
- Point: the point was responsible for the individual identity and coordinate validity. The behaviors related to a single spatial feature such as ensuring that the latitude is between -90 and 90, and the longitude is between -180 and 180, belonged to Point.
- PointSet: all the behaviors related to the collection all belonged to pointset. the pointset was responsible for the collection properties, such as calculating the bounding box, or the bbox of all points or filtering the group by a tag.
- Runner Script: all behavior related to execution, visualization, and file output, all belonged to the runner script. The Runner Script was responsible for execution and output, such as generating the final Matplotlib plot and saving the JSON report.

# Modeling Insight
-By separating geometry from meaning, the spatial logic became reusable across different location types. This organization ensured that the structure was consistent even. Moving the behavior into the classes kept the runner script clean and focused only on visualization and reporting instead of complex spatial computations.

