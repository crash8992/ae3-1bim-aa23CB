import sqlite3


conn = sqlite3.connect('basedatosJUG.db')


conn.execute('''CREATE TABLE IF NOT EXISTS Jugadores
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             Nombre TEXT NOT NULL,
             Apellido TEXT NOT NULL,
             Edad INTEGER NOT NULL,
             MinutosJugados INTEGER NOT NULL DEFAULT 0,
             Lesiones INTEGER NOT NULL DEFAULT 0);''')



nombre = input("Introduce el nombre: ")
apellido = input("Introduce el apellido: ")
edad = input("Introduce la edad: ")
min_jugados = int(input("Introduce los minutos jugados: "))
lesiones = bool(input("¿Ha tenido lesiones? (introduce 0 para no, 1 para sí): "))

conn.execute("INSERT INTO Jugadores (Nombre, Apellido, Edad, MinutosJugados, Lesiones) VALUES (?, ?, ?, ?, ?)", (nombre, apellido, edad, min_jugados, lesiones))
conn.commit()


conn.close()