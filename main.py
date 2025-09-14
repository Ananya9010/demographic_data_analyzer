from demographic_data_analyzer import calculate

result = calculate()

for key, value in result.items():
    print(f"{key}:\n{value}\n")
