# NotionDB

Notionのデータベースを文字通りデータベースとしてシステムで扱うことを目的としたおふざけPythonライブラリ。  
自分用のスクリプトのためにわざわざDB用意するのめんどくさいからNotionで代用しちゃえ！  
SQLとか使えるようになったら面白いなーと思っている。  
おふざけなのでPyPIには登録しません。

## Dependency

Python 3.x

## Usage

### NotionのAPIの準備

<https://developers.notion.com/docs/getting-started>  

* Notionのintegration key & secret token取得
* 利用対象のデータベースを連携
* database id取得

### Sample

```Python
from notion-db import *

database = NotionDB(
    'secret token',
    'database id'
)

payload = {
    'page_size': 10,
    'filter': {
        # 公式のFilterオブジェクト参照
        # https://developers.notion.com/reference/post-database-query-filter
    }
}

records = database.select(payload)

for record in records:
    record.get('column name')
```

## installation

```bash
git clone 
cd notion-db
pip install . 
```

## Note

本ライブラリはNotionのAPI Ver.2022-02-22の仕様に準拠しているため、  
今後のAPIの仕様変更により正常に動作しなくなる可能性あり。

## Issue Memo

* Select以外の動作もさせたい(INSERT, UPDATE, DELETE, CREATE TABLE etc...)
* SQL -> Filterオブジェクト変換機構がほしい

## Author

かさ
