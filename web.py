"""
Created at 17/1/17
__author__ = 'Sergio Padilla'

"""
from flask import Flask, render_template, request
import json
import Utils
from Utils import get_planets_list

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    t = int(request.args.get("t", 0))
    data = Utils.get_planets_data(t)
    return render_template('index.html', t=t, planets_data=data)


@app.route("/get_solar_system_data", methods=['GET'])
def get_solar_system_data():
    planets = get_planets_list()
    data = []
    t = int(request.args.get("t", 0))

    for planeta in planets:
        axis_x = []
        axis_y = []
        axis_z = []
        i = 0
        pos = planeta.get_pos_newton_raphson(t)
        while i < int(planeta.period + 1) + 10:
            i += 4
            position = planeta.get_pos_newton_raphson(i)
            axis_x.append(position[0])
            axis_y.append(position[1])
            axis_z.append(position[2])

        data.append({'name': planeta.name,
                     'x': axis_x,
                     'y': axis_y,
                     'z': axis_z,
                     'pos_x': [pos[0]],
                     'pos_y': [pos[1]],
                     'pos_z': [pos[2]]})

    return json.dumps(data)


if __name__ == "__main__":
    app.run()
