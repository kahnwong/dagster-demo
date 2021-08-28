# Imitate Dagster Logger
class Logger:
    def info(self, text: str):
        print("[INFO] " + text)

    def warn(self, text: str):
        print("[WARN] " + text)

    def error(self, text: str):
        print("[ERROR] " + text)
