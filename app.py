from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/two_sum', methods=['POST'])
def two_sum():
    data = request.get_json()
    nums = data.get('nums', [])
    target = data.get('target', 0)

    indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in indices:
            return jsonify({'result': [indices[complement], i]})
        indices[num] = i

    return jsonify({'error': 'No two sum solution found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
