# PROYECTO: BASE DE DATOS DE PALABRAS CLAVE — BIOLOGÍA BOTÁNICA  

### Asignatura: Programación Lógica Funcional  
### Alumno: Gabriel Enrique Lugo López  
### Número de control: 22760840  
### Tema asignado: Biología – Botánica  
### Fecha de entrega: Noviembre 2025  

##  Descripción del proyecto  
Este proyecto consiste en la creación de una **base de datos local en SQLite** que almacena al menos ** 60 palabras clave relacionadas con el tema de Biología – Botánica**.  
Cada palabra incluye su **porcentaje de identidad con el tema** y una lista de **sinónimos**.  
La base de datos se genera y gestiona automáticamente mediante un **script en Python** ejecutado en **Visual Studio Code**, sin necesidad de servidores externos como PostgreSQL

##  Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instalados los siguientes componentes:

- **Python 3.10 o superior**  
- **SQLite 3.45.3  
- **Editor de texto visual studio code**

- ##  Estructura del Proyecto

- BD_Biología_Botanica/

biologia_botanica.py # Script principal en Python

biologia_botanica.db # Base de datos generada (se crea automáticamente)

README.md # Instrucciones del proyecto

## Ejecución del Proyecto

Sigue estos pasos para ejecutar el proyecto correctamente:

###  Abrir la carpeta del proyecto

1. Presiona `Win + R`, escribe `cmd` y presiona **Enter** para abrir la consola.  
2. Escribe el siguiente comando para ir a la carpeta del proyecto:
3. cd "C:\Users\garoi\OneDrive\Desktop\SCHOOL\7to SEMESTRE\2.- PROGRAMACION LOGICA FUNCIONAL\BD_Biología_Botanica"
4. python Biologia_botanica_bd.py

   
### Forma como te aparece.

✅ Base de datos actualizada con nuevas palabras clave.
(1, 'fotosíntesis', 98.5, 'producción de energía, clorofila, luz solar')
(2, 'célula vegetal', 97.0, 'citoplasma, núcleo, pared celular')
(3, 'clorofila', 96.2, 'pigmento verde, fotosistema, energía solar')
(4, 'flor', 94.7, 'pétalos, reproducción, planta')
(5, 'semilla', 93.5, 'germinación, embrión, fruto')
(6, 'raíz', 92.8, 'absorción, anclaje, rizoma')
(7, 'tallo', 91.6, 'soporte, xilema, floema')
(8, 'hoja', 90.9, 'estoma, cloroplasto, fotosíntesis')
(9, 'polinización', 89.8, 'abeja, reproducción, floración')
(10, 'germinación', 88.6, 'crecimiento, semilla, humedad')
(11, 'planta', 87.4, 'organismo vegetal, flora')
(12, 'ecosistema', 86.2, 'hábitat, biodiversidad, bioma')
(13, 'botánica', 85.0, 'biología vegetal, taxonomía')
(14, 'floración', 84.3, 'estación, primavera, reproducción')
(15, 'xilema', 83.0, 'transporte, savia, conducción')
(16, 'floema', 82.7, 'nutrientes, azúcares, transporte')
(17, 'antera', 81.5, 'polen, estambre, flor')
(18, 'estambre', 81.0, 'polen, flor, reproducción masculina')
(19, 'pistilo', 80.6, 'óvulo, estigma, ovario')
(20, 'polen', 80.1, 'grano, fertilización, flor')
(21, 'óvulo', 79.8, 'ovario, gameto, reproducción')
(22, 'mitosis', 79.2, 'división celular, cromosomas, células hijas')
(23, 'meiosis', 78.9, 'reproducción sexual, gametos, cromosomas')
(24, 'citoplasma', 78.0, 'orgánulos, célula, membrana')
(25, 'ADN', 77.6, 'ácido desoxirribonucleico, genética, cromosomas')
(26, 'ARN', 77.1, 'ácido ribonucleico, síntesis de proteínas, transcripción')
(27, 'genética', 76.8, 'herencia, genes, ADN')
(28, 'mutación', 75.9, 'variación, ADN, evolución')
(29, 'evolución', 75.2, 'selección natural, adaptación, especies')
(30, 'reino vegetal', 74.8, 'plantas, flora, fotosíntesis')
(31, 'taxonomía', 74.0, 'clasificación, especies, biología')
(32, 'bioma', 73.4, 'ecosistema, clima, vegetación')
(33, 'biodiversidad', 73.1, 'variedad, especies, ecosistema')
(34, 'simbiogénesis', 72.6, 'evolución, endosimbiosis, mitocondria')
(35, 'endosimbiosis', 72.2, 'mitocondria, cloroplasto, célula eucariota')
(36, 'autótrofos', 71.8, 'fotosíntesis, energía solar, carbono')
(37, 'heterótrofos', 71.4, 'nutrición, organismos, energía')
(38, 'micorriza', 70.9, 'hongo, raíz, simbiosis')
(39, 'hongos', 70.5, 'micelio, esporas, descomposición')
(40, 'algas', 70.1, 'acuáticas, clorofila, fotosíntesis')
(41, 'morfología vegetal', 69.7, 'estructura, órganos, planta')
(42, 'fisiología vegetal', 69.3, 'procesos vitales, metabolismo, hormonas')
(43, 'transpiración', 69.0, 'agua, hojas, evaporación')
(44, 'estoma', 68.6, 'intercambio gaseoso, hoja, cloroplasto')
(45, 'cloroplasto', 68.3, 'orgánulo, fotosíntesis, energía solar')
(46, 'savias', 68.0, 'nutrientes, transporte, floema')
(47, 'adaptación', 67.5, 'supervivencia, evolución, entorno')
(48, 'descomposición', 67.0, 'nutrientes, reciclaje, hongos')
(49, 'reproducción vegetal', 66.5, 'sexual, asexual, flores')
(50, 'reproducción asexual', 66.0, 'brotación, estolones, esquejes')
(51, 'reproducción sexual', 65.5, 'polinización, fecundación, semillas')



