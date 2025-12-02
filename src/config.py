#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль конфигурации BBοomer
Управление настройками бомбера
"""

import json


class Config:
    """Класс конфигурации"""
    
    def __init__(self, config_data):
        self.target_phone = config_data.get("target_phone", "")
        self.message_count = config_data.get("message_count", 100)
        self.services = config_data.get("services", ["service1", "service2", "service3"])
        self.cooldown = config_data.get("cooldown", 0)  # Без КД по умолчанию
        self.log_level = config_data.get("log_level", "detailed")
    
    def set_target_phone(self, phone):
        """Установка номера телефона цели"""
        self.target_phone = phone
        return True
    
    def set_message_count(self, count):
        """Установка количества сообщений"""
        if count > 0:
            self.message_count = count
            return True
        return False
    
    def add_service(self, service):
        """Добавление сервиса"""
        if service not in self.services:
            self.services.append(service)
            return True
        return False
    
    def remove_service(self, service):
        """Удаление сервиса"""
        if service in self.services:
            self.services.remove(service)
            return True
        return False
    
    def set_cooldown(self, cooldown):
        """Установка задержки между отправками"""
        if cooldown >= 0:
            self.cooldown = cooldown
            return True
        return False
    
    def set_log_level(self, level):
        """Установка уровня логирования"""
        valid_levels = ["basic", "detailed", "debug"]
        if level in valid_levels:
            self.log_level = level
            return True
        return False
    
    def save_to_file(self, filepath="config/settings.json"):
        """Сохранение конфигурации в файл"""
        config_data = {
            "target_phone": self.target_phone,
            "message_count": self.message_count,
            "services": self.services,
            "cooldown": self.cooldown,
            "log_level": self.log_level
        }
        
        try:
            with open(filepath, "w") as f:
                json.dump(config_data, f, indent=4)
            return True
        except Exception as e:
            print(f"Ошибка сохранения конфигурации: {e}")
            return False