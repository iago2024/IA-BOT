# config.py
import threading
import queue
from datetime import datetime

# --- Configurações Imutáveis (Constantes do Sistema) ---
INTERVALO = "1m"
COOLDOWN_MINUTOS = 1
BOLLINGER_PERIODO = 20

# Lista de todos os ativos que podem ser escolhidos
TODOS_OS_ATIVOS_DISPONIVEIS = ["btcusdt", "ethusdt", "bnbusdt", "memeusdt", "solusdt", "adausdt"]

# --- Configurações Padrão para Novos Usuários ---
DEFAULT_CONFIG = {
    # --- Seção de Telegram do Usuário ---
    "TELEGRAM_TOKEN": "",
    "TELEGRAM_CHAT_ID": "",
    
    # --- Estratégias Ativas (PADRÃO: TUDO FALSE/DESLIGADO) ---
    "USAR_ESTRATEGIA_BOLLINGER_RT": False,
    "USAR_ESTRATEGIA_RSI": False,
    "USAR_ESTRATEGIA_SR": False,
    "USAR_ESTRATEGIA_T5": False,
    "USAR_ESTRATEGIA_MHI": False,
    "USAR_ESTRATEGIA_P3V": False, 
    "USAR_ESTRATEGIA_BREAKOUT_SMA": False,
    "USAR_ESTRATEGIA_SPIKE_VOLUME": False,
    "USAR_ESTRATEGIA_MOMENTUM_3": False,
    
    # --- Parâmetros Bollinger ---
    "BOLLINGER_STD_DEV": 2.7,
    "BOLLINGER_OFFSET_PERCENT": 0.0001,
    
    # --- Parâmetros RSI ---
    "RSI_PERIODO": 14,
    "RSI_LIMITE_SUPERIOR": 70,
    "RSI_LIMITE_INFERIOR": 30,
    "RSI_USE_MACD_FILTER": False,
    
    # --- Parâmetros S/R ---
    "SR_PERIODO": 120,
    "SR_TOQUES_NECESSARIOS": 3, 
    "SR_TOLERANCIA_PERCENT": 0.0005,
    "SR_DISTANCIA_MIN_TOQUES": 5,

    # --- Parâmetros MHI ---
    "MHI_USE_TREND_FILTER": True,
    "MHI_TREND_PERIODO": 100,
    "CONFIANCA_MHI": 0.88,

    # --- Parâmetros T5 ---
    "CONFIANCA_T5": 0.92,
    "T5_PAVIO_MIN_RATIO": 2.0,
    
    # --- Parâmetros P3V ---
    "P3V_VWMA_PERIODO": 30,
    "CONFIANCA_P3V": 0.88,

    # --- Parâmetros Gerenciamento ---
    "VALOR_ENTRADA_BASE": 10.0,

    # --- Confiança (Usado pelo Bot Manager) ---
    "CONFIANCA_BOLLINGER_RT": 0.94,
    "CONFIANCA_RSI": 0.90,
    "CONFIANCA_SR": 0.96,
    "CONFIANCA_BREAKOUT_SMA": 0.80,
    "CONFIANCA_SPIKE_VOLUME": 0.85,
    "CONFIANCA_MOMENTUM_3": 0.88,
    
    # --- Parâmetros Breakout SMA ---
    "BREAKOUT_SMA_CURTA": 5,
    "BREAKOUT_SMA_LONGA": 7,
    "BREAKOUT_SMA_BODY_MULT": 2.0,
    "BREAKOUT_SMA_AVG_PERIOD": 20,

    # --- Parâmetros Spike de Volume ---
    "SPIKE_VOLUME_PERIODO_MEDIA": 20,
    "SPIKE_VOLUME_MULTIPLICADOR": 1.5,
    "SPIKE_REVERSAO_PAVIO_RATIO": 0.5,
    "SPIKE_REVERSAO_CORPO_RATIO": 0.3,
    
    # --- Parâmetros Momentum 3 ---
    "MOMENTUM_3_CORPO_FORTE_RATIO": 0.6, 
    "MOMENTUM_3_CORPO_FRACO_RATIO": 0.4, 
    
    "ATIVOS": []
}

# --- Lista de Usuários ---
USUARIOS = {
    "traderbr": "ebinex",
    "rodrigo": "rodrigo",
    "cliente_c": "outrasenha"
}