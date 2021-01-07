import django
from django.contrib.gis.geos import Point
from django.contrib.gis.gdal import gdal_version
from django.test import TestCase


class GDALTestase(TestCase):
    @classmethod
    def setUpClass(self):
        print(f"django=={django.__version__}, gdal=={gdal_version().decode()}")

    def test_transform_normal(self):
        x, y = 5.896539, 52.16808
        point = Point(x=x, y=y, srid=4326)
        rd = point.transform(28992, clone=True)

        print(f"WGS84 x={point.x} y={point.y}")
        print(f"RD x={rd.x} y={rd.y}")

        assert int(rd.x) == 189845, f"expected 189845, got {int(rd.x)}"
        assert int(rd.y) == 464558, f"expected 464558, got {int(rd.y)}"

    def test_transform_swapped(self):
        y, x = 5.896539, 52.16808
        point = Point(x=x, y=y, srid=4326)
        rd = point.transform(28992, clone=True)

        print(f"WGS84 x={point.x} y={point.y}")
        print(f"RD x={rd.x} y={rd.y}")

        assert int(rd.x) == 189845, f"expected 189845, got {int(rd.x)}"
        assert int(rd.y) == 464558, f"expected 464558, got {int(rd.y)}"
