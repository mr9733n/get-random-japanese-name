from flask import Flask, request, jsonify, render_template
from japanese_name_generator import JapaneseNameGenerator

app = Flask(__name__, template_folder='templates', static_folder='static')
name_generator = JapaneseNameGenerator()

def generate_japanese_names(num_names, save_to_file, sex):
    name_generator = JapaneseNameGenerator(num_names=num_names, save_to_file=save_to_file, params={"sex": sex})
    random_names = name_generator.generate_names()
    return random_names

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_names = int(request.form.get('num_names', 1))
        save_to_file = bool(request.form.get('save_to_file', False))
        sex = request.form.get('sex', 'male')
        
        # Get names and return to page
        random_names = generate_japanese_names(num_names, save_to_file, sex)
        return render_template('index.html', names=random_names)
    else:
        return render_template('index.html', names=[])

@app.route('/generate_names', methods=['GET'])
def generate_names():
    num_names = int(request.args.get('num_names', 1))
    save_to_file = bool(request.args.get('save_to_file', False))
    sex = request.args.get('sex', 'male')
    
    # Get name and return in JSON
    random_names = generate_japanese_names(num_names, save_to_file, sex)
    return jsonify({"names": random_names})

if __name__ == '__main__':
    app.run(debug=True)

# app.py
#  Usage: 
# http://localhost:5000/generate_names?num_names=3&sex=male&save_to_file=true
