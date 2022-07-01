"""Main()

Keyword arguments:
real -- the real part (default 0.0)
imag -- the imaginary part (default 0.0)
"""
# import main Flask class and request object
import ast
import json
from flask import Flask, request, render_template
from flask_cors import CORS
from evaluation.eval_graph import evaluate


app = Flask(__name__)
CORS(app)

@app.route('/data_server/evaluation')
def evaluate_graph():
    """Backend function to be called.

    Returns:
        Evaluation score: A dictionary to be dumped as a string.
    """
    floor_plan_json = request.args.get('floor_plan')
    floor_plan_json = ast.literal_eval(floor_plan_json)
    score_final, total_area, total_usable_area, total_used_area = evaluate(
        floor_plan_json)
    (align_score, size_score, desired_size, lounge_score, hallway_access_score,
     work_ext_score, meet_score, hallway_num) = score_final
    return json.dumps({'align_score': str(align_score),
                       'size_score': str(size_score),
                       'desired_size': str(desired_size),
                       'lounge_score': str(lounge_score),
                       'hallway_access_score': str(hallway_access_score),
                       'work_ext_score': str(work_ext_score),
                       'meet_score': str(meet_score),
                       'hallway_number': str(hallway_num),
                       'total_area': str(total_area),
                       'total_usable_area': str(total_usable_area),
                       'total_used_area': str(total_used_area)})

if __name__ == '__main__':
    app.run()


# www.baidu.com (域名) ---> VIP(load balance) ---> servers（10.1.1.200; 10.2.23.100, etc.. ）

# http://10.0.0.195:3000/

# 什么是一个 http request
# 解释一下tcp/ip
