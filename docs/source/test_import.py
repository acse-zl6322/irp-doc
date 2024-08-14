# docs/source/test_import.py
try:
    import montecarlo.handler
    import montecarlo.processor
    import montecarlo.driver
    print("Modules imported successfully")
except ImportError as e:
    print(f"ImportError: {e}")
