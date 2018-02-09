import logging
from datetime import datetime

logger = logging.getLogger('Index images')

logger.setLevel(10)
 
fh = logging.FileHandler('logs/%s.log' % (datetime.now().strftime('%d-%m-%d')))
logger.addHandler(fh)

sh = logging.StreamHandler()
logger.addHandler(sh)

formatter = logging.Formatter('[%(asctime)s]: %(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)
 
# ログのコンソール出力の設定（4）
sh = logging.StreamHandler()
logger.addHandler(sh)