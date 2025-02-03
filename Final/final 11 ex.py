import json


def optimize_loading(max_weight, items):
    items_with_ratio = []
    for i in range(len(items)):
        weight, value = items[i]
        items_with_ratio.append((weight, value, value / weight))

    items_with_ratio.sort(key=lambda x: x[2], reverse=True)

    total_value = 0
    remaining_weight = max_weight
    selected_items = []

    for weight, value, ratio in items_with_ratio:
        if remaining_weight == 0:
            break

        if weight <= remaining_weight:
            selected_items.append((weight, value))
            total_value += value
            remaining_weight -= weight

    return total_value, selected_items

def main():

    with open("detailed_data.json", "r") as file:
        data = json.load(file)

    max_weight = data["max_weight"]
    items = data["items"]

    total_value, selected_items = optimize_loading(max_weight, items)
    print("Общая стоимость: ", total_value)
    print("Выбранные товары:")
    for weight, value in selected_items:
        print("Вес: ", weight, "Стоимость: ", value)


if __name__ == "__main__":
    main()