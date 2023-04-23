from flask import url_for


def template_home(numbers):
    limit = 10
    data = []
    sign_names = ["this_signs", "gemini", "leo", "virgo", "libra", "scorpio", "sagittarius",
                  "capricorn", "aquarius", "pisces", "aries", "taurus",  "cancer"]

    for i in range(1, numbers + 1):
        if i < limit:
            data_home = [url_for('static', filename=f'img/zodiac signs/image_part_0{i}.png'), sign_names[i]]
        else:
            data_home = [url_for('static', filename=f'img/zodiac signs/image_part_{i}.png'), sign_names[i]]
        data.append(data_home)

    return data
