from flask import Flask, request, jsonify
from flask_cors import CORS
from osgeo import gdal
import numpy as np

app = Flask(__name__)
CORS(app, origins=["http://localhost", "http://127.0.0.1"])

dataset = gdal.Open('us_nga_egm84_30.tif')
geotransform = dataset.GetGeoTransform()
raster = dataset.ReadAsArray()

@app.route('/geoid_height', methods=['GET'])
def geoid_height():
    lat = float(request.args.get('lat'))
    lon = float(request.args.get('lon'))

    x = int((lon - geotransform[0]) / geotransform[1])
    y = int((lat - geotransform[3]) / geotransform[5])

    if 0 <= x < raster.shape[1] and 0 <= y < raster.shape[0]:
        height = float(raster[y, x])
    else:
        return jsonify({'error': 'Coordinates out of bounds'}), 400

    return jsonify({'geoid_height': height})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)