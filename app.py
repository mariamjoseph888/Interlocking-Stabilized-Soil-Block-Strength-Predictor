def block_strength_lime(c, l):
    return 2.283 * (c - (3 * l / 761)) - 9.995

def wall_strength_lime(fcb1):
    return 2.64 * fcb1 + 0.08

if __name__ == "__main__":
    cement = 6   # Cement content in %
    lime = 3     # Lime content in %

    fcb1 = block_strength_lime(cement, lime)
    fcw2 = wall_strength_lime(fcb1)

    print("Block Strength (PC + Lime):", round(fcb1, 3), "MPa")
    print("Wall Strength (LSW2):", round(fcw2, 3), "MPa")
    