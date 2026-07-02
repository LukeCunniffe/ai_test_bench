import json

class Config:
    def __init__(self, path="config.json"):
        with open(path, "r") as file:
            self.data = json.load(file)

    @property
    def app_name(self):
        return self.data["application_name"]

    @property
    def version(self):
        return self.data["version"]

    @property
    def camera_index(self):
        return self.data["camera"]["index"]

    @property
    def model_path(self):
        return self.data["ai"]["model"]

    @property
    def database_path(self):
        return self.data["database"]["path"]
