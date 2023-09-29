def draw_haiku_frame(x, y, z):
    str1 = len(x)
    str2 = len(y)
    str3 = len(z)

    length = max(str1, str2, str3)
    haiku  = ("@"* (length + 4) + "\n")
    haiku += ("@ " + " " * (length-str1) + x + " @\n")
    haiku += ("@ " + " " * (length-str2) + y + " @\n")
    haiku += ("@ " + " " * (length-str3) + z + " @\n")
    haiku += ("@"* (length + 4)+ "")
    return haiku

print(draw_haiku_frame("What a pleasure to", "Right justify a haiku", "As an exercise"))

#Kopierte heile koden fra koden eg hadde i oppgave 6 veke 2 
#og i stedet for print skreiv eg haiku += med \n for å lage nyelinjer og brukte x,y,z i stedet for rad1,2,3