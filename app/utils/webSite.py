from datetime import date

def movieDatetime(date_obj: date) -> list:
    "повертає з 1994-10-10 такого масив з [10, 'Жовтня', 1994]"
    months_ua = {
        1: "Cічня", 2: "Лютого", 3: "Березня", 4: "Квітня",
        5: "Травня", 6: "Червня", 7: "Липня", 8: "Серпня",
        9: "Вересня", 10: "Жовтня", 11: "Листопада", 12: "Грудня"
    }
    return [date_obj.day, months_ua[date_obj.month], date_obj.year]

def movieRuntime(runtime: int) -> str:
    "перетворює хвилини у нормалтний формат 121 -> 2 год 1 хв"
    hours = runtime // 60
    mins = runtime % 60
    return f"{hours} год {mins} хв"

def movieStars(rating: int) -> list:
    """
    приймає ціле чисто від 1 до 10
    і повертає скльки зірок має бути від половини до 5 цілих
    [full_stars, has_halfStar]
    [int, bool]
    """
    full_stars = rating // 2
    has_halfStar = rating % 2 == 1
    return [full_stars, has_halfStar]