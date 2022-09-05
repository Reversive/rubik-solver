from data_structure.Member import Member


def elite_selection(palette: list[Member], result_size: int) -> list[Member]:
    # follows the formulae n(i) = ceiling(K-i/N) but since K <= N, n(i) is always 1.
    palette_size = len(palette)
    if result_size > palette_size:
        result_size = palette_size
    palette.sort(key=lambda color: color.fitness, reverse=True)
    return palette[0:result_size]
