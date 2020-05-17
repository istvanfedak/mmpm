#!/usr/bin/env python3
import logging
import logging.handlers
from mmpm import consts
from os.path import join


class MMPMLogger():
    '''
    Object used for logging while MMPM is executing. Log files can be found in
    ~/.config/mmpm/log
    '''
    def __init__(self):
        self.log_file: str = join(consts.MMPM_CONFIG_DIR, 'log', 'mmpm-cli-interface.log')
        self.log_format = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s'
        logging.basicConfig(filename=self.log_file, format=self.log_format)
        logger: logging.Logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        self.handler = logging.handlers.RotatingFileHandler(
            self.log_file,
            mode='a',
            maxBytes=1024*1024,
            backupCount=2,
            encoding=None,
            delay=0
        )

        logger.addHandler(self.handler)
        self.logger = logger


class MagicMirrorModule:
    def __init__(self, category: str, title: str, author: str, repository: str, description: str):
        self.category: str = category
        self.title: str = title
        self.author: str = author
        self.repository: str = repository
        self.description: str = description

    def normalize_name(self) -> str:
        return self.title.lower()
