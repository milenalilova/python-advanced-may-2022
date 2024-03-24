from os import listdir
from os.path import isdir, join


def directory_traversal(path, file_by_ext):
    for element in listdir(path):
        if isdir(join(path, element)):
            directory_traversal(join(path, element), file_by_ext)
        else:
            extension = element.split('.')[-1]
            if extension not in file_by_ext:
                file_by_ext[extension] = []
            file_by_ext[extension].append(element)


result = {}
directory_traversal('./', result)
sorted_result = dict(sorted(result.items(), key=lambda x: (x[0], x[1])))

with open('./report.txt', 'w') as output_file:
    for ext, files in sorted_result.items():
        output_file.write(ext + '\n')

        for file in files:
            output_file.write(f'- - - {file}\n')



# Variant 2 (very interesting)

# from os import walk
#
# result = {}
# for _, _, files in walk('.', topdown=False):
#
#     for file in files:
#         ext = file.split('.')[-1]
#         if ext not in result:
#             result[ext] = []
#         result[ext].append(file)
# # Need to do sorting
# for key, value in result.items():
#     print(key, value)
