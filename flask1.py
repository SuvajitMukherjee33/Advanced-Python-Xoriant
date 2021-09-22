from flask import Flask
app=Flask(__name__)

@app.route('/blog/<int:postId>')
def show_postId(postId):
    return 'Post Id= %d'%postId

@app.route('/rev/<float:revid>')
def show_revId(revid):
    return 'Rec id= %f' %revid

if __name__=='__main__':
    app.run(debug=True)