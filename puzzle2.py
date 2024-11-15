import tkinter as tk
from tkinter import messagebox
from puzzle2 import Puzzle
from metodos2 import bfs, dfs, astar, greedy

class PuzzleApp:
    def __init__(self, root):
        self.root = root
        root.title("Resolver 8-Puzzle")
        root.configure(bg="#f5f5f5")  # Fondo de la ventana principal
        
        # Estado inicial y objetivo del tablero
        self.initial_state = [[1, 2, 3], [4, 5, 0], [6, 7, 8]]
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.current_state = [row[:] for row in self.initial_state]  # Copia profunda del estado inicial

        self.create_widgets()

    def create_widgets(self):
        # Marco para el tablero del puzzle
        self.board_frame = tk.Frame(self.root, bg="#d4f1f9")
        self.board_frame.grid(row=0, column=0, padx=10, pady=10)

        # Crear botones para el tablero
        self.tile_buttons = []
        for row_idx in range(3):
            row_buttons = []
            for col_idx in range(3):
                button = tk.Button(
                    self.board_frame,
                    text=str(self.current_state[row_idx][col_idx]),
                    font=("Arial", 24),
                    width=4, height=2,
                    bg=self.get_button_color(self.current_state[row_idx][col_idx]),  # Color dinámico
                    fg="#ffffff" if self.current_state[row_idx][col_idx] != 0 else "#000000"  # Texto blanco o negro
                )
                button.grid(row=row_idx, column=col_idx, padx=5, pady=5)
                row_buttons.append(button)
            self.tile_buttons.append(row_buttons)

        # Marco para los controles
        self.control_frame = tk.Frame(self.root, bg="#e8f5e9")
        self.control_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

        # Etiqueta para mostrar el método actual
        self.method_label = tk.Label(self.control_frame, text="Método: Ninguno", font=("Arial", 12), bg="#e8f5e9", fg="#1b5e20")
        self.method_label.pack(pady=10)

        # Botones para los algoritmos de búsqueda
        self.bfs_button = tk.Button(self.control_frame, text="BFS", command=self.solve_bfs, width=10, font=("Arial", 12), bg="#aed581", fg="#1b5e20")
        self.bfs_button.pack(pady=5)

        self.dfs_button = tk.Button(self.control_frame, text="DFS", command=self.solve_dfs, width=10, font=("Arial", 12), bg="#ffcc80", fg="#bf360c")
        self.dfs_button.pack(pady=5)

        self.astar_button = tk.Button(self.control_frame, text="A*", command=self.solve_astar, width=10, font=("Arial", 12), bg="#4fc3f7", fg="#01579b")
        self.astar_button.pack(pady=5)

        self.greedy_button = tk.Button(self.control_frame, text="Greedy", command=self.solve_greedy, width=10, font=("Arial", 12), bg="#ce93d8", fg="#4a148c")
        self.greedy_button.pack(pady=5)

        # Botón para reiniciar el tablero
        self.reset_button = tk.Button(self.control_frame, text="Reiniciar", command=self.reset_board, width=10, font=("Arial", 12), bg="#ffab91", fg="#d84315")
        self.reset_button.pack(pady=20)

    def get_button_color(self, value):
        """Devuelve un color basado en el valor del botón."""
        if value == 0:
            return "#d1c4e9"  # Espacio vacío (morado suave)
        colors = {
            1: "#ff8a80",  # Rojo claro
            2: "#ffb74d",  # Naranja
            3: "#ffd54f",  # Amarillo
            4: "#81c784",  # Verde
            5: "#4fc3f7",  # Azul claro
            6: "#7986cb",  # Azul oscuro
            7: "#ba68c8",  # Morado
            8: "#f06292",  # Rosa
        }
        return colors.get(value, "#f5f5f5")  # Color predeterminado (gris claro)

    def update_board(self):
        """Actualiza el tablero con el estado actual."""
        for row_idx in range(3):
            for col_idx in range(3):
                value = self.current_state[row_idx][col_idx]
                self.tile_buttons[row_idx][col_idx].config(
                    text=str(value) if value != 0 else "",
                    bg=self.get_button_color(value)
                )

    def animate_solution(self, solution_steps):
        """Anima cada paso de la solución en el tablero."""
        for step in solution_steps:
            self.current_state = step
            self.update_board()
            self.root.update()
            self.root.after(1000)  # Espera 1 segundo entre pasos
        messagebox.showinfo("Solución Completa", "El puzzle ha sido resuelto.")

    def solve_bfs(self):
        """Resuelve el puzzle usando BFS y anima la solución."""
        self.method_label.config(text="Método: BFS")
        solution = bfs(self.initial_state, self.goal_state)
        if solution:
            self.animate_solution(solution)
        else:
            messagebox.showerror("Error", "No se encontró solución.")

    def solve_dfs(self):
        """Resuelve el puzzle usando DFS y anima la solución."""
        self.method_label.config(text="Método: DFS")
        solution = dfs(self.initial_state, self.goal_state)
        if solution:
            self.animate_solution(solution)
        else:
            messagebox.showerror("Error", "No se encontró solución.")

    def solve_astar(self):
        """Resuelve el puzzle usando A* y anima la solución."""
        self.method_label.config(text="Método: A*")
        solution = astar(self.initial_state, self.goal_state)
        if solution:
            self.animate_solution(solution)
        else:
            messagebox.showerror("Error", "No se encontró solución.")

    def solve_greedy(self):
        """Resuelve el puzzle usando Greedy y anima la solución."""
        self.method_label.config(text="Método: Greedy")
        solution = greedy(self.initial_state, self.goal_state)
        if solution:
            self.animate_solution(solution)
        else:
            messagebox.showerror("Error", "No se encontró solución.")

    def reset_board(self):
        """Reinicia el tablero al estado inicial."""
        self.current_state = [row[:] for row in self.initial_state]  # Copia profunda del estado inicial
        self.update_board()
        self.method_label.config(text="Método: Ninguno")

# Código para ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = PuzzleApp(root)
    root.mainloop()
