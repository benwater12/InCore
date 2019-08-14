from flask import Flask
from flask_restful import Api, Resource, reqparse
from werkzeug.datastructures import FileStorage
from params import params
from utils import tokenValidator,sql
import glob
import uuid
from service.dataService.utils import fileChecker,fileUidGenerator
import logging

# app = Flask(__name__)
# api = Api(app)

param=params()

class Upload(Resource):
    def post(self):
        '''
        @ type: num/cv/nlp
        @ file: a file
        @ tokenstr: keypair1
        @ tokenint: keypair2
        '''
        fName='[Upload]'
        parser = reqparse.RequestParser()
        parser.add_argument('file', type=FileStorage, location='files',required=True)
        parser.add_argument('type',type=str,required=True)
        # parser.add_argument('user',type=str,required=True)
        parser.add_argument('tokenstr',type=str,required=True)
        parser.add_argument('tokenint',type=int,required=True)
        args = parser.parse_args()
        logging.info(f"[Upload] args: {args}")
        file = args['file']
        dataType=args['type']
        # user=args['user']
        tokenstr=args['tokenstr']
        tokenint=args['tokenint']

        
        #check token
        if not tokenValidator(tokenstr,tokenint):
            return {"status":"error","msg":"token error","data":{}},401
        
        pft=param.dataFileType
        #check project type
        if dataType not in pft:
            return {"status":"error","msg":"project type not supported","data":{}},400
        
        #check filetype
        
        filename=file.filename
        filetype=filename[filename.rfind("."):]
        logging.debug("[Upload] File type:{filetype}")
        if filetype not in pft[dataType]:
            return {"status":"error","msg":"file type error","data":{}},400

        #generate file UID and save
        uid=fileUidGenerator().uid
        logging.debug(f'[Upload] file UID:{uid}')
        savedPath=param.filepath+"/"+uid+filetype
        try:
            file.save(savedPath)
        except Exception as e:
            return {"status":"error","msg":f"file error:{e}","data":{}},400

        '''
        @ check file content
        '''
        try:
            fileChecker(savedPath,dataType).check()
        except Exception as e:
            logging.error(f'{fName}{e}')
            return {"status":"error","msg":str(e),"data":{}},400
        if filetype=='.zip':
            savedPath=savedPath[:savedPath.rfind(".")]
            numFilePath=glob.glob((savedPath+"/*.csv"))[0]
        try:
            db=sql()
            if filetype=='.zip':
                db.cursor.execute(f"insert into files (`fid`,`dataType`,`path`,`numFile`,`inuse`) values ('{uid}','{dataType}','{savedPath}','{numFilePath}',False);")
            else:
                db.cursor.execute(f"insert into files (`fid`,`dataType`,`path`,`inuse`) values ('{uid}','{dataType}','{savedPath}',False);")
            db.conn.commit()
        except Exception as e:
            db.conn.rollback()
        finally:
            db.conn.close()
        logging.info(f"[Upload] OK with file uid {uid}")
        return {"status":"success","msg":"","data":{"fileUid":uid}},201