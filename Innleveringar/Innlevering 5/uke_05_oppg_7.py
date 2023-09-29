def hyd_pres(p, g, z):
    dbar = p * g * z
    pas = dbar * 10**-4
    return pas

print(hyd_pres(1025,10,100))