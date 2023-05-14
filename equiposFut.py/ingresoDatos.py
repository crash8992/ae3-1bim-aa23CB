import sqlite3


conn = sqlite3.connect('baseDatosEQ.db')


conn.execute('''CREATE TABLE IF NOT EXISTS Equipos
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre TEXT NOT NULL,
             puntosGanados INTEGER NOT NULL,
             golesFavor INTEGER NOT NULL,
             golesContra INTEGER NOT NULL);''')
conn.commit()

nombre = input("Introduce el nombre del equipo: ")
puntosGanados = int(input("Introduce los puntos ganados por el equipo: "))
golesFavor = int(input("Introduce los goles a favor del equipo: "))
golesContra = int(input("Introduce los goles en contra del equipo: "))

conn.execute("INSERT INTO Equipos (nombre, puntosGanados, golesFavor, golesContra) VALUES (?, ?, ?, ?)", (nombre, puntos_ganados, goles_a_favor, goles_en_contra))
conn.commit()

conn.close()
