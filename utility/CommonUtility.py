import logging

class CommonUtility(object):

    @classmethod
    def get_logger(cls, logger_name, level=logging.INFO):

        logger = logging.getLogger(logger_name)
        logger.setLevel(level)
        ch = logging.StreamHandler()
        ch.setLevel(level)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)

        logger.addHandler(ch)

        return logger

