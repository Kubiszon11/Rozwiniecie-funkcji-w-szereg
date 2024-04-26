import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def funSeriesExpansion(n, x):
    terms = np.arange(0, n+1)  # Tworzenie tablicy n+1 elementów od 0 do n
    numerator = (x - 1)**(2*terms + 1)  # Obliczanie licznika
    denominator = (2*terms + 1) * (x + 1)**(2*terms + 1)  # Obliczanie mianownika
    series_terms = 2 * numerator / denominator  # Wyliczanie poszczególnych wyrazów szeregu
    return np.sum(series_terms)  # Sumowanie wyrazów szeregu

def calculate_errors(x):
    actual_value = np.log(x)
    data = []

    for n in range(11):
        approx_value = funSeriesExpansion(n, x)  #wartość przybliżenia w podanym punkcie
        abs_error = np.abs(actual_value - approx_value) #wyznaczenie błędu bezwzględnego
        rel_error = (abs_error / actual_value) * 100 if actual_value != 0 else 0  #wyznaczenie błędu względnego
        data.append([n, approx_value, abs_error, rel_error])

    return pd.DataFrame(data, columns=['n', 'Approximation', 'Absolute Error', 'Relative Error (%)'])  #tworzenie tabeli


x = 1.2  # Punkt, w ktorym sprawdzamy błędy
errors_table = calculate_errors(x)
print(errors_table)

#tworzenie wykresów
def plot_series_expansion(x1, x2):
    x_values = np.linspace(x1, x2, 100)
    y_actual = np.log(x_values)

    plt.plot(x_values, y_actual, label='ln(x)')

    for n in [0, 2, 7]:
        y_approx = [funSeriesExpansion(n, x) for x in x_values]
        plt.plot(x_values, y_approx, label=f'n={n} Approximation', linestyle= '--')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Function and Series Expansions')
    plt.legend()
    plt.grid(True)
    plt.show()


plot_series_expansion(0.5, 4)
