with open("logo.png",'br') as f:
        x=f.read(4096)
        with open("logo_copy",'bw') as f2:
            f2.write(x)
