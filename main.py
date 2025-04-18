from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

def esperar_y_encontrar_elemento(driver, xpath, tiempo=30):
    """Función auxiliar para esperar y encontrar un elemento"""
    wait = WebDriverWait(driver, tiempo)
    return wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

def verificar_sesion_whatsapp(driver):
    """Verifica que la sesión de WhatsApp esté activa buscando elementos clave"""
    try:
        esperar_y_encontrar_elemento(driver, "//div[@id='side']", 10)
        return True
    except:
        return False

def esperar_chat_cargado(driver):
    """Espera a que el chat esté completamente cargado"""
    try:
        # Espera a que aparezca cualquier elemento del chat
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'chat')]"))
        )
        return True
    except:
        return False

try:
    # Inicializa el driver de Chrome con webdriver-manager
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Abre WhatsApp Web
    print("Abriendo WhatsApp Web...")
    driver.get("https://web.whatsapp.com/")
    
    print("Esperando a que escanees el código QR...")
    input("Presiona Enter después de escanear el código QR y ver que WhatsApp Web está completamente cargado...")
    print("Verificando que WhatsApp Web esté cargado...")
    
    # Espera adicional para asegurar que WhatsApp Web está completamente cargado
    time.sleep(10)
    
    # Verifica que la sesión esté activa
    if not verificar_sesion_whatsapp(driver):
        raise Exception("No se pudo verificar la sesión de WhatsApp Web. Por favor, intenta de nuevo.")
    
    print("Sesión de WhatsApp Web verificada correctamente.")
    
    # Lista de contactos con nombre y número (con el código de país)
    contacts = [
        {"nombre": "Nombre1", "numero": "000000"}
        #añadir nombres y numeros aquí
    ]

    # Plantilla del mensaje
    mensaje_template = (
       #añadir mensaje aquí
    )

    # Envía el mensaje a cada contacto
    for contact in contacts:
        try:
            print(f"\nIntentando enviar mensaje a {contact['nombre']} ({contact['numero']})...")
            mensaje = mensaje_template.format(nombre=contact["nombre"])
            
            # Verifica la sesión antes de cada mensaje
            if not verificar_sesion_whatsapp(driver):
                print("Se perdió la sesión de WhatsApp Web. Reintentando...")
                driver.get("https://web.whatsapp.com/")
                time.sleep(30)
                if not verificar_sesion_whatsapp(driver):
                    raise Exception("No se pudo recuperar la sesión de WhatsApp Web")
            
            # Construye la URL para abrir el chat con el número específico
            url = f"https://web.whatsapp.com/send?phone={contact['numero']}"
            print(f"Abriendo chat: {url}")
            driver.get(url)
            
            print("Esperando a que cargue el chat...")
            time.sleep(15)  # Espera fija inicial
            
            # Verifica si hay mensaje de error de número inválido
            try:
                error_xpath = "//*[contains(text(), 'inválido') or contains(text(), 'no encontrado')]"
                error_message = esperar_y_encontrar_elemento(driver, error_xpath, 10)
                print(f"Error: Número no válido o usuario no encontrado para {contact['nombre']}")
                continue
            except TimeoutException:
                pass
            
            print("Buscando el cuadro de texto del chat...")
            input_box = None
            
            # Intenta encontrar el cuadro de texto usando diferentes métodos
            try:
                # Método 1: Buscar por el placeholder del mensaje
                input_box = driver.find_element(By.XPATH, "//div[contains(@title, 'Escribe un mensaje')]")
            except:
                try:
                    # Método 2: Buscar por la clase del editor de mensajes
                    input_box = driver.find_element(By.CSS_SELECTOR, "div.copyable-text.selectable-text[contenteditable='true']")
                except:
                    try:
                        # Método 3: Buscar por el área de composición de mensajes
                        input_box = driver.find_element(By.XPATH, "//footer//div[@contenteditable='true']")
                    except:
                        try:
                            # Método 4: Buscar por el rol de textbox
                            input_box = driver.find_element(By.CSS_SELECTOR, "div[role='textbox']")
                        except:
                            raise Exception("No se pudo encontrar el cuadro de texto del chat")
            
            if not input_box:
                raise Exception("No se pudo encontrar el cuadro de texto del chat")
            
            print("Escribiendo el mensaje...")
            # Intenta dar foco al cuadro de texto
            try:
                input_box.click()
            except:
                driver.execute_script("arguments[0].focus();", input_box)
            
            time.sleep(2)
            
            # Escribe el mensaje línea por línea
            for line in mensaje.split('\n'):
                input_box.send_keys(line)
                time.sleep(0.5)
                input_box.send_keys(Keys.SHIFT + Keys.ENTER)
                time.sleep(0.5)
            
            time.sleep(2)
            
            print("Enviando mensaje...")
            input_box.send_keys(Keys.ENTER)
            
            # Espera a que el mensaje se envíe verificando el ícono de enviado
            try:
                check_mark = esperar_y_encontrar_elemento(driver, "//span[@data-icon='msg-check' or @data-icon='msg-dblcheck']", 10)
                print(f"✓ Mensaje enviado exitosamente a {contact['nombre']}")
            except:
                print(f"⚠ No se pudo confirmar el envío del mensaje a {contact['nombre']}")
            
            time.sleep(10)  # Espera entre mensajes
            
        except Exception as e:
            print(f"❌ Error al enviar mensaje a {contact['nombre']}: {str(e)}")
            print("Esperando 20 segundos antes de continuar...")
            time.sleep(20)
            continue

except Exception as e:
    print(f"Error general del programa: {str(e)}")
finally:
    print("\nCerrando el navegador...")
    driver.quit()
    print("Programa finalizado.")
