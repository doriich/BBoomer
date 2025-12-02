#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль управления сервисами BBοomer
Управляет различными сервисами для отправки SMS/звонков
"""

import random
import requests
from datetime import datetime


class BaseService:
    """Базовый класс для сервисов"""
    
    def __init__(self, name):
        self.name = name
        self.session = requests.Session()
    
    def send_message(self, phone_number):
        """Отправка сообщения (должен быть переопределен в подклассах)"""
        raise NotImplementedError("Метод send_message должен быть реализован в подклассе")
    
    def make_call(self, phone_number):
        """Осуществление звонка (должен быть переопределен в подклассах)"""
        raise NotImplementedError("Метод make_call должен быть реализован в подклассе")


class Service1(BaseService):
    """Пример первого сервиса"""
    
    def __init__(self):
        super().__init__("Service1")
    
    def send_message(self, phone_number):
        """Отправка сообщения через Service1"""
        try:
            # Симуляция отправки сообщения
            # В реальной реализации здесь будет API вызов к сервису
            print(f"[Service1] Отправка SMS на {phone_number}")
            # Имитация успешной отправки
            return True
        except Exception as e:
            print(f"[Service1] Ошибка отправки SMS: {e}")
            return False
    
    def make_call(self, phone_number):
        """Осуществление звонка через Service1"""
        try:
            # Симуляция звонка
            # В реальной реализации здесь будет API вызов к сервису
            print(f"[Service1] Осуществление звонка на {phone_number}")
            # Имитация успешного звонка
            return True
        except Exception as e:
            print(f"[Service1] Ошибка осуществления звонка: {e}")
            return False


class Service2(BaseService):
    """Пример второго сервиса"""
    
    def __init__(self):
        super().__init__("Service2")
    
    def send_message(self, phone_number):
        """Отправка сообщения через Service2"""
        try:
            # Симуляция отправки сообщения
            print(f"[Service2] Отправка SMS на {phone_number}")
            # Имитация успешной отправки
            return True
        except Exception as e:
            print(f"[Service2] Ошибка отправки SMS: {e}")
            return False
    
    def make_call(self, phone_number):
        """Осуществление звонка через Service2"""
        try:
            # Симуляция звонка
            print(f"[Service2] Осуществление звонка на {phone_number}")
            # Имитация успешного звонка
            return True
        except Exception as e:
            print(f"[Service2] Ошибка осуществления звонка: {e}")
            return False


class Service3(BaseService):
    """Пример третьего сервиса"""
    
    def __init__(self):
        super().__init__("Service3")
    
    def send_message(self, phone_number):
        """Отправка сообщения через Service3"""
        try:
            # Симуляция отправки сообщения
            print(f"[Service3] Отправка SMS на {phone_number}")
            # Имитация успешной отправки
            return True
        except Exception as e:
            print(f"[Service3] Ошибка отправки SMS: {e}")
            return False
    
    def make_call(self, phone_number):
        """Осуществление звонка через Service3"""
        try:
            # Симуляция звонка
            print(f"[Service3] Осуществление звонка на {phone_number}")
            # Имитация успешного звонка
            return True
        except Exception as e:
            print(f"[Service3] Ошибка осуществления звонка: {e}")
            return False


class ServiceManager:
    """Класс управления сервисами"""
    
    def __init__(self, config):
        self.config = config
        self.services = []
        self.initialize_services()
    
    def initialize_services(self):
        """Инициализация доступных сервисов"""
        # Создаем экземпляры всех доступных сервисов
        self.services = [
            Service1(),
            Service2(),
            Service3()
        ]
        
        # Фильтруем по настройкам конфигурации
        enabled_services = []
        for service in self.services:
            if service.name in self.config.services:
                enabled_services.append(service)
        
        self.services = enabled_services
    
    def get_random_service(self):
        """Получение случайного доступного сервиса"""
        if not self.services:
            return None
        return random.choice(self.services)
    
    def get_service_by_name(self, name):
        """Получение сервиса по имени"""
        for service in self.services:
            if service.name == name:
                return service
        return None
    
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
    
    def get_services_list(self):
        """Получение списка имен сервисов"""
        return [service.name for service in self.services]