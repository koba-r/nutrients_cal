from flask import Flask, request, render_template
from nnls import calc

#app = Flask(__name__)
app = Flask(__name__, static_folder='./templates/images') 

@app.route('/')
def test1():
    return render_template('index.html')

@app.route('/input')
def test2():
    return render_template('checkbox.html')

@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
      food_id_list_str = request.form.getlist('food')
      food_id_list = []
      for food_id_str in food_id_list_str:
        food_id_list.append(int(food_id_str))
      result = calc(food_id_list)[0]
      result2 = calc(food_id_list)[1]
      return render_template("result.html",result = result,result2 = result2)
    else :
      food_id_list_str = request.args.getlist('food')
      food_id_list = []
      for food_id_str in food_id_list_str:
        food_id_list.append(int(food_id_str))
      result = calc(food_id_list)[0]
      result2 = calc(food_id_list)[1]
      return render_template("result.html",result = result,result2 = result2)

if __name__ == "__main__":
  app.run()

# 以下は元のプログラム
# from flask import Flask, request, render_template
# from nnls import calc

# app = Flask(__name__)

# @app.route('/')
# def test1():
#     return render_template('checkbox.html')

# @app.route('/result', methods=['POST','GET'])
# def result():
#     if request.method == 'POST':
#       food_id_list_str = request.form.getlist('food')
#       food_id_list = []
#       for food_id_str in food_id_list_str:
#         food_id_list.append(int(food_id_str))
#       result = calc(food_id_list)
#       return render_template("result.html",result = result)
#     else :
#       food_id_list_str = request.args.getlist('food')
#       food_id_list = []
#       for food_id_str in food_id_list_str:
#         food_id_list.append(int(food_id_str))
#       result = calc(food_id_list)
#       return render_template("result.html",result = result)

# if __name__ == "__main__":
#   app.run()
