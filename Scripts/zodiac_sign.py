sign_dates = (
    ((21, 3), (20, 4)),
    ((21, 4), (21, 5)),
    ((22, 5), (21, 6)),
    ((22, 6), (22, 7)),
    ((23, 7), (21, 8)),
    ((22, 8), (23, 9)),
    ((24, 9), (23, 10)),
    ((24, 10), (22, 11)),
    ((23, 11), (22, 12)),
    ((23, 12), (20, 1)),
    ((21, 1), (19, 2)),
    ((20, 2), (20, 3)),
)

sign_names = {
    '0': "aries",
    '1': "taurus",
    '2': "gemini",
    '3': "cancer",
    '4': "leo",
    '5': "virgo",
    '6': "libra",
    '7': "scorpio",
    '8': "sagittarius",
    '9': "capricorn",
    '10': "aquarius",
    '11': "pisces"
}


def get_sign_from_form(birthday):
    data = birthday.split('-')
    day, month = int(data[2]), int(data[1])
    for index, sign in enumerate(sign_dates):
        if (month == sign[0][1] and day >= sign[0][0]) or (month == sign[1][1] and day <= sign[1][0]):
            return sign_names[f'{index}']
