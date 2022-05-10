# se abre el archivo tzop.txt en modo lectura, devolviéndolo como un objeto de archivo
# rt es read and text
stream = open("archivo.txt", "rt", encoding = "utf-8") 

# se imprime el contenido del archivo
print(stream.read()) 