El objetivo del juego es reorganizar las piezas desde un estado inicial desordenado hasta un estado objetivo 
en el que las piezas estén ordenadas de manera secuencial.

Estos son algunos de los métodos comunes que se pueden aplicar en el 8-Puzzle:

    BFS (Búsqueda en amplitud): Busca la solución explorando primero los movimientos más cercanos al estado inicial, garantizando encontrar la solución más corta, aunque puede ser ineficiente en términos de memoria.

    DFS (Búsqueda en profundidad): Explora completamente cada posible movimiento hacia abajo, antes de retroceder, lo que puede llevar a encontrar soluciones rápidamente, pero también puede ser ineficiente o incluso no encontrar la solución en algunos casos.

    *A (A estrella)**: Es una de las mejores opciones, ya que utiliza una heurística para estimar qué tan cerca está el estado actual de la solución, lo que le permite encontrar la solución de manera más eficiente que BFS o DFS.

    Greedy: Similar a A*, pero solo usa la heurística para decidir el siguiente movimiento, sin tener en cuenta el costo real desde el inicio.
El jugador puede seleccionar uno de los algoritmos de búsqueda (BFS, DFS, A*, Greedy) para que la aplicación resuelva el rompecabezas automáticamente, animando los pasos de la solución y mostrando cómo se reorganizan las piezas.
