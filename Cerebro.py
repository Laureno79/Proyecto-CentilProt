import os
import requests
import json
from datetime import datetime

class Cerebro:
    """
    Núcleo central del Proyecto CentilProt.
    Este módulo gestiona la lógica de detección y protocolos de defensa automatizada.
    """

    def __init__(self):
        # Configuración de identidad del sistema
        self.proyecto = "CentilProt"
        self.fase = "Programa Piloto"
        
        # Datos del bot proporcionados por el usuario
        self.bot_name = "centinela"
        self.chat_id = "6190256693"
        
        # El token debe manejarse como variable de entorno por seguridad en GitHub
        self.bot_token = os.getenv("TELEGRAM_TOKEN", "TU_TOKEN_AQUI")
        self.api_url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

    def registrar_evento(self, nivel, mensaje):
        """Genera un log de auditoría para el monitoreo de protección."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{nivel}] {mensaje}"
        print(log_entry)
        return log_entry

    def enviar_alerta_telegram(self, texto):
        """Establece comunicación directa con el bot centinela para reportar anomalías."""
        payload = {
            "chat_id": self.chat_id,
            "text": f"🛡️ [{self.proyecto} - Alerta]: {texto}",
            "parse_mode": "Markdown"
        }
        try:
            response = requests.post(self.api_url, data=payload)
            return response.status_code == 200
        except Exception as e:
            self.registrar_evento("ERROR", f"Fallo en comunicación con centinela: {e}")
            return False

    def motor_deteccion_ia(self, flujo_datos):
        """
        Analiza patrones de datos buscando anomalías.
        Implementación preparada para agentes de IA (LangGraph / RAG).
        """
        self.registrar_evento("INFO", "Analizando flujo de datos para detección de amenazas...")
        
        # Simulación de lógica defensiva:
        # Aquí se integraría el agente que analiza si el comportamiento es malicioso
        amenaza_detectada = False 
        
        if amenaza_detectada:
            self.ejecutar_protocolo_defensa("Intento de acceso no autorizado detectado.")
        else:
            self.registrar_evento("OK", "Entorno seguro. No se detectaron anomalías.")

    def ejecutar_protocolo_defensa(self, motivo):
        """Activa las capas de protección del sistema."""
        self.registrar_evento("CRITICAL", f"ACTIVANDO DEFENSA: {motivo}")
        alerta = f"Protocolo de defensa activado. Motivo: {motivo}. Revisando integridad de catastro y sistemas."
        self.enviar_alerta_telegram(alerta)

    def iniciar_sistema(self):
        """Arranque del programa piloto en el equipo local."""
        print(f"--- {self.proyecto} : El Cerebro está activo ---")
        self.registrar_evento("SISTEMA", "Inicio de monitoreo en modo protección.")
        
        # Ejemplo de ejecución inicial
        self.motor_deteccion_ia({"origen": "local_pc", "estado": "monitoreo"})

if __name__ == "__main__":
    # Inicialización del núcleo
    cerebro = Cerebro()
    cerebro.iniciar_sistema()