def start_spring(**kwargs):
    collection_dict = {}
    for object, type in kwargs.items():
        if type not in collection_dict:
            collection_dict[type] = []
        collection_dict[type].append(object)

    sorted_collection_dict = dict(sorted(collection_dict.items(), key=lambda x: (-len(x[1]), x[0])))

    output = ''
    for type, collection in sorted_collection_dict.items():
        output += f"{type}:\n"
        for object in sorted(collection):
            output += f"-{object}\n"
            
    return output


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))
print()
example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird", }
print(start_spring(**example_objects))
print()
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
