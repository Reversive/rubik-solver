from data_structure.Color import Color


def elite_selection(palette: list[Color], result_size: int, palette_size: int):
    # follows the formulae n(i) = ceiling(K-i/N) but since K <= N, n(i) is always 1.
    if result_size > palette_size:
        result_size = palette_size
    palette.sort(key=lambda color: color.fitness, reverse=True)
    return palette[0:result_size]
