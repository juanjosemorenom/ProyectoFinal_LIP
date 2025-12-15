# LIBRERÍAS

from random import choice
import tkinter as tk
from tkinter import messagebox
import json
import os

# VARIABLES GLOBALES PARA LA INTERFAZ

ventana = None
ventanaJuego = None
canvas = None
labelPalabra = None
labelVidas = None
botonesTeclado = {}
opcionCategoria = None
opcionDificultad = None
opcionModalidad = None

# VARIABLES GLOBALES DEL JUEGO

palabra = ""
pista = ""
vidas = 0
vidasIniciales = 0
vidasGlobales = None
letrasUsadas = set()
palabraAdivinada = []
ronda = 0
modalidad = 1
glosario = {}
estadisticas = {"partidasJugadas": 0, "partidasGanadas": 0, "rachaActual": 0, "mejorRacha": 0}

# DATOS (LISTAS Y DICCIONARIOS) QUE SE USARÁN EN EL JUEGO

america = ["Canadá", "Estados_Unidos", "México", "Guatemala", "Belice", "Honduras", "El_Salvador", "Nicaragua", "Costa_Rica", "Panamá", "Colombia", "Venezuela", "Guyana", "Ecuador", "Perú", "Bolivia", "Brasil", "Paraguay", "Uruguay", "Argentina", "Chile", "Bahamas", "Cuba", "República_Dominicana", "Haití", "Jamaica", "Antigua_y_Barbuda", "Barbados", "Trinidad_y_Tobago", "Dominica", "Granada", "San_Cristóbal_y_Nives", "San_Vicente_y_las_Granadinas", "Santa_Lucía"]
oceania = ["Australia", "Nueva_Zelanda", "Fiyi", "Islas_Marshall", "Islas_Salomón", "Kiribati", "Estados_Federados_de_Micronesia", "Nauru", "Palaos", "Samoa", "Tonga", "Tuvalu", "Vanuatu"]
europa = ["España", "Portugal", "Andorra", "Francia", "Mónaco", "Islandia", "Irlanda", "Reino_Unido", "Bélgica", "Países_Bajos", "Luxemburgo", "Suiza", "Italia", "San_Marino", "Ciudad_del_Vaticano", "Malta", "Liechtenstein", "Alemania", "Dinamarca", "Polonia", "Chequia", "Eslovaquia", "Austria", "Hungría", "Eslovenia", "Croacia", "Bosnia_y_Herzegovina", "Montenegro", "Albania", "Serbia", "Macedonia_del_Norte", "Kosovo", "Grecia", "Bulgaria", "Rumania", "Moldavia", "Ucrania", "Bielorrusia", "Estonia", "Letonia", "Lituania", "Noruega", "Suecia", "Finlandia", "Rusia"]
asia = ["Afganistán", "Arabia_Saudita", "Armenia", "Azerbaiyán", "Bangladesh", "Bahréin", "Myanmar", "Brunéi", "Bután", "Camboya",  "Catar", "China", "Chipre", "Corea_del_Norte", "Corea_del_Sur", "Egipto", "Emiratos_Árabes_Unidos", "Filipinas", "Georgia", "India", "Indonesia", "Irak", "Irán", "Israel", "Japón", "Jordania", "Kazajistán", "Kirguistán", "Kuwait", "Laos", "Líbano", "Maldivas", "Malasia", "Mongolia", "Nepal", "Omán", "Pakistán", "Singapur", "Siria", "Sri Lanka", "Tailandia", "Tayikistán", "Timor_Oriental", "Turkmenistán", "Turquía", "Uzbekistán", "Vietnam", "Yemen"]
africa = ["Angola", "Argelia", "Benín", "Botsuana", "Burkina_Faso", "Burundi", "Cabo_Verde", "Camerún", "Chad", "República_Centroafricana", "Comoras", "República_del_Congo", "República_Democrática_del_Congo", "Costa_de_Marfil", "Egipto", "Eritrea", "Etiopía", "Gabón", "Gambia", "Ghana", "Guinea", "Guinea_Bisáu", "Guinea_Ecuatorial", "Kenia", "Lesoto", "Liberia", "Libia", "Madagascar", "Malaui", "Malí", "Marruecos", "Mauricio", "Mauritania", "Mozambique", "Namibia", "Níger", "Nigeria", "Ruanda", "Santo_Tomé_y_Príncipe", "Senegal", "Seychells", "Sierra_Leona", "Somalia", "Suazilandia", "Sudáfrica", "Sudán", "Sudán_del_Sur", "Tanzania", "Togo", "Túnez", "Uganda", "Yibuti", "Zambia", "Zimbabue"] 

mamiferos = ["Perro", "Gato", "León", "Elefante", "Venado", "Caballo", "Ballena", "Canguro", "Jirafa", "Delfin", "Murciélago", "Guepardo", "Leopardo", "Jaguar", "Conejo", "Liebre", "Borrega", "Pantera", "Rinoceronte", "Hipopotamo", "Tigre", "Alpaca", "Zorrillo", "Zorro", "Armadillo", "Ornitorrrinco"]
reptiles = ["Tortuga", "Cocodrilo", "Serpiente", "Caimán", "Iguana", "Lagartija", "Camaleón", "Lagarto", "Salamandra"]
aves = ["Paloma", "Loro", "Halcón", "Pato", "Cisne", "Garza", "Gaviota", "Pelicano", "Ganso", "Águila", "Avestruz", "Colibrí", "Quetzal", "Golondrina", "Flamenco", "Búho"]

paises = {"América": america, "Oceanía": oceania, "Europa": europa, "Asia": asia, "África": africa}

fauna = {"Mamíferos": mamiferos, "Reptiles": reptiles, "Aves": aves}

fiesta = {**paises, **fauna} 

dificultadVidas = {"1": 6, "2": 5, "3": 4, "4": 3}

# FUNCIONES DE ESTADÍSTICAS

def cargarEstadisticas():
    """
    Carga las estadísticas del usuario desde el archivo .JSON
    Args:
        Nada
    Returns:
        Nada
    """
    global estadisticas
    try:
        if os.path.exists("estadisticas.json"):
            with open("estadisticas.json", "r") as archivo:
                estadisticas = json.load(archivo)
    except:
        pass

def guardarEstadisticas():
    """
    Guarda las estadísticas del usuario en el archivo .JSON
    Args:
        Nada
    Returns:
        Nada
    """
    try:
        with open("estadisticas.json", "w") as archivo:
            json.dump(estadisticas, archivo)
    except:
        pass

def exportarArchivo():
    """
    Exporta las estadísticas del usuario en un archivo .TXT
    Args:
        Nada
    Returns:
        Nada
    """
    eJ = f"Estadísticas del Jugador:\n\n"
    pJ = f"Partidas Jugadas: {estadisticas['partidasJugadas']}\n"
    pG = f"Partidas Ganadas: {estadisticas['partidasGanadas']}\n"
    rA = f"Racha Actual: {estadisticas['rachaActual']}\n"
    mR = f"Mejor Racha: {estadisticas['mejorRacha']}\n"
    if estadisticas['partidasJugadas'] > 0:
        porcentaje = (estadisticas['partidasGanadas'] / estadisticas['partidasJugadas'] * 100)
        pV = f"Porcentaje de Victoria: {porcentaje:.2f}%\n"
    else:
        pV = ""
    try:
        with open("TusEstadísticas.txt", "w") as exportado:
            exportado.write(eJ+pJ+pG+rA+mR+pV)
        messagebox.showinfo("Exportación exitosa", "Las estadísticas han sido exportadas a 'TusEstadísticas.txt'")
    except Exception:
        messagebox.showerror("Error de Exportación", "No se pudo exportar el archivo")

def mostrarEstadisticas():
    """
    Muestra las estadísticas del usuario en otra ventana
    Args:
        Nada
    Returns:
        Nada
    """
    ventanaEstadisticas = tk.Toplevel(ventana)
    ventanaEstadisticas.title("📊 Estadísticas del Jugador")
    ventanaEstadisticas.geometry("400x400")
    ventanaEstadisticas.configure(bg="#2D707C")
    ventanaEstadisticas.resizable(False, False)
    titulo = tk.Label(ventanaEstadisticas, text="📊 TUS ESTADÍSTICAS", font=("Arial", 20, "bold"), bg="#458C99", fg="white")
    titulo.pack(pady=20)

    ests = [f"🎮 Partidas Jugadas: {estadisticas['partidasJugadas']}", f"🏆 Partidas Ganadas: {estadisticas['partidasGanadas']}", f"🔥 Racha Actual: {estadisticas['rachaActual']}", f"⭐ Mejor Racha: {estadisticas['mejorRacha']}"]
    if estadisticas['partidasJugadas'] > 0:
        porcentaje = (estadisticas['partidasGanadas'] / estadisticas['partidasJugadas'] * 100)
        ests.append(f"📈 Porcentaje de Victoria: {porcentaje:.2f}%")

    for est in ests:
        label = tk.Label(ventanaEstadisticas, text=est, font=("Arial", 12), bg="#458C99", fg="white")
        label.pack(pady=8)

    botonExportar = tk.Button(ventanaEstadisticas, text="Exportar", command=exportarArchivo,bg="#3498DB", fg="white", font=("Arial", 10, "bold"))
    botonExportar.pack(pady=20)
    botonCerrar = tk.Button(ventanaEstadisticas, text="Cerrar", command=ventanaEstadisticas.destroy,bg="#4FBFCE", fg="white", font=("Arial", 10, "bold"))
    botonCerrar.pack(pady=10)

# FUNCIONES DEL JUEGO

def iniciarJuego():
    """
    Inicializa el juego verificando la selección del usuario
    Args:
        Nada
    Returns:
        Nada
    """
    global glosario, vidasIniciales, modalidad

    categoria = opcionCategoria.get()
    if not categoria:
        messagebox.showerror("ERROR", "Debes seleccionar una categoría de juego ⚠️")
        return
    if categoria == "Países del mundo":
        for texto, grupo in paises.items():
            glosario[texto] = grupo.copy()
    elif categoria == "Animales del mundo":
        for texto, grupo in fauna.items():
            glosario[texto] = grupo.copy()
    else:
         for texto, grupo in fiesta.items():
            glosario[texto] = grupo.copy()
 
    vidasInicio = opcionDificultad.get()
    if not vidasInicio:
        messagebox.showerror("ERROR", "Debes seleccionar una dificultad de juego ⚠️")
        return    
    vidasIniciales = dificultadVidas[opcionDificultad.get()]  

    mod = opcionModalidad.get()
    if not mod:
        messagebox.showerror("ERROR", "Debes seleccionar una modalidad de juego ⚠️")
        return
    modalidad = int(opcionModalidad.get())

    iniciarRonda()
    
def iniciarRonda():
    """
    Selecciona la palabra por adivinar aleatoriamente (según la categoría seleccionada), establece la cantidad de vidas (según la dificultad) 
        y actualiza la palabra mientras se va adivinando
    Args:
        Nada
    Returns:
        Nada
    """
    global ventanaJuego, palabra, pista, vidas, letrasUsadas, palabraAdivinada, ronda, vidasGlobales
    ronda += 1
    
    if not glosario:
        messagebox.showinfo("JUEGO TERMINADO", "¡Has completado adivinado todas las palabras! 🎉")
        if ventanaJuego:
            ventanaJuego.destroy()
        return
    
    if modalidad == 2 and vidasGlobales is not None and vidasGlobales == 0:
        messagebox.showinfo("EL JUEGO TERMINÓ", f"Tu racha terminó en la RONDA {ronda - 1} 😢")
        if ventanaJuego:
            ventanaJuego.destroy()
        return
    
    pistaCategoria = choice(list(glosario.keys()))
    palabras = glosario[pistaCategoria]
    palabra = choice(palabras)
    palabras.remove(palabra)

    if not palabras:
        del glosario[pistaCategoria]
    
    palabra = palabra.upper().replace("_", " ")
    pista = pistaCategoria
    
    if modalidad == 1:
        vidas = vidasIniciales
    else:
        if vidasGlobales is None:
            vidasGlobales = vidasIniciales
        vidas = vidasGlobales

    letrasUsadas = set()
    palabraAdivinada = []

    for letra in palabra:
        if letra != " ":
            palabraAdivinada.append("_")
        else:
            palabraAdivinada.append(" ")

    crearInterfaz()

def crearInterfaz():
    """
    Crea y actualiza la ventana del juego y los widgets, una vez que se ha iniciado la ronda
    Args:
        Nada
    Returns:
        Nada
    """
    global ventanaJuego, canvas, labelPalabra, labelVidas
    
    if ventanaJuego is None:
        ventanaJuego = tk.Toplevel(ventana)
        ventanaJuego.title("Jugando Ahorcado 🎮")
        ventanaJuego.geometry("1200x650")
        ventanaJuego.configure(bg="#2C3E50")
        ventanaJuego.resizable(False, False)
        ventanaJuego.protocol("WM_DELETE_WINDOW", cerrarVentanaJuego)
    
    for widget in ventanaJuego.winfo_children():
        widget.destroy()

    headerFrame = tk.Frame(ventanaJuego, bg="#34495E")
    headerFrame.pack(fill="x", pady=10)
    
    labelRonda = tk.Label(headerFrame, text=f"🎯 RONDA {ronda}", font=("Arial", 16, "bold"), bg="#34495E", fg="white")
    labelRonda.pack(pady=5)
    
    labelPista = tk.Label(headerFrame, text=f"💡 Pista: {pista}", font=("Arial", 14), bg="#34495E", fg="orange")
    labelPista.pack(pady=5)

    canvas = tk.Canvas(ventanaJuego, width=300, height=280, bg="white", highlightthickness=2, highlightbackground="#34495E")
    canvas.pack(pady=10)
    dibujarAhorcado()

    labelPalabra = tk.Label(ventanaJuego, text=" ".join(palabraAdivinada),font=("Courier", 28, "bold"), bg="#2C3E50", fg="white")
    labelPalabra.pack(pady=15)

    labelVidas = tk.Label(ventanaJuego, text=f"❤️ Vidas: {vidas}", font=("Arial", 14, "bold"), bg="#2C3E50", fg="red")
    labelVidas.pack(pady=5)

    crearTeclado()

def cerrarVentanaJuego():
    """
    Cierra la ventana de juego y reinicia el contador de rondas y de vidas
    Args:
        Nada
    Returns:
        Nada
    """
    global ventanaJuego, ronda, vidasGlobales
    ventanaJuego.destroy()
    ventanaJuego = None
    ronda = 0
    vidasGlobales = None

def crearTeclado():
    """
    Crea y muestra un teclado tipo QWERTY para que el usuario introduzca las letras
    Args:
        Nada
    Returns:
        Nada
    """
    global botonesTeclado
    
    frameTeclado = tk.Frame(ventanaJuego, bg="#2C3E50")
    frameTeclado.pack(pady=10)
    filas = ["QWERTYUIOP", "ASDFGHJKLÑ", "ZXCVBNM"]
    botonesTeclado = {}
    
    for fila in filas:
        frameLinea = tk.Frame(frameTeclado, bg="#2C3E50")
        frameLinea.pack()
        for letra in fila:
            tecla = tk.Button(frameLinea, text=letra, width=3, height=1, font=("Arial", 12, "bold"), bg="#3091D1", fg="white", command = lambda l=letra : verificarLetra(l))
            tecla.pack(side="left", padx=2, pady=2)
            botonesTeclado[letra] = tecla

def verificarLetra(letra):
    """
    Verifica el estado de la letra presionada en el teclado por el usuario:
        - Deshabilita la letra en el teclado, si ya se utilizó
        - Si no se adivinó la letra, se resta una vida
    Args:
        letra (str): Letra mayúscula seleccionada por el usuario en el teclado
    Returns:
        Nada
    """
    global vidas, vidasGlobales
    
    if letra in letrasUsadas:
        return
    
    letrasUsadas.add(letra)
    botonesTeclado[letra].config(state="disabled", bg="#698183")
    
    variantes = obtenerVariantes(letra)
    encontrada = False
    for var in variantes:
        if var in palabra:
            encontrada = True
            for i, car in enumerate(palabra):
                if car == var:
                    palabraAdivinada[i] = var
    if not encontrada:
        vidas -= 1
        if modalidad == 2:
            vidasGlobales = vidas
    
    actualizarInterfaz()
    verificarFinDeRonda()

def dibujarAhorcado():
    """
    Dibuja una parte de la figura del ahorcado en el canvas, cada vez que se comete un error
    Args:
        Nada
    Returns:
        Nada
    """
    canvas.delete("all")
    errores = vidasIniciales - vidas

    canvas.create_line(50, 250, 200, 250, width=4, fill="#34495E")
    canvas.create_line(100, 250, 100, 50, width=4, fill="#34495E")
    canvas.create_line(100, 50, 200, 50, width=4, fill="#34495E")
    canvas.create_line(200, 50, 200, 80, width=3, fill="#6D7879")
    
    if errores >= 1:
        canvas.create_oval(180, 80, 220, 120, width=3, outline="red")
    if errores >= 2:
        canvas.create_line(200, 120, 200, 180, width=3, fill="red")
    if errores >= 3:
        canvas.create_line(200, 140, 170, 160, width=3, fill="red")
    if errores >= 4:
        canvas.create_line(200, 140, 230, 160, width=3, fill="red")
    if errores >= 5:
        canvas.create_line(200, 180, 170, 230, width=3, fill="red")
    if errores >= 6:
        canvas.create_line(200, 180, 230, 230, width=3, fill="red")

def obtenerVariantes(letra):
    """
    Define las variantes de una letra que podría o no, estar acentuada
    Args:
        letra (str): Letra mayúscula seleccionada por el usuario en el teclado
    Returns:
        Lista de las variantes de la letra tecleada o la letra por defecto
    """
    variantes = {
        'A': ['A', 'Á'], 'E': ['E', 'É'], 'I': ['I', 'Í'],
        'O': ['O', 'Ó'], 'U': ['U', 'Ú']
    }
    return variantes.get(letra, [letra])

def actualizarInterfaz():
    """
    Actualiza el contador de vidas, la palabra y el dibujo del ahorcado mientras se va adivinando la palabra
    Args:
        Nada
    Returns:
        Nada
    """
    labelPalabra.config(text=" ".join(palabraAdivinada))
    labelVidas.config(text=f"❤️ Vidas: {vidas}")
    dibujarAhorcado()

def verificarFinDeRonda():
    """
    Verifica que ya no queden letras por adivinar o que se hayan terminado las vidas
    Args:
        Nada
    Returns:
        Nada
    """
    if "_" not in palabraAdivinada:
        finalizarRonda(True)
    elif vidas <= 0:
        finalizarRonda(False)

def finalizarRonda(gane):
    """
    Finaliza la ronda si ya se adivinaron todas las letras o se terminaron las vidas en la ronda anterior
    Args:
        gane (bool): Indica si se ganó o se perdió la ronda
    Returns:
        Nada
    """
    global ronda 
    for boton in botonesTeclado.values():
        boton.config(state="disabled")
    
    if gane:
        estadisticas["partidasGanadas"] += 1
        estadisticas["rachaActual"] += 1
        if estadisticas["rachaActual"] > estadisticas["mejorRacha"]:
            estadisticas["mejorRacha"] = estadisticas["rachaActual"]
        mensaje = f"🎉 ¡FELICIDADES!\nLa palabra era: {palabra}"
        if modalidad == 1:
            respuesta = messagebox.askyesno("Victoria", mensaje + "\n\n¿Jugar otra ronda?")
            if respuesta:
                iniciarRonda()
            else:
                cerrarVentanaJuego()
        else:
            messagebox.showinfo("Victoria", mensaje)
            iniciarRonda()
    else:
        estadisticas["rachaActual"] = 0
        mensaje = f"😢 PERDISTE\nLa palabra era: {palabra}"
        if modalidad == 1:
            respuesta = messagebox.askyesno("Derrota", mensaje + "\n\n¿Jugar otra ronda?")
            if respuesta:
                ronda = 0 
                iniciarRonda()
            else:
                cerrarVentanaJuego()
        else:
            messagebox.showinfo("JUEGO TERMINADO", f"{mensaje}\n🏆 Llegaste a la RONDA {ronda}")
            cerrarVentanaJuego()
    
    estadisticas["partidasJugadas"] += 1
    guardarEstadisticas()

def crearInterfazDeInicio():
    """
    Crea ventana de inicio del juego y actualiza los widgets para la configuración del juego
    Args:
        Nada
    Returns:
        Nada
    """
    global ventana, opcionCategoria, opcionDificultad, opcionModalidad
    global lista, entrada
    
    ventana = tk.Tk()
    ventana.title("Asistente de juego del AHORCADO")
    ventana.geometry("800x750")
    ventana.resizable(False, False)
    ventana.configure(bg="#346CA3")
    
    opcionCategoria = tk.StringVar(value="")
    opcionDificultad = tk.StringVar(value="")
    opcionModalidad = tk.StringVar(value="")
    
    titulo = tk.Label(ventana, text="🎮 AHORCADO 🐍", font=("Arial", 32, "bold"), bg="#305E8B", fg="white")
    titulo.pack(pady=15)

    mainFrame = tk.Frame(ventana, bg="#3C6A99")
    mainFrame.pack(fill="both", expand=True, padx=20)

    frameCategoria = tk.LabelFrame(mainFrame, text="1️⃣ Selecciona una Categoría", font=("Arial", 12, "bold"), bg="#385E97", fg="white", padx=10, pady=10)
    frameCategoria.pack(pady=8, fill="x")
    opcionesCat = [("🌎 Países del mundo", "Países del mundo", "#369BB9"), ("🦁 Animales del mundo", "Animales del mundo", "#3A9C37"), ("🎉 ¡FIESTA!", "¡FIESTA!", "purple")] 
    for texto, valor, color in opcionesCat:
        btn = tk.Radiobutton(frameCategoria, text=texto, variable=opcionCategoria, value=valor, indicatoron=0, font=("Arial", 10, "bold"), bg=color, fg="white", selectcolor=color, activebackground=color, width=20, height=2)
        btn.pack(side="left", padx=5, expand=True, fill="x")

    frameDificultad = tk.LabelFrame(mainFrame, text="2️⃣ Selecciona Dificultad", font=("Arial", 12, "bold"), bg="#385E97", fg="white", padx=10, pady=10)
    frameDificultad.pack(pady=8, fill="x")
    opcionesDificultad = [("Fácil (6❤️)", "1", "#3A9C37"), ("Medio (5❤️)", "2", "#D4D227"), ("Difícil (4❤️)", "3", "orange"), ("Extremo (3❤️)", "4", "red")]
    for texto, valor, color in opcionesDificultad:
        btn = tk.Radiobutton(frameDificultad, text=texto, variable=opcionDificultad, value=valor, indicatoron=0, font=("Arial", 9, "bold"), bg=color, fg="white", selectcolor=color, activebackground=color, width=14)
        btn.pack(side="left", padx=3, expand=True)

    frameModalidad = tk.LabelFrame(mainFrame, text="3️⃣ Selecciona Modalidad", font=("Arial", 12, "bold"), bg="#385E97", fg="white", padx=10, pady=10)
    frameModalidad.pack(pady=8, fill="x")
    opcionesMod = [("RONDAS", "1", "#369BB9"), ("MUERTE SÚBITA", "2", "purple")]
    for texto, valor, color in opcionesMod:
        btn = tk.Radiobutton(frameModalidad, text=texto, variable=opcionModalidad, value=valor, indicatoron=0, font=("Arial", 10, "bold"), bg=color, fg="white", selectcolor=color, activebackground=color, width=28)
        btn.pack(side="left", padx=5, expand=True)
    
    frameBotones = tk.LabelFrame(ventana, text="OPCIONES", font=("Arial", 12, "bold"), bg="#305E8B", fg="#ECF0F1")
    frameBotones.pack(pady=20)
    botonIniciar = tk.Button(frameBotones, text="▶️  INICIAR JUEGO", command=iniciarJuego,font=("Arial", 16, "bold"), bg="#2CD30B", fg="white",width=18, height=2, cursor="hand2")
    botonIniciar.pack(side="left", padx=10)
    botonEstadisticas = tk.Button(frameBotones, text="📊 ESTADÍSTICAS", command=mostrarEstadisticas, font=("Arial", 12, "bold"), bg="#255CF1", fg="white",width=18, height=2, cursor="hand2")
    botonEstadisticas.pack(side="left", padx=10)
    botonSalir = tk.Button(frameBotones, text="❌ SALIR", command=ventana.destroy,font=("Arial", 16, "bold"), bg="red", fg="white", width=12, height=2, cursor="hand2")
    botonSalir.pack(side="left", padx=10)

cargarEstadisticas()
crearInterfazDeInicio()

ventana.mainloop()