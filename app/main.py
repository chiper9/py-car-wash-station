class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0.0  # Доход от мойки автомобилей
        for car in cars:
            if car.clean_mark < self.clean_power:
                # Рассчитываем стоимость мойки для этого автомобиля
                cost = self.calculate_washing_price(car)
                income += cost
                # Моем автомобиль
                self.wash_single_car(car)
        return round(income, 1)  # Округляем доход до 1 знака после запятой

    def calculate_washing_price(self, car: dict) -> float:
        # Рассчитываем стоимость мойки для одного автомобиля
        difference = self.clean_power - car.clean_mark
        cost = (car.comfort_class * difference * self.average_rating
                / self.distance_from_city_center)
        return round(cost, 1)  # Округляем стоимость до 1 знака после запятой

    def wash_single_car(self, car: dict) -> None:
        # Моем автомобиль, если его уровень чистоты меньше, чем у станции
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        # Обновляем средний рейтинг и количество оценок
        total_ratings = self.average_rating * self.count_of_ratings
        total_ratings += rating
        self.count_of_ratings += 1
        self.average_rating = round(total_ratings / self.count_of_ratings, 1)
