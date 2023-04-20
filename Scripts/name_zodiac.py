def get_name_zodiac(sign):
    ZODIAC_SIGNS = {
        "gemini": 'близнецов', "leo": 'львов', "virgo": 'дев',
        "libra": 'весов,', "scorpio": 'скорпионов', "sagittarius": 'стрельцов',
        "capricorn": 'козерогов', "aquarius": 'водолеев', "pisces": 'рыб',
        "aries": 'овнов', "taurus": 'тельцов', "cancer": 'раков'
    }

    return ZODIAC_SIGNS[sign]
