from flask import render_template, request, redirect, url_for

from App.views import mn
from App.dynamo import init_dynamo


@mn.route("/")
def index():
    db = init_dynamo()
    all_items = db.scan(
        Select="ALL_ATTRIBUTES")
    return render_template("index.html", all_items=all_items)

@mn.route("/new_item", methods=["GET", "POST"])
def new_item():
    if request.method == "POST":
        first_name = request.form.get("firstName")
        last_name = request.form.get("lastName")
        print(first_name)
        
        db = init_dynamo()
        db.put_item(
            Item={
                "First Name": first_name,
                "Last Name": last_name
        })

        return redirect(url_for("main.new_item"))

    return render_template("new_item.html")
