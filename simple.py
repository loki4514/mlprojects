dict1 = {'a':98.34, 'b':67.32, 'c':99.0, 'd':7}
best_model = max(dict1, key=lambda k: dict1[k])
print(best_model)     