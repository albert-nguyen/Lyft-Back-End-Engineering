from abc import ABC, abstractmethod


class Serviceable(ABC):
    def needs_service(self):
        pass
