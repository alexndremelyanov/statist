from scipy.stats import kruskal


def write_to_file(file_path, statistic, p_value, hypothesis_result):
    with open(file_path, 'w') as result_file:
        result_file.write(
            f"Статистика критерия Краскела-Уоллиса: {statistic}\n")
        result_file.write(f"P-значение: {p_value}\n")
        result_file.write(hypothesis_result)


def read_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        groups = [list(map(float, line.strip().split())) for line in lines]
    return groups


input_file_path = "Inp\\kruskal_input.inp"


output_file_path = "Out\\kruskal_result.out"


data_groups = read_from_file(input_file_path)


statistic, p_value = kruskal(*data_groups)


alpha = 0.05
if p_value < alpha:
    hypothesis_result = "Отвергаем нулевую гипотезу: Есть статистически значимые различия между группами."
else:
    hypothesis_result = "Не отвергаем нулевую гипотезу: Нет статистически значимых различий между группами."


write_to_file(output_file_path, statistic, p_value, hypothesis_result)
print(f"Результаты сохранены в файле: {output_file_path}")
