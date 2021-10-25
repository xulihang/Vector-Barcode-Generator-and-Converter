from flask import Flask, request, render_template, send_file
import inkscape_convertor
import barcode
import os

app = Flask(__name__, static_url_path='/', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/barcode/create', methods=['POST'])
def create_barcode():
    data=request.get_json()
    barcode_format = data["barcodeFormat"]
    barcode_text = data["barcodeText"]
    file_format = data["fileFormat"]
    print("Generating "+barcode_format)
    result = create_svg(barcode_format, barcode_text)
    path = "out.svg"
    if result["success"] == True:
        if file_format!="svg":
            target_path = inkscape_convertor.convert("out.svg",file_format)
            if os.path.exists(target_path):
                path = target_path
        return path
    else:
        return "faild"
        
@app.route('/image/get/<file_path>')
def get_image(file_path):
    if os.path.exists(file_path):
        return send_file(file_path)
    else:
        return "Not exist"
    
@app.route('/formats/get')
def get_formats():
    return {"formats": get_supported_formats()}

def create_svg(barcode_format,code):
    result = {}
    result["success"] = True
    try:
        writer = barcode.get(barcode_format, code)
        writer.save("out")
    except Exception as e:
        print(e)
        result["msg"] = e.msg
        result["success"] = False
    return result

def get_supported_formats():
    return barcode.PROVIDED_BARCODES

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5051)