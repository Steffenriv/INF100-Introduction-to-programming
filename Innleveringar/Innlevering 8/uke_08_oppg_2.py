from math import sqrt

def pearson_corr(x,y):

    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    length = len(x)

    dx = []
    dy = []
    zip_dxdy = []
    dx2 = 0
    dy2 = 0

    for i in range(length):
        dx.append(x[i] -  mean_x)
        dy.append(y[i] - mean_y)
        zip_dxdy.append(dx[i]*dy[i])
        dx2 += (x[i]-mean_x)**2
        dy2 += (y[i]-mean_y)**2

    sum_dxdy = sum(zip_dxdy)
    sqr_dx2dy2 = sqrt(dx2*dy2)
    r = sum_dxdy /sqr_dx2dy2
    return r

x1_ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y1_ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y2_ls = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512,1024]

print(pearson_corr(x1_ls, y2_ls))