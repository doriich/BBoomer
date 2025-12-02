#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль логирования BBοomer
Обеспечивает детальное логирование всех действий
"""

import os
from datetime import datetime


class Logger:
    """Класс логирования"""
    
    def __init__(self, log_file):
        self.log_file = log_file
        # Создаем директорию для логов, если она не существует
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    def log(self, message, level="info"):
        """Запись сообщения в лог"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] [{level.upper()}] {message}\n"
        
        # Выводим в консоль
        print(log_entry.strip())
        
        # Записываем в файл
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(log_entry)
        except Exception as e:
            print(f"Ошибка записи в лог файл: {e}")
    
    def show_logs(self, lines=20):
        """Показ последних строк лога"""
        try:
            with open(self.log_file, 'r', encoding='utf-8') as f:
                all_lines = f.readlines()
                last_lines = all_lines[-lines:] if len(all_lines) > lines else all_lines
                
                print(f"\nПоследние {len(last_lines)} записей из лога:")
                print("=" * 50)
                for line in last_lines:
                    print(line.strip())
                print("=" * 50)
        except FileNotFoundError:
            print("Файл лога не найден")
        except Exception as e:
            print(f"Ошибка чтения лога: {e}")
    
    def clear_logs(self):
        """Очистка лога"""
        try:
            with open(self.log_file, 'w') as f:
                f.write("")
            print("Лог очищен")
        except Exception as e:
            print(f"Ошибка очистки лога: {e}")
    
    def search_logs(self, keyword):
        """Поиск по ключевому слову в логах"""
        try:
            with open(self.log_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            matching_lines = [line.strip() for line in lines if keyword.lower() in line.lower()]
            
            if matching_lines:
                print(f"\nНайдено {len(matching_lines)} записей по ключевому слову '{keyword}':")
                print("=" * 50)
                for line in matching_lines:
                    print(line)
                print("=" * 50)
            else:
                print(f"Записи с ключевым словом '{keyword}' не найдены")
                
        except FileNotFoundError:
            print("Файл лога не найден")
        except Exception as e:
            print(f"Ошибка поиска в логе: {e}")