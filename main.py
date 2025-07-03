from demographic_data_analyzer import calculate

# Call the function and store the result
result = calculate()

# Print results
for key, value in result.items():
    print(f"{key}:\n{value}\n")