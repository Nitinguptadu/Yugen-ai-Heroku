from flask import Flask, request, jsonify, render_template
import pickle
import config

import numpy as np
import pandas as pd 


from prep import preproccese

app = Flask(__name__)
model = pickle.load(open('Pickle_RL_Model1.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    content = request.json

    output_list = []
    j = 0
    for i in content:

	
        int_features = []
        for x in i:
            int_features.append(content[j][x])

        k = preproccese(int_features)
        final_features = [np.array(k)]
        prediction = model.predict(final_features)
        output = round(prediction[0], 2)
        j = j + 1

        output_list.append({"output "+str(j): output})
	    
 
    return jsonify({"output_list":str(output_list)})


#    print (int_features)

#    int_feature = []
#    for i in int_features:
#        i = i.replace("\t", "")
#        int_feature.append(i)
#    int_feature.append(0)


#    int_feature = np.transpose(int_feature)
#    print(int_feature)


#    content = request.json
#    print (content['mytext'])




#    int_features = [ x for x in request.form.values()]


#    return render_template('index.html', prediction_text='[One Repersent Yes & Zero Repersent No] Your Result  :-- {}'.format(output))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)

