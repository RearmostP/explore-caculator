import json, os

CONFIG_PATH = "config.json"

class AppManager:
    _instance = None

    @staticmethod
    def instance():
        if not AppManager._instance:
            AppManager._instance = AppManager()
        return AppManager._instance

    def __init__(self):
        self.config = self._load_config()
        self.lang_data = self._load_language(self.config["language"])

    # === ניהול קובץ קונפיג ===
    def _load_config(self):
        if not os.path.exists(CONFIG_PATH):
            config = {"language": "he", "theme": "dark"}
            self.save_config(config)
            return config
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_config(self, new_cfg):
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(new_cfg, f, ensure_ascii=False, indent=2)
        self.config = new_cfg
        self.lang_data = self._load_language(new_cfg["language"])

    # === טעינת שפה ===
    def _load_language(self, lang_code):
        path = os.path.join("languages", f"{lang_code}.json")
        if not os.path.exists(path):
            path = os.path.join("languages", "he.json")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    # === גישה פשוטה לשפה ולעיצוב ===
    def get_theme(self):
        return self.config["theme"]

    def get_language(self):
        return self.lang_data
