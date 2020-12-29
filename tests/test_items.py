from .fixtures import client


def test_items(client):
    def test_shopping_list(client):
        res = client.get("/shoppinglist")
        assert isinstance(res.json, list), "GET json is not a list"
        assert len(res.json) == 0, "Not the correct number of items"
        assert res.status_code == 200, "Could not GET items"

        res = client.post("/shoppinglist", data={"name": "test"})
        assert res.status_code == 201, "Could not POST item"

        res = client.get("/shoppinglist")
        assert len(res.json) == 1, "Not the correct number of items"

    def test_item(client):
        res = client.get("/shoppinglist/1")
        assert res.status_code == 200, "Could not GET added item"
        assert res.json["name"] == "test", "Wrong item name"

        res = client.get("/shoppinglist/2")
        assert res.status_code == 404, "Could GET item that has not been added"

        res = client.put(
            "/shoppinglist/1",
            data={"name": "test 2", "quantity": "1 bag", "note": "at rema"},
        )
        assert res.status_code == 201, "Could not PUT item"
        assert (
            (res.json["name"] == "test 2")
            & (res.json["quantity"] == "1 bag")
            & (res.json["note"] == "at rema")
        ), "Did not correctly PUT item"
        res = client.put("/shoppinglist/1", data=dict(quantity="1bag"))
        assert res.status_code == 201, "Could not PUT a single entry (quantity)"

        res = client.delete("/shoppinglist/1")
        assert res.status_code == 204, "Could not DELETE item"

        res = client.get("/shoppinglist/1")
        assert res.status_code == 404, "Could GET item that was DELETEd"

        res = client.delete("/shoppinglist/1")
        assert res.status_code == 404, "Could DELETE non-existing item"

    test_shopping_list(client)
    test_item(client)
