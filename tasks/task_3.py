class PointsForPlace:
    @staticmethod
    def get_points_for_place(place):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
            points = 0
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            points = 0
        else:
            points = 101 - place
        return points


class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            points = 0
        else:
            points = meters * 0.5
        return points


class TotalPoints(PointsForPlace, PointsForMeters):
    @staticmethod
    def get_total_points(place, meters):
        total = PointsForPlace.get_points_for_place(place) + PointsForMeters.get_points_for_meters(meters)
        return total


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))
