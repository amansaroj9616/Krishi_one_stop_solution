try:
    from tensorflow.keras.preprocessing import image
    print("Import successful.")
except ImportError as e:
    print("Import failed:", e)
