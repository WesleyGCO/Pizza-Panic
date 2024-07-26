import json

def load_settings():
    try:
        with open('settings.json') as f:
            settings = json.load(f)
            return settings
    except FileNotFoundError:
        print("Arquivo settings.json não encontrado. Usando configurações padrão.")
        return {
            # ... suas configurações padrão aqui
        }