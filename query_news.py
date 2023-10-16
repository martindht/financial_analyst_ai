import os, config
import openai
from llama_index import StorageContext, load_index_from_storage


os.environ['OPENAI_API_KEY'] = config.OPENAI_API_KEY
openai.api_key = os.environ.get('OPENAI_API_KEY')


storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)




