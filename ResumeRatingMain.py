import os
from flask import Flask, flash, request, redirect, render_template,url_for
import SimilarityCalculator

ALLOWED_EXTENSIONS = ['txt', 'pdf']
app = Flask(__name__)
app.secret_key = "COMS661"

def isProperFile(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def uploadFormsHtml():
    return render_template('resume_loader.html')

@app.route('/failure')
def failure():
   return 'No files were selected'

@app.route('/success/<name>')
def success(name):
   return 'Files %s has been selected' %name

@app.route('/', methods=['POST', 'GET'])
def checkFileTypes():
    if request.method == 'POST':
        # check for proper file types.
        if 'jobDescriptionFile' not in request.files:
           flash('Job description document can not be empty')
           return redirect(request.url)
        if 'resumeFiles' not in request.files:
           flash('Select at least one resume File')
           return redirect(request.url)

        jDFile = request.files['jobDescriptionFile']
        resumeFiles = request.files.getlist("resumeFiles")

        if len(resumeFiles) == 0:
            flash('Select at least one resume File')
            return redirect(request.url)

        for resumeFile in resumeFiles:
            if not isProperFile(resumeFile.filename):
                flash('Allowed file types are txt, pdf')
                return redirect(request.url)
        
        if not isProperFile(jDFile.filename):
            flash('Allowed file types are txt, pdf')
            return redirect(request.url)

        abs_paths = []
        jDFileName = jDFile.filename
        jDFile.save(os.path.join('', jDFileName))
        for resumeFile in resumeFiles:
            resumeFilename = resumeFile.filename
            abs_paths.append(resumeFilename)
            resumeFile.save(os.path.join('', resumeFilename))
        result = SimilarityCalculator.getSimilarityScore(jDFileName, abs_paths)
        for file_path in abs_paths:
            os.remove(file_path)

        return render_template("resume_results.html", result=result)

if __name__ == "__main__":
    app.run(debug = True)