#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BBοomer - Бомбер на Python
Основной модуль приложения
"""

import os
import sys
import json
import time
from datetime import datetime
from bomber import Bomber
from config import Config
from logger import Logger


def show_menu():
    """Отображение главного меню"""
    print("\n===== BBοomer - Бомбер =====")
    print("1. Запустить атаку")
    print("2. Настройки атаки")
    print("3. Просмотр логов")
    print("4. Остановить атаку")
    print("5. Выход")
    print("=" * 30)


def load_config():
    """Загрузка конфигурации"""
    try:
        with open("config/settings.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Файл конфигурации не найден. Создаю новый...")
        default_config = {
            "target_phone": "",
            "message_count": 100,
            "services": ["service1", "service2", "service3"],
            "cooldown": 0,  # Без КД
            "log_level": "detailed"
        }
        with open("config/settings.json", "w") as f:
            json.dump(default_config, f, indent=4)
        return default_config


def main():
    """Главная функция приложения"""
    print("Добро пожаловать в BBοomer - бомбер на Python!")
    
    # Загрузка конфигурации
    config_data = load_config()
    config = Config(config_data)
    
    # Инициализация логгера
    logger = Logger("logs/bomber.log")
    
    # Инициализация бомбера
    bomber = Bomber(config, logger)
    
    while True:
        show_menu()
        choice = input("Выберите действие (1-5): ").strip()
        
        if choice == "1":
            target_phone = input("Введите номер телефона жертвы: ").strip()
            if target_phone:
                message_count = input("Введите количество сообщений (по умолчанию 100): ").strip()
                try:
                    message_count = int(message_count) if message_count else 100
                except ValueError:
                    message_count = 100
                
                print(f"Запуск атаки на {target_phone} с отправкой {message_count} сообщений...")
                bomber.start_attack(target_phone, message_count)
            else:
                print("Неверный номер телефона")
        
        elif choice == "2":
            print("Настройки атаки...")
            # Здесь будет код для настройки
            print("Функция настройки будет реализована позже")
        
        elif choice == "3":
            print("Просмотр логов...")
            logger.show_logs()
        
        elif choice == "4":
            print("Остановка атаки...")
            bomber.stop_attack()
        
        elif choice == "5":
            print("Спасибо за использование BBοomer. До свидания!")
            sys.exit(0)
        
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()