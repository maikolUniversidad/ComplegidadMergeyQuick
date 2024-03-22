# ComplegidadMergeyQuick

Graficos Resultados 3000 Registros:
![image](https://github.com/maikolUniversidad/ComplegidadMergeyQuick/assets/112012566/c5c68ac9-b7af-4d24-a342-fa10fb47583b)



Los coeficientes polinómicos que has proporcionado son el resultado de ajustar un polinomio a los datos recogidos de los pasos totales para los algoritmos Merge Sort y Quick Sort sobre listas aleatorias de diferentes tamaños, en este caso hasta un tamaño máximo de 3000.

Para Merge Sort (Aleatoria), los coeficientes son:
- \( -5.16020115 \times 10^2 \)
- \( 1.09757690 \times 10^1 \)
- \( 6.29129194 \times 10^{-4} \)

Para Quick Sort (Aleatoria), los coeficientes son:
- \( -6.99379177 \times 10^2 \)
- \( 1.08040496 \times 10^1 \)
- \( 9.23336300 \times 10^{-4} \)

Estos coeficientes corresponden a un polinomio de segundo grado, que generalmente tiene la forma \( ax^2 + bx + c \), donde 'a' es el coeficiente principal, 'b' es el coeficiente lineal, y 'c' es el término constante.

La interpretación de estos coeficientes es la siguiente:

- El coeficiente principal (el de \( x^2 \)) representa la parte de la complejidad que escala con el cuadrado del tamaño de la entrada. Para algoritmos como Merge Sort, que tiene una complejidad temporal de \( O(n\log{n}) \), esperaríamos que este coeficiente fuera cercano a 0, lo que se aproxima al resultado obtenido. Para Quick Sort, en el caso promedio también tendríamos un coeficiente pequeño porque su complejidad esperada es \( O(n\log{n}) \), pero debido a la elección de pivotes no óptimos en listas aleatorias, este valor puede variar.
  
- El coeficiente lineal (el de \( x \)) indica cómo escala la complejidad en relación lineal con el tamaño de la entrada. En ambos casos, vemos que hay un incremento lineal que contribuye significativamente a la complejidad total.

- El término constante (el valor sin \( x \)) a menudo puede ser ignorado para propósitos de complejidad algorítmica a gran escala, ya que representa un costo fijo que no cambia con el tamaño de la entrada. Sin embargo, los valores negativos pueden ser el resultado del ajuste y no tienen un significado físico directo en este contexto.

Al analizar estos coeficientes en el marco de la complejidad algorítmica, podemos concluir que ambos algoritmos tienen un comportamiento que se acerca a una complejidad \( O(n\log{n}) \), como se espera teóricamente, aunque con algunas variaciones debido a la naturaleza aleatoria de las listas y la influencia de los casos particulares que afectan a Quick Sort.

Cuando miramos los gráficos proporcionados, podemos ver que los tiempos de ejecución y los pasos totales aumentan con el tamaño de la lista. El gráfico de tiempos de ejecución para Quick Sort muestra más variabilidad, lo que podría ser un indicativo de que el peor caso tiene más peso en algunas instancias, mientras que Merge Sort muestra un aumento más suave y predecible en tiempo, lo cual es coherente con su complejidad temporal constante de \( O(n\log{n}) \).
