import os, config
import openai
from llama_index import StorageContext, load_index_from_storage


os.environ['OPENAI_API_KEY'] = config.OPENAI_API_KEY
openai.api_key = os.environ.get('OPENAI_API_KEY')


# new version of llama index uses StorageContext instead of load_from_disk
# index = GPTSimpleVectorIndex.load_from_disk('index_news.json')
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)




