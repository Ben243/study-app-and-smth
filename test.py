from flask import Flask, request, redirect, url_for
import app_data

app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__)
    return "<p>Hello from china</p>"
    
@app.route("/test")
def test():
    return """
        <h1>This is a test page</h1>
        <p>I hate how this works</p>
    """

@app.route("/make_req", methods=['GET'])
def test_req():
    if (app_data.data):
        # test, just make a div out of the first value
        return f"""
            <form method="POST" action="{url_for('remove_item')}">
                <p>{app_data.data}</p>
                <button type="submit" name="urmom" value="{app_data.data[0]}">{app_data.data[0]}</button>
            </form>
        """
    else:
        return f"<p>no more data</p>"

@app.route("/remove", methods=['POST'])
def remove_item():
    value = request.form.get("urmom")
    value = int(value)

    if value in app_data.data:
        app_data.data.remove(value)
        print(app_data.data)

    # return f"<p>{value}</p>"
    return redirect(url_for('test_req'))