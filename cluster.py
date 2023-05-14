from point import makePointList, Point
import numpy as np

class Cluster:
    """A class representing a cluster of points.
    Attributes:
      center: A Point object representing the exact center of the cluster.
      points: A set of Point objects that constitute our cluster.
    """

    def __init__(self, center=Point([0, 0])):
        """Inits a Cluster with a specific center (defaults to [0,0])."""
        self.center = center
        self.points = set()

    @property
    def coords(self):
        return self.center.coords

    @property
    def dim(self):
        return self.center.dim

    def addPoint(self, p):
        self.points.add(p)

    def removePoint(self, p):
        self.points.remove(p)

    @property
    def avgDistance(self):
        """Calculates the average distance of points in the cluster to the center.
        Returns:
          A float representing the average distance from all points in self.points
          to self.center.
        """

    

        if len(self.points) == 0:
            return 0
        distances = [self.center.distFrom(p) for p in self.points]
        return sum(distances) / len(self.points)

    def updateCenter(self):
        """Updates self.center to be the average of all points in the cluster.
        If no points are in the cluster, then self.center should be unchanged
        
        """
        # fill in
        # Hint: make sure self.center is a Point object after this function runs.


    
        if self.points:
            updated_coords = [sum(dim) / len(self.points) for dim in zip(*self.points)]
            self.center = Point(updated_coords)
        else:
            return
        

    def printAllPoints(self):
        print(str(self))
        for p in self.points:
            print("   {}".format(p))

    def __str__(self):
        return "Cluster: {} points and center = {}".format(
            len(self.points), self.center
        )

    def __repr__(self):
        return self.__str__()


def createClusters(data):
    """Creates clusters with centers from a k-by-d numpy array.
    Args:
      data: A k-by-d numpy array representing k d-dimensional points.
    Returns:
      A list of Clusters with each cluster centered at a d-dimensional
      point from each row of data.
    """
    centers = makePointList(data)
    return [Cluster(c) for c in centers]


if __name__ == "__main__":

    p1 = Point([1.5, 2.5])
    p2 = Point([2.0, 3.0])
    c = Cluster(Point([0.5, 3.5]))
    print(c)

    c.addPoint(p1)
    c.addPoint(p2)
    print(c)
    print(c.avgDistance)
    c.updateCenter()
    print(c)
    print(c.avgDistance)
    assert isinstance(
        c.center, Point
    ), "After updateCenter, the center must remain a Point object."