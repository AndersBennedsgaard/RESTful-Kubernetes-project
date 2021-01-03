from requests import put, get, post, delete


BASE_URL = "http://localhost:5000/"


# shopping_list = [
#     {"name": "onion", "quantity": "10", "note": "organic"},
#     {"name": "keyboard", "quantity": "1"},
#     {"name": "coffee"},
# ]
# for lst in shopping_list:
#     print(f"\nADD data: {lst['name']}")
#     post(BASE_URL + "shoppinglist", data=lst)

print("GET all")
res = get(BASE_URL + "shoppinglist")
print(res.text)
n_entries = len(res.json())

print("POST item")
res = post(BASE_URL + "shoppinglist", data={"name": "brakes", "quantity": "4"})
new_id = n_entries + 1

print(f"GET item with id {new_id}")
res = get(BASE_URL + f"shoppinglist/{new_id}")
print(res.text)

print(f"PUT item with id {new_id} with new resources")
res = put(
    BASE_URL + f"shoppinglist/{new_id}",
    data={"name": "brakes", "quantity": "8", "note": "The cheap ones"},
)
print(res.text)

print(f"DELETE item with id {new_id}")
res = delete(BASE_URL + f"shoppinglist/{new_id}")

print(f"\nGET item with id {new_id}")
res = get(BASE_URL + f"shoppinglist/{new_id}")
print(res.text)
