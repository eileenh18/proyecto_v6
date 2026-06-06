import tkinter as tk
import sqlite3

class RegistroApp:
    def __init__(self):
        self.conexion = sqlite3.connect("registro_bullying.bd")
        self.cursor = self.conexion.cursor()
        self.crear_tablas()

        self.password_admin = "ad1234"

        self.ventana = tk.Tk()
        self.ventana.title("Registro")
        self.ventana.geometry("400x300")

        self.color_fondo = "#90CAF9"
        self.color_boton = "#2196F3"
        self.color_boton_activo = "#0D47A1"
        self.color_texto = "#0D47A1"
        
        self.ventana.configure(bg=self.color_fondo)

        self.menu()
        self.ventana.mainloop()

    def crear_tablas(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS victimas (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, lugar TEXT, tipo TEXT, grupo TEXT)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS testigos (id INTEGER PRIMARY KEY AUTOINCREMENT, lugar TEXT, tipo TEXT, intervino TEXT, grupo TEXT)""")

    def limpiar(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def menu(self):
        self.limpiar()
        tk.Label(self.ventana, text="Selecciona una opcion:", font=("Arial", 15), bg=self.color_fondo, fg=self.color_texto).pack(pady=10)
        
        tk.Button(self.ventana, text="Victima", bg=self.color_boton, fg="white", activebackground=self.color_boton_activo, command=self.victima).pack(pady=5)
        tk.Button(self.ventana, text="Testigo", bg=self.color_boton, fg="white", activebackground=self.color_boton_activo, command=self.testigo).pack(pady=5)
        tk.Button(self.ventana, text="Administrador", bg=self.color_boton, fg="white", activebackground=self.color_boton_activo, command=self.admin_login).pack(pady=5)
        tk.Button(self.ventana, text="Salir", bg=self.color_boton, fg="white", activebackground=self.color_boton_activo, command=self.ventana.destroy).pack(pady=5)

    def admin_login(self):
        self.limpiar()
        tk.Label(self.ventana, text="ADMINISTRADOR", font=("Arial", 13), bg=self.color_fondo, fg=self.color_texto).pack()

        tk.Label(self.ventana, text="Contraseña: ", bg=self.color_fondo).pack()
        entry_password = tk.Entry(self.ventana, show="*")
        entry_password.pack()

        def verificar():
            if entry_password.get() == self.password_admin:
                self.admin_archivos()
            else:
                tk.Label(self.ventana, text="Contraseña incorrecta", fg="red", bg=self.color_fondo).pack()

        tk.Button(self.ventana, text="Ingresar", bg=self.color_boton, fg="white", activebackground=self.color_boton_activo, command=verificar).pack(pady=5)
        tk.Button(self.ventana, text="Menu", bg=self.color_boton, fg="white", activebackground=self.color_boton_activo, command=self.menu).pack()

    def admin_archivos(self):
        self.limpiar()

        tk.Label(self.ventana, text="REGISTROS", font=("Arial", 13), bg=self.color_fondo, fg=self.color_texto).pack()
        
        texto = tk.Text(self.ventana, height=12, width=50)
        texto.pack()

        texto.insert(tk.END, "===VICTIMAS===\n")
        self.cursor.execute("SELECT nombre, lugar, tipo, grupo FROM victimas")
        for v in self.cursor.fetchall():
            texto.insert(tk.END, f"Nombre: {v[0]}, Lugar: {v[1]}, Tipo: {v[2]},\n Grupo: {v[3]}\n")

        texto.insert(tk.END, "===TESTIGOS===\n")
        self.cursor.execute("SELECT lugar, tipo, intervino, grupo FROM testigos")
        for t in self.cursor.fetchall():
            texto.insert(tk.END, f"Lugar: {t[0]}, Tipo: {t[1]}, Intervino: {t[2]},\n Grupo: {t[3]}\n")

        tk.Button(self.ventana, text="Menu", bg=self.color_boton, fg="white", activebackground=self.color_boton_activo, command=self.menu).pack()

    def victima(self):
        self.limpiar()
        tk.Label(self.ventana, text="VICTIMA", font=("Arial", 13), bg=self.color_fondo, fg=self.color_texto).pack()

        tk.Label(self.ventana, text="Nombre: (puede ser anonimo)", bg=self.color_fondo).pack()
        entry_nombre = tk.Entry(self.ventana)
        entry_nombre.pack()
  
        tk.Label(self.ventana, text="Lugar de la escuela: ", bg=self.color_fondo).pack()
        entry_lugar = tk.Entry(self.ventana)
        entry_lugar.pack()
  
        tk.Label(self.ventana, text="Tipo de bullying: ", bg=self.color_fondo).pack()
        entry_tipo = tk.Entry(self.ventana)
        entry_tipo.pack()

        tk.Label(self.ventana, text="Si sabe el grupo del agresor/a ingreselo: ", bg=self.color_fondo).pack()
        entry_grupo = tk.Entry(self.ventana)
        entry_grupo.pack()

        def guardar():
            self.cursor.execute("INSERT INTO victimas (nombre, lugar, tipo, grupo) VALUES (?, ?, ?, ?)",
                (entry_nombre.get(), entry_lugar.get(), entry_tipo.get(), entry_grupo.get())
            )
            self.conexion.commit()
            self.menu()

        tk.Button(self.ventana, text="Guardar", bg=self.color_boton, fg="white", activebackground=self.color_boton_activo, command=guardar).pack(pady=5)
        tk.Button(self.ventana, text="Menu", bg=self.color_boton, fg="white", activebackground=self.color_boton_activo, command=self.menu).pack()

    def testigo(self):
        self.limpiar()
        tk.Label(self.ventana, text="TESTIGO", font=("Arial", 13), bg=self.color_fondo, fg=self.color_texto).pack()
        
        tk.Label(self.ventana, text="Lugar de la escuela: ", bg=self.color_fondo).pack()
        entry_lugar = tk.Entry(self.ventana)
        entry_lugar.pack()
  
        tk.Label(self.ventana, text="Tipo de bullying: ", bg=self.color_fondo).pack()
        entry_tipo = tk.Entry(self.ventana)
        entry_tipo.pack()
  
        tk.Label(self.ventana, text="Intervino? si/no: ", bg=self.color_fondo).pack()
        entry_intervino = tk.Entry(self.ventana)
        entry_intervino.pack()

        tk.Label(self.ventana, text="Si sabe el grupo del agresor/a ingreselo: ", bg=self.color_fondo).pack()
        entry_grupo = tk.Entry(self.ventana)
        entry_grupo.pack()

        def guardar():
            self.cursor.execute("INSERT INTO testigos (lugar, tipo, intervino, grupo) VALUES (?, ?, ?, ?)",
                (entry_lugar.get(), entry_tipo.get(), entry_intervino.get(), entry_grupo.get())
            )
            self.conexion.commit()
            self.menu()

        tk.Button(self.ventana, text="Guardar", bg=self.color_boton, fg="white", activebackground=self.color_boton_activo, command=guardar).pack(pady=5)
        tk.Button(self.ventana, text="Menu", bg=self.color_boton, fg="white", activebackground=self.color_boton_activo, command=self.menu).pack()

RegistroApp()
