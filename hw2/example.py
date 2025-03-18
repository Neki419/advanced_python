from latex_generator.latex_generator import generate_latex_table, generate_full_latex_document

table_data = [[str(i * j) for j in range(10)] for i in range(10)]
image_path = "cat.png"

with open("output.tex", "w", encoding="utf-8") as f:
        for line in generate_full_latex_document(table_data, image_path):
            f.write(line)


# table_data1 = [["A", "B"], ["1", "2"]]

# table_data2 = [["A", ""], ["", "B"]]

# table_data3 = [["Single Cell"]]

# table_data4 = [["A", "B"], ["1", "2", "3"]]

# table_data5 = []

# table_data6 = [[str(i * j) for j in range(10)] for i in range(10)]

# table_data = [
#     table_data1,
#     table_data2,
#     table_data3,
#     table_data4,
#     table_data5,
#     table_data6
# ]

# with open("artifact1.tex", "w", encoding="utf-8") as f:
#     for table in table_data:
#         try:
#             for line in generate_latex_table(table):
#                 f.write(line)
#             f.write('\n')
#         except ValueError as e:
#             print(f"Ошибка в таблице {table}: {e}")
#             continue