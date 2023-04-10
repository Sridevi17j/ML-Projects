
"""
Create DB
"""
"""
connecting to a db

"""
conn=mysql.connector.connect(
host='127.0.0.1',
user='root',
password='',
database='mysql'
)


mycursor=conn.cursor()





"""
Upload CSV File from front end(flask) to the backend(to our location)
"""

def uploadFiles():
    uploaded_file=request.files['file']
    if uploaded_file.filename!='':
        file_path=os.path.join(app.config['UPLOAD_FOLDER'],uploaded_file.filename)
        uploaded_file.save(file_path)
    return redirect(url_for('index'))

"""
Read CSV File in df and Parse CSV File

"""
df=pd.read_csv(file_path)
col_names=df.columns

for i, row in df.iterrows():
    mycursor.execute('INSERT INTO TAIWAN_CP({col_names})'.format)


for i in



col


mycursor.execute('INSERT INTO TA)

"""
Parsing CSV Files and storing into db

"""

def parseCSV(file_path):
    df=pd.read_csv(file_path)
    for i,row in df.iterrows():
        query="INSERT INTO TAI"



if (__name__ == '__main__'):
    app.run(port=5000)