from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

class Propietario:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

class Mascota:
    def __init__(self, nombre, especie, raza, edad, propietario):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.propietario = propietario
        self.historial_medico = []

    def agregar_historial(self, diagnostico, tratamiento, medicamentos):
        cita = {
            'fecha': datetime.now(),
            'diagnostico': diagnostico,
            'tratamiento': tratamiento,
            'medicamentos': medicamentos
        }
        self.historial_medico.append(cita)

class Cita:
    def __init__(self, mascota, fecha, hora):
        self.mascota = mascota
        self.fecha = fecha
        self.hora = hora

class Medicamento:
    def __init__(self, nombre, descripcion, precio, existencias):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.existencias = existencias

class ClinicaVeterinaria:
    def __init__(self):
        self.mascotas = []
        self.citas = []
        self.medicamentos = []

    def registrar_mascota(self, mascota):
        self.mascotas.append(mascota)
        print(f"Mascota '{mascota.nombre}' registrada correctamente.")

    def actualizar_mascota(self, mascota, nombre=None, especie=None, raza=None, edad=None):
        if nombre:
            mascota.nombre = nombre
        if especie:
            mascota.especie = especie
        if raza:
            mascota.raza = raza
        if edad:
            mascota.edad = edad
        print(f"Información de '{mascota.nombre}' actualizada correctamente.")

    def consultar_historial(self, mascota):
        print(f"Historial médico de '{mascota.nombre}':")
        for cita in mascota.historial_medico:
            print(f"Fecha: {cita['fecha']}")
            print(f"Diagnóstico: {cita['diagnostico']}")
            print(f"Tratamiento: {cita['tratamiento']}")
            print(f"Medicamentos: {', '.join(cita['medicamentos'])}")
            print("---")

    def programar_cita(self, mascota, fecha, hora):
        cita = Cita(mascota, fecha, hora)
        self.citas.append(cita)
        print(f"Cita programada para '{mascota.nombre}' el {fecha} a las {hora}.")

    def registrar_consulta(self, mascota, diagnostico, tratamiento, medicamentos):
        mascota.agregar_historial(diagnostico, tratamiento, medicamentos)
        print(f"Consulta registrada para '{mascota.nombre}'.")

    def registrar_medicamento(self, nombre, descripcion, precio, existencias):
        medicamento = Medicamento(nombre, descripcion, precio, existencias)
        self.medicamentos.append(medicamento)
        print(f"Medicamento '{nombre}' registrado correctamente.")

    def actualizar_inventario(self, medicamento, existencias=None, precio=None):
        if existencias:
            medicamento.existencias = existencias
        if precio:
            medicamento.precio = precio
        print(f"Inventario de '{medicamento.nombre}' actualizado correctamente.")

    def generar_reporte_citas(self):
        print("Reporte de citas:")
        for cita in self.citas:
            print(f"Mascota: {cita.mascota.nombre}, Fecha: {cita.fecha}, Hora: {cita.hora}")

    def generar_reporte_ventas(self):
        print("Reporte de ventas de medicamentos:")
        for medicamento in self.medicamentos:
            print(f"Medicamento: {medicamento.nombre}, Existencias: {medicamento.existencias}")

GUI = Tk()
# Función para crear la Interfaz
def crear_gui(gui):
    gui.title("Sistema de Gestión de una Clínica Veterinaria")
    gui.resizable(True, True)
    gui.geometry("250x100")

    # Crear el menú principal
    menu_principal = Menu(gui)
    gui.config(menu=menu_principal)

    # Menu Mascotas
    menu_mascotas = Menu(menu_principal)
    menu_principal.add_cascade(label="Mascotas", menu=menu_mascotas)
    menu_mascotas.add_command(label="Registrar Mascota", command=abrir_registro_mascota)
    menu_mascotas.add_command(label="Actualizar Mascota", command=abrir_actualizar_mascota)
    menu_mascotas.add_command(label="Consultar Historial", command=abrir_historial_mascota)

    # Menu Citas
    menu_citas = Menu(menu_principal)
    menu_principal.add_cascade(label="Citas", menu=menu_citas)
    menu_citas.add_command(label="Programar Cita", command=abrir_programar_cita)
    menu_citas.add_command(label="Registrar Consulta", command=abrir_registrar_consulta)

    # Menu Inventario
    menu_inventario = Menu(menu_principal)
    menu_principal.add_cascade(label="Inventario", menu=menu_inventario)
    menu_inventario.add_command(label="Registrar Medicamento", command=abrir_registrar_medicamento)
    menu_inventario.add_command(label="Actualizar Inventario", command=abrir_actualizar_inventario)

    # Menu Reportes
    menu_reportes = Menu(menu_principal)
    menu_principal.add_cascade(label="Reportes", menu=menu_reportes)
    menu_reportes.add_command(label="Reporte de Citas", command=generar_reporte_citas)
    menu_reportes.add_command(label="Reporte de Ventas", command=generar_reporte_ventas)

    # Area de contenido principal
    area_contenido = Frame(GUI)
    area_contenido.pack(fill=BOTH, expand=True)

    gui.protocol("WM_DELETE_WINDOW", quit_app)
    gui.mainloop()
    
def quit_app():
    GUI.quit() 
    
def abrir_registro_mascota():
    ventana_registro = Toplevel(GUI)
    ventana_registro.title("Registrar Mascota")

    # Etiquetas y campos de entrada para los datos del propietario
    Label(ventana_registro, text="Nombre del propietario:").grid(row=0, column=0)
    entry_nombre_propietario = Entry(ventana_registro)
    entry_nombre_propietario.grid(row=0, column=1)

    Label(ventana_registro, text="Dirección del propietario:").grid(row=1, column=0)
    entry_direccion_propietario = Entry(ventana_registro)
    entry_direccion_propietario.grid(row=1, column=1)

    Label(ventana_registro, text="Teléfono del propietario:").grid(row=2, column=0)
    entry_telefono_propietario = Entry(ventana_registro)
    entry_telefono_propietario.grid(row=2, column=1)

    # Etiquetas y campos de entrada para los datos de la mascota
    Label(ventana_registro, text="Nombre de la mascota:").grid(row=3, column=0)
    entry_nombre_mascota = Entry(ventana_registro)
    entry_nombre_mascota.grid(row=3, column=1)

    Label(ventana_registro, text="Especie:").grid(row=4, column=0)
    entry_especie_mascota = Entry(ventana_registro)
    entry_especie_mascota.grid(row=4, column=1)

    Label(ventana_registro, text="Raza:").grid(row=5, column=0)
    entry_raza_mascota = Entry(ventana_registro)
    entry_raza_mascota.grid(row=5, column=1)

    Label(ventana_registro, text="Edad:").grid(row=6, column=0)
    entry_edad_mascota = Entry(ventana_registro)
    entry_edad_mascota.grid(row=6, column=1)

    def registrar_mascota():
        nombre_propietario = entry_nombre_propietario.get()
        direccion_propietario = entry_direccion_propietario.get()
        telefono_propietario = entry_telefono_propietario.get()
        nombre_mascota = entry_nombre_mascota.get()
        especie_mascota = entry_especie_mascota.get()
        raza_mascota = entry_raza_mascota.get()
        edad_mascota = int(entry_edad_mascota.get())

        propietario = Propietario(nombre_propietario, direccion_propietario, telefono_propietario)

        mascota = Mascota(nombre_mascota, especie_mascota, raza_mascota, edad_mascota, propietario)

        # Registrar la mascota en la clínica
        clinica.registrar_mascota(mascota)

        # Cerrar la ventana de registro
        ventana_registro.destroy()

    boton_registrar = Button(ventana_registro, text="Registrar", command=registrar_mascota)
    boton_registrar.grid(row=7, columnspan=2)

def abrir_actualizar_mascota():
    ventana_actualizar = Toplevel(GUI)
    ventana_actualizar.title("Actualizar Mascota")

    # Crear un campo de entrada para seleccionar la mascota
    Label(ventana_actualizar, text="Seleccionar mascota:").grid(row=0, column=0)
    combo_mascotas = ttk.Combobox(ventana_actualizar, values=[m.nombre for m in clinica.mascotas])
    combo_mascotas.grid(row=0, column=1)

    # Etiquetas y campos de entrada para los datos de la mascota
    Label(ventana_actualizar, text="Nombre de la mascota:").grid(row=1, column=0)
    entry_nombre_mascota = Entry(ventana_actualizar)
    entry_nombre_mascota.grid(row=1, column=1)

    Label(ventana_actualizar, text="Especie:").grid(row=2, column=0)
    entry_especie_mascota = Entry(ventana_actualizar)
    entry_especie_mascota.grid(row=2, column=1)

    Label(ventana_actualizar, text="Raza:").grid(row=3, column=0)
    entry_raza_mascota = Entry(ventana_actualizar)
    entry_raza_mascota.grid(row=3, column=1)

    Label(ventana_actualizar, text="Edad:").grid(row=4, column=0)
    entry_edad_mascota = Entry(ventana_actualizar)
    entry_edad_mascota.grid(row=4, column=1)

    def actualizar_mascota():
        # Obtener la mascota seleccionada
        nombre_mascota = combo_mascotas.get()
        mascota = next((m for m in clinica.mascotas if m.nombre == nombre_mascota), None)

        # Obtener los nuevos datos ingresados
        nuevo_nombre = entry_nombre_mascota.get() or mascota.nombre
        nueva_especie = entry_especie_mascota.get() or mascota.especie
        nueva_raza = entry_raza_mascota.get() or mascota.raza
        nueva_edad = entry_edad_mascota.get() or mascota.edad

        # Actualizar la información de la mascota
        clinica.actualizar_mascota(mascota, nuevo_nombre, nueva_especie, nueva_raza, nueva_edad)

        # Cerrar la ventana de actualización
        ventana_actualizar.destroy()

    boton_actualizar = Button(ventana_actualizar, text="Actualizar", command=actualizar_mascota)
    boton_actualizar.grid(row=5, columnspan=2)

def abrir_historial_mascota():
    ventana_historial = Toplevel(GUI)
    ventana_historial.title("Historial Médico")

    # Crear un campo de entrada para seleccionar la mascota
    Label(ventana_historial, text="Seleccionar mascota:").grid(row=0, column=0)
    combo_mascotas = ttk.Combobox(ventana_historial, values=[m.nombre for m in clinica.mascotas])
    combo_mascotas.grid(row=0, column=1)

    # Crear un area de texto para mostrar el historial
    area_historial = Text(ventana_historial, width=60, height=20)
    area_historial.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def mostrar_historial():
        # Obtener la mascota seleccionada
        nombre_mascota = combo_mascotas.get()
        mascota = next((m for m in clinica.mascotas if m.nombre == nombre_mascota), None)

        if mascota:
            # Limpiar el area de texto
            area_historial.delete('1.0', END)

            # Mostrar el historial medico de la mascota
            area_historial.insert(END, f"Historial médico de '{mascota.nombre}':\n\n")
            for cita in mascota.historial_medico:
                area_historial.insert(END, f"Fecha: {cita['fecha']}\n")
                area_historial.insert(END, f"Diagnóstico: {cita['diagnostico']}\n")
                area_historial.insert(END, f"Tratamiento: {cita['tratamiento']}\n")
                area_historial.insert(END, f"Medicamentos: {', '.join(cita['medicamentos'])}\n\n")
        else:
            area_historial.delete('1.0', END)
            area_historial.insert(END, "Seleccione una mascota primero.")

    boton_mostrar = Button(ventana_historial, text="Mostrar Historial", command=mostrar_historial)
    boton_mostrar.grid(row=2, column=0, columnspan=2, pady=10)

def abrir_programar_cita():
    ventana_cita = Toplevel(GUI)
    ventana_cita.title("Programar Cita")

    # Seleccionar mascota
    Label(ventana_cita, text="Seleccionar mascota:").grid(row=0, column=0)
    combo_mascotas = ttk.Combobox(ventana_cita, values=[m.nombre for m in clinica.mascotas])
    combo_mascotas.grid(row=0, column=1)

    # Ingresar fecha y hora
    Label(ventana_cita, text="Fecha de la cita:").grid(row=1, column=0)
    entry_fecha = Entry(ventana_cita)
    entry_fecha.grid(row=1, column=1)

    Label(ventana_cita, text="Hora de la cita:").grid(row=2, column=0)
    entry_hora = Entry(ventana_cita)
    entry_hora.grid(row=2, column=1)

    def programar_cita():
        nombre_mascota = combo_mascotas.get()
        mascota = next((m for m in clinica.mascotas if m.nombre == nombre_mascota), None)
        fecha = entry_fecha.get()
        hora = entry_hora.get()

        if mascota:
            clinica.programar_cita(mascota, fecha, hora)
            ventana_cita.destroy()
        else:
            messagebox.showerror("Error", "Seleccione una mascota primero.")

    boton_programar = Button(ventana_cita, text="Programar Cita", command=programar_cita)
    boton_programar.grid(row=3, columnspan=2, pady=10)

def abrir_registrar_consulta():
    ventana_consulta = Toplevel(GUI)
    ventana_consulta.title("Registrar Consulta")

    # Seleccionar mascota
    Label(ventana_consulta, text="Seleccionar mascota:").grid(row=0, column=0)
    combo_mascotas = ttk.Combobox(ventana_consulta, values=[m.nombre for m in clinica.mascotas])
    combo_mascotas.grid(row=0, column=1)

    # Ingresar diagnostico, tratamiento y medicamentos
    Label(ventana_consulta, text="Diagnóstico:").grid(row=1, column=0)
    entry_diagnostico = Entry(ventana_consulta)
    entry_diagnostico.grid(row=1, column=1)

    Label(ventana_consulta, text="Tratamiento:").grid(row=2, column=0)
    entry_tratamiento = Entry(ventana_consulta)
    entry_tratamiento.grid(row=2, column=1)

    Label(ventana_consulta, text="Medicamentos:").grid(row=3, column=0)
    entry_medicamentos = Entry(ventana_consulta)
    entry_medicamentos.grid(row=3, column=1)

    def registrar_consulta():
        nombre_mascota = combo_mascotas.get()
        mascota = next((m for m in clinica.mascotas if m.nombre == nombre_mascota), None)
        diagnostico = entry_diagnostico.get()
        tratamiento = entry_tratamiento.get()
        medicamentos = entry_medicamentos.get().split(',')

        if mascota:
            clinica.registrar_consulta(mascota, diagnostico, tratamiento, medicamentos)
            ventana_consulta.destroy()
        else:
            messagebox.showerror("Error", "Seleccione una mascota primero.")

    boton_registrar = Button(ventana_consulta, text="Registrar Consulta", command=registrar_consulta)
    boton_registrar.grid(row=4, columnspan=2, pady=10)

def abrir_registrar_medicamento():
    ventana_medicamento = Toplevel(GUI)
    ventana_medicamento.title("Registrar Medicamento")

    # Ingresar datos del medicamento
    Label(ventana_medicamento, text="Nombre del medicamento:").grid(row=0, column=0)
    entry_nombre = Entry(ventana_medicamento)
    entry_nombre.grid(row=0, column=1)

    Label(ventana_medicamento, text="Descripción:").grid(row=1, column=0)
    entry_descripcion = Entry(ventana_medicamento)
    entry_descripcion.grid(row=1, column=1)

    Label(ventana_medicamento, text="Precio:").grid(row=2, column=0)
    entry_precio = Entry(ventana_medicamento)
    entry_precio.grid(row=2, column=1)

    Label(ventana_medicamento, text="Existencias:").grid(row=3, column=0)
    entry_existencias = Entry(ventana_medicamento)
    entry_existencias.grid(row=3, column=1)

    def registrar_medicamento():
        nombre = entry_nombre.get()
        descripcion = entry_descripcion.get()
        precio = float(entry_precio.get())
        existencias = int(entry_existencias.get())

        clinica.registrar_medicamento(nombre, descripcion, precio, existencias)
        ventana_medicamento.destroy()

    boton_registrar = Button(ventana_medicamento, text="Registrar Medicamento", command=registrar_medicamento)
    boton_registrar.grid(row=4, columnspan=2, pady=10)

def abrir_actualizar_inventario():
    ventana_inventario = Toplevel(GUI)
    ventana_inventario.title("Actualizar Inventario")

    # Seleccionar medicamento
    Label(ventana_inventario, text="Seleccionar medicamento:").grid(row=0, column=0)
    combo_medicamentos = ttk.Combobox(ventana_inventario, values=[m.nombre for m in clinica.medicamentos])
    combo_medicamentos.grid(row=0, column=1)

    # Ingresar nuevas existencias y precio
    Label(ventana_inventario, text="Nuevas existencias:").grid(row=1, column=0)
    entry_existencias = Entry(ventana_inventario)
    entry_existencias.grid(row=1, column=1)

    Label(ventana_inventario, text="Nuevo precio:").grid(row=2, column=0)
    entry_precio = Entry(ventana_inventario)
    entry_precio.grid(row=2, column=1)

    def actualizar_inventario():
        nombre_medicamento = combo_medicamentos.get()
        medicamento = next((m for m in clinica.medicamentos if m.nombre == nombre_medicamento), None)

        if medicamento:
            nuevas_existencias = int(entry_existencias.get()) if entry_existencias.get() else None
            nuevo_precio = float(entry_precio.get()) if entry_precio.get() else None

            clinica.actualizar_inventario(medicamento, nuevas_existencias, nuevo_precio)
            ventana_inventario.destroy()
        else:
            messagebox.showerror("Error", "Seleccione un medicamento primero.")

    boton_actualizar = Button(ventana_inventario, text="Actualizar Inventario", command=actualizar_inventario)
    boton_actualizar.grid(row=3, columnspan=2, pady=10)
    
def generar_reporte_citas():
    ventana_reporte = Toplevel(GUI)
    ventana_reporte.title("Reporte de Citas")

    area_reporte = Text(ventana_reporte, width=60, height=20)
    area_reporte.pack(padx=10, pady=10)

    area_reporte.insert(END, "Reporte de citas:\n\n")
    for cita in clinica.citas:
        area_reporte.insert(END, f"Mascota: {cita.mascota.nombre}, Fecha: {cita.fecha}, Hora: {cita.hora}\n")

def generar_reporte_ventas():
    ventana_reporte = Toplevel(GUI)
    ventana_reporte.title("Reporte de Ventas")

    area_reporte = Text(ventana_reporte, width=60, height=20)
    area_reporte.pack(padx=10, pady=10)

    area_reporte.insert(END, "Reporte de ventas de medicamentos:\n\n")
    for medicamento in clinica.medicamentos:
        area_reporte.insert(END, f"Medicamento: {medicamento.nombre}, Existencias: {medicamento.existencias}\n")

clinica = ClinicaVeterinaria()

crear_gui(GUI)
