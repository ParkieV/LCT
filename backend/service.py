from .utils import getScores
from .parsing_2gis import parse_2gis


def get_scores(analog, main_flat):
    corrections = {'bid adjustment': getScores.correct_bid_adjustment(),
                   'floor': getScores.correct_floors(analog, main_flat),
                   'the area of the apartment': getScores.correct_apartment_area(analog, main_flat),
                   'kitchen area': getScores.correct_kitchen_area(analog, main_flat),
                   'the presence of a balcony / loggia': getScores.correct_balcony(analog, main_flat),
                   'distance to the metro': getScores.correct_metro(analog, main_flat),
                   'finishing condition': getScores.correct_condition(analog, main_flat) / analog["correcting"]['square_flat']}
    return corrections


def find_analogs(base_flats):
    all_analogs = parse_2gis(base_flats)
    for num_room_category in all_analogs:
        for analog in all_analogs[num_room_category]:
            corrections = get_scores(analog['content'], base_flats[num_room_category])
            analog['correction'] = corrections | {'final_correction': sum(percent for percent in corrections.values())}
        all_analogs[num_room_category] = sorted(all_analogs[num_room_category],
                                                key=lambda curr_analog:
                                                -curr_analog['correction']['final_correction'])[:10]
    return all_analogs


def calculate_cost(flats, base_flats):
    for flat in flats:
        corrections = get_scores(flat, base_flats[flat['num_rooms']])
        curr_price = base_flats['base_price']
        for correction in corrections:
            curr_price *= correction
        flat['price'] = flat['apartment area'] * curr_price
    return flats


# if __name__ == '__main__':
    # find_analogs()