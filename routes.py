from flask import Flask, render_template
 
app = Flask(__name__)  
 
@app.route('/')
def velha():
  return render_template('velha.html')
 
if __name__ == '__main__':
  app.run(debug=True)