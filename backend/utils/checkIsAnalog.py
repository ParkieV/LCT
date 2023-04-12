def check_is_analog(analog, main_flat):
    return all((analog[param] == main_flat[param]) or (param == 'address') for param in analog)

