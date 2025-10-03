from subprocess import call

def mod_port(puerto, productpage):
    # Modificar el puerto
    call(["mv","-f", productpage + "productpage_monolith.py", productpage + "productpage_monolith.txt"])
    fin = open(productpage + "productpage_monolith.txt", 'r')
    fout = open("copia.txt", 'w')
    for line in fin:
        if '.format(detailsHostname, servicesDomain)' in line:
            fout.write('    "name": "http://{0}{1}:' + puerto + '".format(detailsHostname, servicesDomain),\n')
        elif '.format(ratingsHostname, servicesDomain)' in line:
            fout.write('    "name": "http://{0}{1}:' + puerto + '".format(ratingsHostname, servicesDomain),\n')
        elif '.format(reviewsHostname, servicesDomain)' in line:
            fout.write('    "name": "http://{0}{1}:' + puerto + '".format(reviewsHostname, servicesDomain),\n')
        else:
            fout.write(line)  
    fin.close()
    fout.close()
    call(["rm", "-f", productpage + "productpage_monolith.txt"])
    call(["mv", "-f", "copia.txt", productpage + "productpage_monolith.py"])

def arranque(puerto, productpage):
    # Se arranca la aplicacion.
    call(["python3", productpage + "productpage_monolith.py", puerto])