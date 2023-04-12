import json

with open('backend/config.json') as file:
    main_config = json.load(file)


def correct_bid_adjustment():
    return main_config['bid adjustment']


def correct_floors(analog, main_flat):
    correction = 0
    config = main_config['apartament floor']
    if main_flat['floor'] == 1:
        if analog['correcting']['floor'] == 1:
            correction = config['first floor']['ff']
        elif analog['correcting']['floor'] == analog['required']['building_num_floors']:
            correction = config['first floor']['lf']
        else:
            correction = config['first floor']['mf']
    elif main_flat['floor'] == main_flat['building_num_floor']:
        if analog['correcting']['floor'] == 1:
            correction = config['last floor']['ff']
        elif analog['correcting']['floor'] == analog['required']['building_num_floors']:
            correction = config['last floor']['lf']
        else:
            correction = config['last floor']['mf']
    else:
        if analog['correcting']['floor'] == 1:
            correction = config['middle floor']['ff']
        elif analog['correcting']['floor'] == analog['required']['building_num_floors']:
            correction = config['middle floor']['lf']
        else:
            correction = config['middle floor']['mf']
    return correction


def correct_apartment_area(analog, main_flat):
    correction = 0
    config = main_config['apartment area']
    if main_flat['square_flat'] < 30:
        if analog['correcting']['square_flat'] < 30:
            correction = config['<30']['<30']
        elif analog['correcting']['square_flat'] < 50:
            correction = config['<30']['30-50']
        elif analog['correcting']['square_flat'] < 65:
            correction = config['<30']['50-65']
        elif analog['correcting']['square_flat'] < 90:
            correction = config['<30']['65-90']
        elif analog['correcting']['square_flat'] < 120:
            correction = config['<30']['90-120']
        else:
            correction = config['<30']['>120']
    elif main_flat['square_flat'] < 50:
        if analog['correcting']['floor'] == 1:
            correction = config['last floor']['ff']
        elif analog['correcting']['floor'] == analog['required']['building_num_floors']:
            correction = config['last floor']['lf']
        else:
            correction = config['last floor']['mf']
    elif main_flat['square_flat'] < 65:
        if analog['correcting']['floor'] == 1:
            correction = config['last floor']['ff']
        elif analog['correcting']['floor'] == analog['required']['building_num_floors']:
            correction = config['last floor']['lf']
        else:
            correction = config['last floor']['mf']
    elif main_flat['square_flat'] < 90:
        if analog['correcting']['floor'] == 1:
            correction = config['last floor']['ff']
        elif analog['correcting']['floor'] == analog['required']['building_num_floors']:
            correction = config['last floor']['lf']
        else:
            correction = config['last floor']['mf']
    elif main_flat['square_flat'] < 120:
        if analog['correcting']['floor'] == 1:
            correction = config['last floor']['ff']
        elif analog['correcting']['floor'] == analog['required']['building_num_floors']:
            correction = config['last floor']['lf']
        else:
            correction = config['last floor']['mf']
    else:
        if analog['correcting']['floor'] == 1:
            correction = config['middle floor']['ff']
        elif analog['correcting']['floor'] == analog['required']['building_num_floors']:
            correction = config['middle floor']['lf']
        else:
            correction = config['middle floor']['mf']
    return correction


def correct_kitchen_area(analog, main_flat):
    correction = 0
    config = main_config['kitchen area']
    if main_flat['floor'] == 1:
        if analog['correcting']['floor'] == 1:
            correction = config['first floor']['ff']
        elif analog['correcting']['floor'] == analog['required']['building_num_floors']:
            correction = config['first floor']['lf']
        else:
            correction = config['first floor']['mf']
    elif main_flat['floor'] == main_flat['building_num_floor']:
        if analog['correcting']['floor'] == 1:
            correction = config['last floor']['ff']
        elif analog['correcting']['floor'] == analog['required']['building_num_floors']:
            correction = config['last floor']['lf']
        else:
            correction = config['last floor']['mf']
    else:
        if analog['correcting']['floor'] == 1:
            correction = config['middle floor']['ff']
        elif analog['correcting']['floor'] == analog['required']['building_num_floors']:
            correction = config['middle floor']['lf']
        else:
            correction = config['middle floor']['mf']
    return correction


def correct_balcony(analog, main_flat):
    correction = 0
    config = main_config['balcony / loggia']
    if main_flat['floor'] == 1:
        if analog['correcting']['floor'] == 1:
            correction = config['first floor']['ff']
        elif analog['correcting']['floor'] == analog['required']['building_num_floors']:
            correction = config['first floor']['lf']
        else:
            correction = config['first floor']['mf']
    elif main_flat['floor'] == main_flat['building_num_floor']:
        if analog['correcting']['floor'] == 1:
            correction = config['last floor']['ff']
        elif analog['correcting']['floor'] == analog['required']['building_num_floors']:
            correction = config['last floor']['lf']
        else:
            correction = config['last floor']['mf']
    else:
        if analog['correcting']['floor'] == 1:
            correction = config['middle floor']['ff']
        elif analog['correcting']['floor'] == analog['required']['building_num_floors']:
            correction = config['middle floor']['lf']
        else:
            correction = config['middle floor']['mf']
    return correction


def correct_metro(analog, main_flat):
    correction = 0
    config = main_config['metro']
    if main_flat['floor'] == 1:
        if analog['correcting']['floor'] == 1:
            correction = config['first floor']['ff']
        elif analog['correcting']['floor'] == analog['required']['building_num_floors']:
            correction = config['first floor']['lf']
        else:
            correction = config['first floor']['mf']
    elif main_flat['floor'] == main_flat['building_num_floor']:
        if analog['correcting']['floor'] == 1:
            correction = config['last floor']['ff']
        elif analog['correcting']['floor'] == analog['required']['building_num_floors']:
            correction = config['last floor']['lf']
        else:
            correction = config['last floor']['mf']
    else:
        if analog['correcting']['floor'] == 1:
            correction = config['middle floor']['ff']
        elif analog['correcting']['floor'] == analog['required']['building_num_floors']:
            correction = config['middle floor']['lf']
        else:
            correction = config['middle floor']['mf']
    return correction


def correct_condition(analog, main_flat):
    correction = 0
    config = main_config['finishing condition']
    if main_flat['floor'] == 1:
        if analog['correcting']['floor'] == 1:
            correction = config['first floor']['ff']
        elif analog['correcting']['floor'] == analog['required']['building_num_floors']:
            correction = config['first floor']['lf']
        else:
            correction = config['first floor']['mf']
    elif main_flat['floor'] == main_flat['building_num_floor']:
        if analog['correcting']['floor'] == 1:
            correction = config['last floor']['ff']
        elif analog['correcting']['floor'] == analog['required']['building_num_floors']:
            correction = config['last floor']['lf']
        else:
            correction = config['last floor']['mf']
    else:
        if analog['correcting']['floor'] == 1:
            correction = config['middle floor']['ff']
        elif analog['correcting']['floor'] == analog['required']['building_num_floors']:
            correction = config['middle floor']['lf']
        else:
            correction = config['middle floor']['mf']
    return correction

