# SCRAPY_RCLONE

## Installation

From `github`

To install it via `pip`,

```bash
pip isntall git+https://github.com/taicaile/pyrclone
pip install git+https://github.com/taicaile/scrapy_rclone
```

or clone it first,

```bash
git clone https://github.com/taicaile/scrapy_rclone.git
cd scrapy_rclone
pip install -r requirements.txt
python setup.py install
```

To install specific version,

```bash
# replace the version `v0.1.0` as you expect,
pip isntall git+https://github.com/taicaile/pyrclone
pip install git+https://github.com/taicaile/scrapy_rclone@v0.1.0
```

You may need to install pyrclone manully,

```bash
pip install git+https://github.com/taicaile/pyrclone@v0.1.0
```

## Usage

```bash
# config rclone remote,
RCLONE_REMOTE = "xxx"
# add pipeline for image download
IMAGES_STORE = "files"
ITEM_PIPELINES = {
    "scrapy.pipelines.images.ImagesPipeline": 200,
    "scrapy_rclone.pipelines.RcloneMoveImagesPipeline": 300,
}

# add pipeline for files download
FILES_STORE = "files"
ITEM_PIPELINES = {
    "scrapy.pipelines.images.FilesPipeline": 200,
    "scrapy_rclone.pipelines.RcloneMoveFilesPipeline": 300,
}s
```
