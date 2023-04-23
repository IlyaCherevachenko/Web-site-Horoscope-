def get_name_zodiac(sign):
    zodiac_signs = {
        "gemini": 'Близнецов', "leo": 'Львов', "virgo": 'Дев',
        "libra": 'Весов,', "scorpio": 'Скорпионов', "sagittarius": 'Стрельцов',
        "capricorn": 'Козерогов', "aquarius": 'Водолеев', "pisces": 'Рыб',
        "aries": 'Овнов', "taurus": 'Тельцов', "cancer": 'Раков'
    }

    result = zodiac_signs[sign]

    return result
