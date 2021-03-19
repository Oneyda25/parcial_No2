

texto = """ De Los Errores Aprendemos Siempre vamos a cometer errores. Debemos asimilarlos
porque somos seres humanos, no somos productos artificiales programados donde no debamos cometerlos. 
A pesar de que no son nuestras intenciones incurrir estas faltas, el punto fundamental es aprender de ellas, es decir, que los errores
forman parte de nuestros procesos de aprendizajes. Aprendemos las consecuencias de ellos para luego no volver a cometerlos, y nos llevan
a un escenario para poder repensar en un aspecto que es de suma importancia: no somos seres que nacimos programados, no somos 
seres artificiales, no somos seres perfectos donde los resultados de nuestras prácticas siempre serán “maravillosos” 
como los planificamos, somos seres humanos.
"""

ignorar = ",;:''.\n!\"'"
for caracter in ignorar:
    texto = texto.replace(caracter,
                          "")  
texto = texto.lower()

palabras = texto.split(" ")

diccionario_frecuencias = {}
for palabra in palabras:
    if palabra in diccionario_frecuencias:
        diccionario_frecuencias[palabra] += 1
    else:
        diccionario_frecuencias[palabra] = 1

for palabra in diccionario_frecuencias:
    frecuencia = diccionario_frecuencias[palabra]
    print(f" '{palabra}' {frecuencia}")

