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
    data = map(int, birthday.split('-'))
    year, month, day = data

    for index, sign in enumerate(sign_dates):
        month_limit_first, day_limit_first = sign[0][1], sign[0][0]
        month_limit_second, day_limit_second = sign[1][1], sign[1][0]

        if (month == month_limit_first and day >= day_limit_first) \
                or (month == month_limit_second and day <= day_limit_second):

            return sign_names[f'{index}']
