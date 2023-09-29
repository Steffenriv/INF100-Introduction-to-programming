def swap_tuple(y):
    x = list(y)
    x[2] = "salmon"
    y = tuple(x)
    return y

print(swap_tuple(("Princess Sparkle", "aloof", "tuna")))    