"""MongoDB Item Pipeline"""
import logging
from abc import ABC

from pyrclone.move import RcloneMoveProducer
from twisted.internet.threads import deferToThread

from . import defaults

logger = logging.getLogger(__name__)


class RcloneMovePipeline(ABC):
    """Pushes serialized item into a MongoDB collection"""

    STORE_FIELD = None
    RESULTS_FIELD = None
    DEFAULT_RESULTS_FIELD = None

    def __init__(self, rclonemove: "RcloneMoveProducer", itemkey: str):
        """Initialize pipeline."""
        self.rclonemove = rclonemove
        self.itemkey = itemkey

    @classmethod
    def from_settings(cls, settings):
        """create from settings"""
        if cls.STORE_FIELD is None:
            logger.error("the STORE_FIELD cannot be empty.")
            return None

        copy = settings.copy_to_dict()
        copy["BASEDIR"] = settings.get(cls.STORE_FIELD)
        rclonemove = RcloneMoveProducer.from_settings(copy)
        itemkey = settings.get(
            cls.RESULTS_FIELD, getattr(defaults, cls.DEFAULT_RESULTS_FIELD)
        )
        return cls(rclonemove=rclonemove, itemkey=itemkey)

    @classmethod
    def from_crawler(cls, crawler):
        """create from crawler"""
        return cls.from_settings(crawler.settings)

    def process_item(self, item, spider):
        """process item"""
        return deferToThread(self._process_item, item, spider)

    def _process_item(self, item, spider):
        """process item"""
        del spider
        # pylint:disable=protected-access
        if self.itemkey in item:
            storages = item[self.itemkey]
            for storage in storages:
                if "path" in storage:
                    self.rclonemove.push(storage["path"])
        return item


class RcloneMoveFilesPipeline(RcloneMovePipeline):
    STORE_FIELD = "FILES_STORE"
    RESULTS_FIELD = "FILES_RESULTS_FIELD"
    DEFAULT_RESULTS_FIELD = "FILES_RESULT_FIELD"


class RcloneMoveImagesPipeline(RcloneMovePipeline):
    STORE_FIELD = "IMAGES_STORE"
    RESULTS_FIELD = "IMAGES_RESULTS_FIELD"
    DEFAULT_RESULTS_FIELD = "IMAGES_RESULT_FIELD"
