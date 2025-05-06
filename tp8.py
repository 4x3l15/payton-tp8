import pandas as pd

# 1. Ubipark: Análisis de Estacionamientos en Córdoba
# Definición del dataset
data_ubipark = {
    "Estacionamiento": ["Patio Olmos", "Nueva Córdoba", "Güemes", "Cerro de las Rosas"],
    "Hora_Pico": ["08:00-10:00", "18:00-20:00", "12:00-14:00", "17:00-19:00"],
    "Ocupación_Promedio (%)": [90, 85, 70, 78],
    "Tarifa_por_Hora ($)": [50, 40, 35, 45]
}
df_ubipark = pd.DataFrame(data_ubipark)

# 1. Filtrado: Estacionamientos con ocupación superior al 80%
ocupacion_alta = df_ubipark[df_ubipark["Ocupación_Promedio (%)"] > 80]
print("Estacionamientos con ocupación superior al 80%:")
print(ocupacion_alta)

# 2. Cálculo de ingresos: Crear columna Ingresos_Diarios (asumir 8 horas de operación)
df_ubipark['Ingresos_Diarios'] = df_ubipark['Tarifa_por_Hora ($)'] * 8
print("\nIngresos diarios:")
print(df_ubipark[['Estacionamiento', 'Ingresos_Diarios']])

# 3. Clasificación: Nivel de congestión
df_ubipark['Nivel_Congestión'] = df_ubipark['Ocupación_Promedio (%)'].apply(
    lambda x: "Alto" if x > 80 else ("Medio" if x > 60 else "Bajo")
)
print("\nNivel de congestión:")
print(df_ubipark[['Estacionamiento', 'Nivel_Congestión']])

# 4. Agregación: Tarifa promedio por hora de los estacionamientos con alta ocupación
alta_ocupacion = df_ubipark[df_ubipark['Ocupación_Promedio (%)'] > 80]
tarifa_promedio_alta_ocupacion = alta_ocupacion['Tarifa_por_Hora ($)'].mean()
print(f"\nTarifa promedio por hora de estacionamientos con alta ocupación: ${tarifa_promedio_alta_ocupacion:.2f}")

# 2. Planeta Modo Off: Uso de Celulares en Estudiantes
data_planeta = {
    "Estudiante": ["Ana", "Luis", "Marta", "Carlos", "Lucía"],
    "Horas_Diarias": [5, 8, 3, 6, 4],
    "Red_Social_Favorita": ["Instagram", "TikTok", "Twitter", "Facebook", "Instagram"],
    "Rendimiento_Académico": ["Alto", "Bajo", "Medio", "Alto", "Medio"]
}
df_planeta = pd.DataFrame(data_planeta)

# 1. Agregación: Promedio y desviación estándar de horas de uso
promedio_horas = df_planeta['Horas_Diarias'].mean()
desviacion_horas = df_planeta['Horas_Diarias'].std()
print(f"\nPromedio de horas de uso: {promedio_horas:.2f} horas")
print(f"Desviación estándar de horas de uso: {desviacion_horas:.2f} horas")

# 2. Filtrado: Estudiantes con rendimiento 'Alto' y menos de 5 horas de uso diario
alto_rendimiento = df_planeta[(df_planeta['Rendimiento_Académico'] == 'Alto') & (df_planeta['Horas_Diarias'] < 5)]
print("\nEstudiantes con rendimiento alto y menos de 5 horas de uso diario:")
print(alto_rendimiento)

# 3. Conteo: Cuántos estudiantes prefieren cada red social
conteo_redes = df_planeta['Red_Social_Favorita'].value_counts()
print("\nConteo de estudiantes por red social favorita:")
print(conteo_redes)

# 4. Nueva columna: Clasificación del uso del celular
df_planeta['Clasificación_Uso'] = df_planeta['Horas_Diarias'].apply(
    lambda x: "Excesivo" if x > 5 else ("Moderado" if x >= 3 else "Bajo")
)
print("\nClasificación del uso del celular:")
print(df_planeta[['Estudiante', 'Clasificación_Uso']])

# 3. Civic Report: Reportes de Infraestructura Urbana
data_civic = {
    "ID_Reporte": [1, 2, 3, 4],
    "Descripción": ["Bache en Av. Colón", "Alumbrado roto en Cerro", "Basura en Plaza San Martín", "Bache en Av. Vélez Sarsfield"],
    "Barrio": ["Centro", "Cerro de las Rosas", "Centro", "Alberdi"],
    "Prioridad": ["Alta", "Media", "Baja", "Alta"]
}
df_civic = pd.DataFrame(data_civic)

# 1. Extracción de texto: Crear columna Tipo extrayendo palabras clave
df_civic['Tipo'] = df_civic['Descripción'].str.extract(r'(Bache|Alumbrado|Basura)')
print("\nTipo de reporte:")
print(df_civic[['Descripción', 'Tipo']])

# 2. Filtrado: Reportes del "Centro" con prioridad "Alta"
reportes_centro_alta = df_civic[(df_civic['Barrio'] == 'Centro') & (df_civic['Prioridad'] == 'Alta')]
print("\nReportes en Centro con prioridad Alta:")
print(reportes_centro_alta)

# 3. Agregación: Contar reportes por tipo y barrio
conteo_reportes = df_civic.groupby(['Tipo', 'Barrio']).size().reset_index(name='Conteo')
print("\nConteo de reportes por tipo y barrio:")
print(conteo_reportes)

# 4. Nueva columna: Asignar código único combinando Barrio y ID_Reporte
df_civic['Código_Uni'] = df_civic['Barrio'] + '-' + df_civic['ID_Reporte'].astype(str)
print("\nCódigo único por barrio y reporte:")
print(df_civic[['Barrio', 'ID_Reporte', 'Código_Uni']])

# 4. SafeZone: Análisis de Incidentes en Barrios
data_safezone = {
    "Fecha": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"],
    "Tipo": ["Robo", "Asalto", "Robo", "Vandalismo"],
    "Barrio": ["Nueva Córdoba", "Centro", "Alberdi", "Nueva Córdoba"],
    "Hora": ["Noche", "Tarde", "Noche", "Mañana"]
}
df_safezone = pd.DataFrame(data_safezone)

# 1. Conteo: Frecuencia de incidentes por tipo y barrio
frecuencia_incidentes = df_safezone.groupby(['Tipo', 'Barrio']).size().reset_index(name='Frecuencia')
print("\nFrecuencia de incidentes por tipo y barrio:")
print(frecuencia_incidentes)

# 2. Filtrado: Incidentes ocurridos de noche en "Nueva Córdoba"
incidentes_noche_nueva_cordoba = df_safezone[(df_safezone['Hora'] == 'Noche') & (df_safezone['Barrio'] == 'Nueva Córdoba')]
print("\nIncidentes nocturnos en Nueva Córdoba:")
print(incidentes_noche_nueva_cordoba)

# 3. Agregación: Calcular porcentaje de incidentes por franja horaria
porcentaje_franja_horaria = df_safezone['Hora'].value_counts(normalize=True) * 100
print("\nPorcentaje de incidentes por franja horaria:")
print(porcentaje_franja_horaria)

# 4. Nueva columna: Clasificar la gravedad
df_safezone['Gravedad'] = df_safezone['Tipo'].apply(lambda x: "Crítico" if x == "Asalto" else "Moderado")
print("\nClasificación de la gravedad de los incidentes:")
print(df_safezone[['Tipo', 'Gravedad']])

# 5. Colillas Amigables: Contaminación por Colillas
data_colillas = {
    "Ubicación": ["Plaza San Martín", "Parque Sarmiento", "Paseo del Buen Pastor", "Plaza de la Intendencia"],
    "Colillas_m2": [15, 10, 20, 12],
    "Día": ["Lunes", "Miércoles", "Viernes", "Sábado"]
}
df_colillas = pd.DataFrame(data_colillas)

# 1. Cálculo: Estimar el total de colillas asumiendo un área de 500 m2 por ubicación
df_colillas['Total_Colillas'] = df_colillas['Colillas_m2'] * 500
print("\nEstimación total de colillas por ubicación:")
print(df_colillas[['Ubicación', 'Total_Colillas']])

# 2. Ordenamiento: Ordenar ubicaciones por contaminación descendente
df_colillas_sorted = df_colillas.sort_values(by='Colillas_m2', ascending=False)
print("\nUbicaciones ordenadas por contaminación:")
print(df_colillas_sorted[['Ubicación', 'Colillas_m2']])

# 3. Agregación: Promedio de colillas/m2 en fines de semana
fin_de_semana = df_colillas[df_colillas['Día'].isin(['Sábado', 'Domingo'])]
promedio_colillas_fds = fin_de_semana['Colillas_m2'].mean()
print(f"\nPromedio de colillas por m2 en fines de semana: {promedio_colillas_fds:.2f}")

# 4. Nueva columna: Clasificar la contaminación
df_colillas['Clasificación_Contaminación'] = df_colillas['Colillas_m2'].apply(
    lambda x: "Alta" if x > 15 else ("Media" if x >= 10 else "Baja")
)
print("\nClasificación de contaminación por colillas:")
print(df_colillas[['Ubicación', 'Clasificación_Contaminación']])
