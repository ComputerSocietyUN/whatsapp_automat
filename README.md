|             |          Grouping           ||
First Header  | Second Header | Third Header |
 ------------ | :-----------: | -----------: |
Content       |          *Long Cell*        ||
Content       |   **Cell**    |         Cell |

New section   |     More      |         Data |
And more      | With an escaped '\|'         ||  

# WhatsApp Message Sender

Un script de Python que automatiza el envío de mensajes a través de WhatsApp Web utilizando Selenium.

## 🚀 Descripción

Este programa permite enviar mensajes personalizados a múltiples contactos de WhatsApp de forma automatizada. Es especialmente útil para:
- Envío de mensajes de bienvenida
- Notificaciones grupales
- Campañas de comunicación
- Recordatorios programados

## 📋 Requisitos Previos

- Python 3.7 o superior
- Google Chrome instalado
- Conexión a Internet
- Cuenta de WhatsApp activa

## 📦 Dependencias

```bash
pip install selenium webdriver-manager
```

## 🛠️ Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/ComputerSocietyUN/whatsapp_automat
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Configura los contactos en el archivo `automat_cs.py`:
```python
contacts = [
    {"nombre": "Nombre1", "numero": "000000"},
    {"nombre": "Nombre2", "numero": "000000"},
    # Añade más contactos según necesites
]
```

4. Personaliza el mensaje:
```python
mensaje_template = (
    "Tu mensaje personalizado aquí {nombre}"
)
```

## 🎯 Uso

1. Ejecuta el script:
```bash
python automat_cs.py
```

2. Escanea el código QR cuando se abra WhatsApp Web
3. Espera a que se complete el proceso de envío

## ⚠️ Consideraciones Importantes

- Los números deben incluir el código de país sin el símbolo '+'
- Asegúrate de que los números sean válidos
- No uses el script para spam o mensajes no deseados
- Respeta las políticas de WhatsApp

## 🤝 Contribuciones

Este proyecto es open source y acepta contribuciones. Algunas áreas donde puedes ayudar:

### 1. Mejoras en la Detección de Elementos
- Actualizar los selectores XPath y CSS
- Mejorar la detección del cuadro de texto
- Agregar más métodos de verificación

### 2. Nuevas Funcionalidades
- Programación de mensajes
- Plantillas de mensajes múltiples
- Integración con bases de datos
- Interfaz gráfica

### 3. Optimizaciones
- Mejorar los tiempos de espera
- Reducir la dependencia de sleep()
- Implementar reintentos automáticos

### 4. Documentación
- Mejorar la documentación del código
- Agregar ejemplos de uso
- Crear guías de troubleshooting

## 🐛 Reporte de Errores

Si encuentras un error, por favor:
1. Verifica que estás usando la última versión
2. Revisa los logs de error
3. Abre un issue con:
   - Descripción del error
   - Pasos para reproducir
   - Capturas de pantalla (si aplica)

## 📝 Guía de Contribución

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 🔄 Mantenimiento

El código necesita mantenimiento regular debido a:
- Cambios en la interfaz de WhatsApp Web
- Actualizaciones de Selenium
- Nuevas versiones de Chrome

### Áreas que Necesitan Atención Constante:

1. **Selectores de Elementos**
```python
# Ejemplo de selectores que pueden necesitar actualización
"//div[contains(@title, 'Escribe un mensaje')]"
"div.copyable-text.selectable-text[contenteditable='true']"
```

2. **Tiempos de Espera**
```python
# Ajusta estos valores según la velocidad de tu conexión
time.sleep(15)  # Tiempo de carga inicial
time.sleep(2)   # Entre acciones
```

3. **Manejo de Errores**
```python
try:
    # Código que puede fallar
except Exception as e:
    # Manejo de errores
```

## 📜 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para detalles.

## ✨ Agradecimientos

- Selenium WebDriver
- WhatsApp Web
- La comunidad de Python
- Todos los contribuidores
- 
---

Hecho con ❤️ por Computer Society
