from random import uniform
from functools import partial
from statistics import mean, pstdev
from copy import deepcopy

from data_point import DataPoint

def zscores(values):
    avg = mean(values)
    std = pstdev(values)
    if std == 0:
        return [0] * len(values)
    return [(x - avg) / std for x in values]

class KMeans(object):
    """
    K-Means clustering algorithm.
    """
    class Cluster(object):
        def __init__(self, points, centroid):
            self.points = points
            self.centroid = centroid

    def __init__(self, k, data):
        if k < 1:
            raise ValueError("k must be >= 1")
        self._points = data
        self._zscore_normalize()
        # Initialize clusters
        self._clusters = []
        for _ in range(k):
            self._clusters.append(KMeans.Cluster([], self._random_point()))

    @property
    def _centroids(self):
        return [cluster.centroid for cluster in self._clusters]

    def _dimension_slice(self, dimension):
        return [point.dimensions[dimension] for point in self._points]

    def _zscore_normalize(self):
        zscored = [[] for _ in range(len(self._points))]
        for dim in range(self._points[0].num_dimensions):
            dim_slice = self._dimension_slice(dim)
            for i, zscore in enumerate(zscores(dim_slice)):
                zscored[i].append(zscore)
        # Update points
        for i in range(len(self._points)):
            self._points[i].dimensions = zscored[i]

    def _random_point(self):
        rand_dims = []
        for dim in range(self._points[0].num_dimensions):
            dim_slice = self._dimension_slice(dim)  
            rand_val = uniform(min(dim_slice), max(dim_slice))
            rand_dims.append(rand_val)
        return DataPoint(rand_dims)

    def _assign_clusters(self):
        for point in self._points:
            closest = min(
                self._centroids,
                key=partial(DataPoint.distance, point)
            )
            idx = self._centroids.index(closest)
            self._clusters[idx].points.append(point)

    def _generate_cluster_centroids(self):
        for cluster in self._clusters:
            if len(cluster.points) == 0:
                continue
            means = []
            for dim in range(self._points[0].num_dimensions):
                dim_slice = [p.dimensions[dim] for p in cluster.points]
                means.append(mean(dim_slice))
            cluster.centroid = DataPoint(means)

    def run(self, max_iterations=100):
        for iteration in range(max_iterations):
            for cluster in self._clusters:
                cluster.points.clear()
            self._assign_clusters()
            old_centroids = deepcopy(self._centroids)
            self._generate_cluster_centroids()
            # Convergence check
            if old_centroids == self._centroids:
                print("Converged after {} iterations".format(iteration))
                return self._clusters
        return self._clusters

def basic_kmeans_test():
    p1 = DataPoint((2, 1, 1))
    p2 = DataPoint((2, 2, 5))
    p3 = DataPoint((3, 1.5, 2.5))
    test = KMeans(2, (p1, p2, p3))
    test_result = test.run()
    for i, cluster in enumerate(test_result):
        print("Cluster {}: {}".format(i, cluster.points))

if __name__ == "__main__":
    basic_kmeans_test()
