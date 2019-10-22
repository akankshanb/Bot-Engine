import os
import yaml
from mattermostdriver import Driver

params={}

def get_driver():
    my_driver = Driver({
    'url': params['mm_ip'],
    'token': params['bot_token'],
    'scheme': 'http',
    'port': 8065,
    'basepath': '/api/v4',
    'debug': False })
    my_driver.login()
    return my_driver

def upload_file(channel_id,file_path):
    files={'files': (os.path.basename(file_path), open(file_path, 'rb'))}
    mm_file=get_driver().files.upload_file(channel_id,files)
    #mm_file=controller.files.get_file_metadata('bqgh91bhabd7ifm6ta4q7pu4bw')
    #print(mm_file)
    file_id=mm_file["file_infos"][0]["id"]
    #file_id=mm_file["id"]
    return file_id

def create_post_file(channel_id,message,file_ids):
    get_driver().posts.create_post(options={
        'channel_id': channel_id,
        'message': message,
        'file_ids': file_ids})

def create_post_url(channel_id,message):
    get_driver().posts.create_post(options={
        'channel_id': channel_id,
        'message': message,
        "props": {"attachments": [{"image_url": "https://file-examples.com/wp-content/uploads/2017/10/file_example_JPG_100kB.jpg"}]}
        })

def post_message_file(channel_id,message,file_path):
    file_id=upload_file(channel_id,file_path)
    create_post_file(channel_id,message,[file_id])

def post_message(channel_id,message):
    get_driver().posts.create_post(options={
        'channel_id': channel_id,
        'message': message})

def save_outgoing_webhook(team_id,channel_id,display_name,url,words):
    my_driver=get_driver()
    options={'team_id': team_id,'channel_id': channel_id,'display_name': display_name,
        'trigger_words': words,'trigger_when': 0,'callback_urls': [url]}
    hooks=my_driver.webhooks.list_outgoing_hooks({})
    my_hook=next((hook for hook in hooks if hook['display_name'] == display_name), None)
    if not my_hook:
        my_driver.webhooks.create_outgoing_hook(options)
    else:
        pass
        # options['hook_id']=my_hook['id']
        # res=my_driver.webhooks.update_outgoing_hook(my_hook['id'],options)
