#plot = [
#    ("#","#","#","#","#")
#    ("#"," "," "," ","#")
#    ("#"," "," "," ","#")
#    ("#"," "," "," ","#")
#    ("#"," "," "," ","#")
#    ("#","#","#","#","#")
#]
coords = [(2, 3), (-1, 2), (1, -1), (0, 1)]

def render_plot(x):
    plot = []
    innhold = ""
    xs, ys = zip(*coords)
    x_max = max(xs)
    x_min = min(xs)                   
    y_max = max(ys)                  
    y_min = min(ys)

    for i in range(y_max,y_min-1,-1):
        for n in range(x_max,x_min-1,-1):
            if (i,n) in coords:
                innhold += "*"
            else:
                innhold += " "
        plot.append(innhold)
        
    return "\n".join(plot)


print(render_plot(coords))
