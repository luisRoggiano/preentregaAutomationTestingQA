🎓 Pre-Entrega: Framework de Automatización Web con Pytest
Este proyecto es la pre-entrega del Curso de Automation Testing y establece un framework de pruebas automatizadas End-to-End (E2E) para validar los flujos críticos de usuario en la plataforma SauceDemo.

El framework está desarrollado en Python, utilizando Selenium WebDriver para la interacción con el navegador y Pytest como motor de pruebas.

📜 Evolución y Características Clave
El historial de commits documenta la construcción progresiva del framework a través de tres fases principales, reflejando una clara progresión desde la estructura inicial hasta la entrega final con evidencia de pruebas:

1. ⚙️ Base y Estructura (Oct 16, 2025)
Configuración Inicial: Se establecieron los cimientos del proyecto con el Initial commit y el commit Estructura.

Archivos Base: Se configuró la jerarquía de carpetas necesaria para separar la lógica de utilidades (utils/), las páginas web (page/) y los scripts de prueba (test/).

2. 🧪 Desarrollo de Casos de Prueba (Oct 18, 2025 - Commit [PRE-ENTREGA])
Esta fase fue crítica para el desarrollo del framework funcional:

Implementación de Tests: Se introdujo el archivo test/test_saucedemo.py, que contiene los escenarios de prueba para la aplicación (Login, Catálogo, Carrito).

Modularidad de Páginas: Se comenzó a estructurar la interacción con la aplicación, incluyendo una página inicial de Login (page/login_page.py), indicando una intención de utilizar o explorar el patrón Page Object Model (POM).

Funciones de Ayuda: Se modificó utils/helpers.py para incluir la lógica reutilizable (ej. inicialización del driver y las acciones de login).

3. 📸 Gestión de Evidencia (Oct 18, 2025 - Commit [AutomationQA])
El commit final agregó la característica más robusta y el requerimiento clave de la pre-entrega:

Implementación de Screenshots: Se integró la función take_screenshot en utils/helpers.py y se realizaron las llamadas a esta función en test/test_saucedemo.py.

Generación de Evidencia: La ejecución de las pruebas ahora genera automáticamente la evidencia visual en la carpeta test/screenshots/.

Trazabilidad: Los nombres de los archivos de captura, como carritoAddOk_2025_10_18_13-29-26.png y loginOk_2025_10_18_13-29-26.png, demuestran el uso de timestamp único y un formato descriptivo para una trazabilidad clara del estado del sistema tras cada paso clave.
Detalle Tests PASSED
<img width="1369" height="347" alt="image" src="https://github.com/user-attachments/assets/9abf5ffe-21c4-42b3-ae9a-4913899ed9c5" />


