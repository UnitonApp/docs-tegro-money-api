#!/usr/bin/env python3
"""
Тестовый скрипт для проверки примеров Tegro.money API
Проверяет синтаксис и базовую корректность примеров
"""
import importlib.util
import sys
import os


def test_python_syntax(file_path):
    """Проверка синтаксиса Python файла"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        compile(code, file_path, 'exec')
        return True, "OK"
    except SyntaxError as e:
        return False, f"Syntax Error: {e}"
    except Exception as e:
        return False, f"Error: {e}"


def test_imports(file_path):
    """Проверка доступности импортов"""
    try:
        spec = importlib.util.spec_from_file_location("test_module", file_path)
        if spec is None:
            return False, "Could not create module spec"
        
        # Не выполняем модуль, только проверяем импорты
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for line in lines:
            if line.strip().startswith('import ') or line.strip().startswith('from '):
                try:
                    exec(line.strip())
                except ImportError as e:
                    return False, f"Import Error: {e}"
        
        return True, "OK"
    except Exception as e:
        return False, f"Error: {e}"


def main():
    """Основная функция тестирования"""
    print("🧪 Тестирование примеров Tegro.money API")
    print("=" * 50)
    
    # Список файлов для тестирования
    test_files = [
        'balance.py',
        'createorder.py', 
        'createWithdrawal.py',
        'order.py',
        'orders.py',
        'shops.py',
        'withdrawal.py',
        'withdrawals.py',
        'tegro_api.py'
    ]
    
    total_tests = 0
    passed_tests = 0
    
    for file_name in test_files:
        if not os.path.exists(file_name):
            print(f"❌ {file_name}: File not found")
            total_tests += 1
            continue
            
        print(f"\n📄 Тестирование {file_name}:")
        
        # Тест синтаксиса
        syntax_ok, syntax_msg = test_python_syntax(file_name)
        total_tests += 1
        if syntax_ok:
            print(f"  ✅ Синтаксис: {syntax_msg}")
            passed_tests += 1
        else:
            print(f"  ❌ Синтаксис: {syntax_msg}")
        
        # Тест импортов
        imports_ok, imports_msg = test_imports(file_name)
        total_tests += 1
        if imports_ok:
            print(f"  ✅ Импорты: {imports_msg}")
            passed_tests += 1
        else:
            print(f"  ❌ Импорты: {imports_msg}")
    
    print("\n" + "=" * 50)
    print(f"📊 Результаты: {passed_tests}/{total_tests} тестов пройдено")
    
    if passed_tests == total_tests:
        print("🎉 Все тесты пройдены успешно!")
        return 0
    else:
        print("⚠️  Обнаружены проблемы в коде")
        return 1


if __name__ == "__main__":
    sys.exit(main())