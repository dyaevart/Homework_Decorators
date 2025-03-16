import pprint
import os
from Decorators.test_2 import logger
# from Decorators.test_1 import logger

@logger("get_shop_list_by_dishes.log")
def get_shop_list_by_dishes(dishes, person_count):
	ingredients = {}
	for dish in dishes:
		for dish_name, ingredient_list in cook_book.items():
			if dish_name == dish:
				for ingredient in ingredient_list:
					if ingredient["ingredient_name"] in list(ingredients.keys()):
						ingredients[ingredient["ingredient_name"]]["quantity"] +=(
								int(ingredient["quantity"]) * person_count)
					else:
						ingredients[ingredient["ingredient_name"]] = \
							{"measure": ingredient["measure"], "quantity": int(ingredient["quantity"]) * person_count}
	return ingredients

def convert_files_content_to_dict(files_paths):
	file_list = []
	for file_path in files_paths:
		with open(file_path, encoding="utf-8") as f:
			lines = [line for line in f]
		file_list.append({"file_name": os.path.basename(file_path),
								"file_lines": len(lines), "file_contain": lines})
	return sorted(file_list, key=lambda d: d["file_lines"])

with open("./recipes.txt", encoding="utf-8") as file:
	cook_book = {}
	for line in file.read().split('\n\n'):
		name, _, *args = line.split('\n')
		cook_li = []
		for arg in args:
			arg_list = arg.split(" | ")
			cook_li.append({"ingredient_name": arg_list[0], "quantity": arg_list[1], "measure": arg_list[2]})
		cook_book[name] = cook_li

print("Словарь с кулинарной книгой cook_book:\n=============")
pprint.pprint(cook_book, sort_dicts=False)

print("\nПодсчёт количества продуктов:\n=============")
pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

print("\nОбъединение файлов:\n=============")
with open('./result.txt', 'w', encoding='utf-8') as f:  # w в явном виде указывает, что мы хотим открыть файл для записи
	all_files_list = convert_files_content_to_dict(["./1.txt", "./2.txt", "./3.txt"])
	for file_item in all_files_list:
		f.write(file_item["file_name"] + "\n"
				+ str(file_item["file_lines"]) + "\n"
				+ "".join(file_item["file_contain"]) + "\n")