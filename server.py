from flask import Flask, render_template, redirect, request

app = Flask(__name__)

COUNTS = {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0}

with open("request_counts.txt", "r") as f:
    lines = f.readlines()
for line in range(len(lines)):
    lines[line] = lines[line].replace("\n", "").split(":")
    COUNTS[lines[line][0]] = int(lines[line][1])


@app.route('/')
def root_route():
    return render_template("index.html")


@app.route('/request-counter', methods=["GET", "POST", "PUT", "DELETE"])
def counter_route():
    global COUNTS
    COUNTS[request.method] += 1
    data = []
    for key, value in COUNTS.items():
        data.append("{0}: {1}".format(key, value))
    with open("request_counts.txt", "w") as f:
        f.write("\n".join(data))
    return redirect("/")


if __name__ == '__main__':
    app.run()
