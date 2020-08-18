import logging

logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
# fmt = logging.Formatter('%(name)s - %(levelname)s - %(asctime)s - %(message)s')
fh = logging.FileHandler('test.log')
# fh.setFormatter(fmt)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.info('info')
logger.debug('debug')