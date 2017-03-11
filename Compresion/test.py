import zipfile
myzip = zipfile.ZipFile('Comprimido.zip', 'w', zipfile.ZIP_DEFLATED)
myzip.write('archivo.txt')
myzip.write('copy.txt')
myzip.writestr("pepe.txt", 'cpapapapa')
myzip.close()