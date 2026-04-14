# generacion-automatica_queries_dimtiempo_Python

Descripción: 
Este proyecto genera automáticamente registros para una tabla de dimensión de tiempo (DimTime), utilizada en modelos de Data Warehouse para análisis de datos.

Problema: 
En entornos de Business Intelligence, la construcción de una dimensión de tiempo es esencial para el análisis histórico. 
Sin embargo, su generación manual es repetitiva, propensa a errores y difícil de mantener.

Solución: 
Se desarrolló un script en Python que: 
-Genera registros diarios para un mes completo 
-Calcula automáticamente: 
-Año, mes, día 
-Semana del año 
-Trimestre 
-Día del año y de la semana 
-Maneja lógica personalizada de calendario (EMPRESA) 
-Genera instrucciones SQL listas para insertar en base de datos

Tecnologías utilizadas: 
-Python 
-datetime 
-calendar 
-SQL (generación de queries)

Cómo usar: 
Configurar los parámetros iniciales en el script: 
-daniosemana 
-nsemanaEMPRESA 
-ndiaAnio 
-ndiaSeman 
-inicioSemana_Rt 
-finSemana_Rt 
-n = 3 
-m = 3 
-dia_reinicio_EMPRESA 
-anioEMPRESA 
-anioid 
Ejecutar el script: 
python main.py 
El script generará múltiples sentencias INSERT INTO listas para ejecutar en base de datos.

Resultados: 
-Automatización de generación de calendario analítico 
-Reducción de errores manuales 
-Estandarización de estructura de fechas para análisis

🔒 Nota: 
Los parámetros y estructuras han sido adaptados para fines demostrativos y no contienen información confidencial.

🎯 Próximas mejoras: 
-Exportación directa a base de datos 
-Generación para múltiples años 
-Configuración dinámica sin valores manuales 
-Integración con ETL pipelines

👨‍💻 Autor: 
Mario Blanco Abregú
