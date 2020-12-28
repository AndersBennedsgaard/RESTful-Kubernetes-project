from requests import put, get, post, delete


BASE_URL = "http://localhost:5000/"


def add(item_name, quantity=1, note=""):
    res = post(
        BASE_URL + "shoppinglist",
        data={"name": item_name, "quantity": str(quantity), "note": note},
    )
    return res


def retrieve(item_id="all"):
    if isinstance(item_id, int):
        item_id = str(item_id)

    if item_id == "all":
        res = get(BASE_URL + "shoppinglist")
        return res
    res = get(BASE_URL + "shoppinglist/" + item_id)
    return res


def update(item_id, item_name, quantity=1, note=""):
    if isinstance(item_id, int):
        item_id = str(item_id)

    res = put(
        BASE_URL + "shoppinglist/" + item_id,
        data={"name": item_name, "quantity": str(quantity), "note": note},
    )
    return res


def remove(item_id):
    if isinstance(item_id, int):
        item_id = str(item_id)

    res = delete(BASE_URL + "shoppinglist/" + item_id)
    return res


# shopping_list = [
#     {"name": "onion", "quantity": "10", "note": "organic"},
#     {"name": "keyboard", "quantity": "1"},
#     {"name": "coffee"},
# ]

# for lst in shopping_list:
#     print(f"\nADD data: {lst['name']}")
#     post(BASE_URL + "shoppinglist", data=lst)

print("\nGET all")
res = retrieve()
print(res.text)

print("\nADD brakes")
res = add("brakes", 4)
print(res.text)

print("\nGET all")
res = retrieve()
print(res.text)
new_id = len(res.json()) + 1

print(f"\nGET item with id {new_id}")
res = retrieve(new_id)
print(res.text)

print(f"\nPUT item with id {new_id} with new resources")
res = update(new_id, "brakes", 8, "the cheap ones")
print(res.text)

print(f"\nDELETE item with id {new_id}")
res = remove(new_id)
print(res.text)

print(f"\nGET item with id {new_id}")
res = retrieve(new_id)
print(res.text)
