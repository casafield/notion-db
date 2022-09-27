import requests

class NotionDB:
    def __init__(
        self,
        secret_token,
        database_id
    ):
        self.database_id = database_id

        self.query_database_url = f"https://api.notion.com/v1/databases/{database_id}/query"
        self.create_database_url = "https://api.notion.com/v1/databases"
        self.update_database_url = f"https://api.notion.com/v1/databases/{database_id}"
        self.retrieve_database_url = f"https://api.notion.com/v1/databases/{database_id}"

        self.headers = {
            "Accept": "application/json",
            "Notion-Version": "2022-02-22",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {secret_token}"
        }

    def select(self, payload):
        response = requests.post(
            self.query_database_url, json=payload, headers=self.headers
        ).json()
        return self._response_to_record_array(response)

    # def update():
    #     return None
    
    # def insert():
    #     return None
    
    # def describe(database_id):
    #     return database_id

    # def create_table():
    #     return None


    def _response_to_record_array(self, response):
        database = []
        for column in response["results"]:
            database.append(Record(column["properties"]))
        return database


class Record:
    def __init__(self, notion_data) -> None:
        self.data = notion_data

    def get(self, column_name):
        type = self.data[column_name]["type"]
        if type == "rich_text":
            rich_text = self.data[column_name]["rich_text"]
            if len(rich_text) == 0: return ""
            return self.data[column_name]["rich_text"][0]["plain_text"]
        elif type == "number":
            return self.data[column_name]["number"]
        elif type == "title":
            return self.data[column_name]["title"][0]["plain_text"]
        elif type == "checkbox":
            return self.data[column_name]["checkbox"]
        elif type == "select":
            return self.data[column_name]["select"]["name"]
        else:
            return None
