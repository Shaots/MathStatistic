from Lab8.Code.distribution8 import *


def main():
    signal = read_signal("wave_ampl.txt")
    draw_signal(signal)
    draw_hist(signal)
    start, finish, types = get_areas(signal)
    zones, zones_types, signal_data = get_zones(signal, start, finish, types)
    res.write(str(zones) + "\n")
    draw_areas(signal_data, zones, zones_types)
    get_params(signal, zones)
