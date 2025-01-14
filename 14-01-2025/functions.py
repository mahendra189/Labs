# all methods on set class available

methods_of_sets =  (list(set().__dir__()))

for m in methods_of_sets:
    if not m.startswith("_"):
        print(m)