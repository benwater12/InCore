# 你是接手這個東西的小可愛麼 (*´･д･)?
# 是的話恭喜你哦 (✧≖‿ゝ≖)
# 不是的話趕緊關掉回地球吧 這裡很可怕的 (°ཀ°)
# 大部分代碼和架構都是在喝了一瓶酒才開始寫ㄉ ( ´∀｀)つt[ ]
# 寫的時候只有我和神知道在幹嘛  (༼•̀ɷ•́༽)
# 現在只有神知道了 ( ￣ 3￣)y▂ξ
# 代碼成分：酒精 (80%)、尼古丁 (10%)、肝(6%)、青春歲月(3%)，以及一點點的 flask,sql,sklearn,keras,matplotlib (1%)

from flask import Flask
from flask_restful import Api
import logging
import sys
from params import params
from flask_cors import CORS

from service.dataService.controller.upload import Upload
from service.dataService.controller.download import Download
from service.dataService.controller.getColumn import getColumn
from service.dataService.controller.getFileStatus import getFileStatus
from service.dataService.controller.delete import DeleteFile

from service.visualizeService.controller.getImg import getImg

par=params()
app = Flask(__name__)
cors = CORS(app, resources=r"/*")

# bind api
api.add_resource(Upload, "/data/upload")
api.add_resource(Download,'/data/download')
api.add_resource(getColumn,'/data/getcol')
api.add_resource(getFileStatus,'/data/getstatus')
api.add_resource(DeleteFile,'/data/delete')

api.add_resource(getImg,'/viz/getimg')

if __name__ == "__main__":

    if '--debug' in sys.argv:
        logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s')
    else:
        logging.basicConfig(level=logging.INFO , format='[%(levelname)s] %(message)s')
    logging.info(f'InCore running at port {par.port}')
    app.run(debug='--debug' in sys.argv,port=par.port,host='0.0.0.0')
    

#   █████▒█    ██  ▄████▄   ██ ▄█▀       ██████╗ ██╗   ██╗ ██████╗
# ▓██   ▒ ██  ▓██▒▒██▀ ▀█   ██▄█▒        ██╔══██╗██║   ██║██╔════╝
# ▒████ ░▓██  ▒██░▒▓█    ▄ ▓███▄░        ██████╔╝██║   ██║██║  ███╗
# ░▓█▒  ░▓▓█  ░██░▒▓▓▄ ▄██▒▓██ █▄        ██╔══██╗██║   ██║██║   ██║
# ░▒█░   ▒▒█████▓ ▒ ▓███▀ ░▒██▒ █▄       ██████╔╝╚██████╔╝╚██████╔╝
#  ▒ ░   ░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░▒ ▒▒ ▓▒       ╚═════╝  ╚═════╝  ╚═════╝
#  ░     ░░▒░ ░ ░   ░  ▒   ░ ░▒ ▒░
#  ░ ░    ░░░ ░ ░ ░        ░ ░░ ░
#           ░     ░ ░      ░  ░
#                 ░
#


#                       _oo0oo_
#                      o8888888o
#                      88" . "88
#                      (| -_- |)
#                      0\  =  /0
#                    ___/`---'\___
#                  .' \\|     |# '.
#                 / \\|||  :  |||# \
#                / _||||| -:- |||||- \
#               |   | \\\  -  #/ |   |
#               | \_|  ''\---/''  |_/ |
#               \  .-\__  '-'  ___/-. /
#             ___'. .'  /--.--\  `. .'___
#          ."" '<  `.___\_<|>_/___.' >' "".
#         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#         \  \ `_.   \_ __\ /__ _/   .-` /  /
#     =====`-.____`.___ \_____/___.-`___.-'=====
#                       `=---='
#
#
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#               佛祖保佑         永无BUG
#



#                               |~~~~~~~|
#                               |       |
#                               |       |
#                               |       |
#                               |       |
#                               |       |
#    |~.\\\_\~~~~~~~~~~~~~~xx~~~         ~~~~~~~~~~~~~~~~~~~~~/_#;~|
#    |  \  o \_         ,XXXXX),                         _..-~ o /  |
#    |    ~~\  ~-.     XXXXX`)))),                 _.--~~   .-~~~   |
#     ~~~~~~~`\   ~\~~~XXX' _/ ';))     |~~~~~~..-~     _.-~ ~~~~~~~
#              `\   ~~--`_\~\, ;;;\)__.---.~~~      _.-~
#                ~-.       `:;;/;; \          _..-~~
#                   ~-._      `''        /-~-~
#                       `\              /  /
#                         |         ,   | |
#                          |  '        /  |
#                           \/;          |
#                            ;;          |
#                            `;   .       |
#                            |~~~-----.....|
#                           | \             \
#                          | /\~~--...__    |
#                          (|  `\       __-\|
#                          ||    \_   /~    |
#                          |)     \~-'      |
#                           |      | \      '
#                           |      |  \    :
#                            \     |  |    |
#                             |    )  (    )
#                              \  /;  /\  |
#                              |    |/   |
#                              |    |   |
#                               \  .'  ||
#                               |  |  | |
#                               (  | |  |
#                               |   \ \ |
#                               || o `.)|
#                               |`\\\\) |
#                               |       |
#                               |       |
#
#                           耶穌保佑    永無BUG

#        _.---,._,'
#       /' _.--.<
#         /'     `'
#       /' _.---._____
#       \.'   ___, .-'`
#           /'    \\             
#         /'       `-.           
#        |                       
#        |                   .-'~~~`-.
#        |                 .'         `.
#        |                 |  R  I  P  |
#        |                 |           |
#        |                 |   LIVER   |
#        |                 |   LUNGS   |
#        |                 |   TIMES   |
#        |                 |           |
#         \              \\|           |//
#   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
