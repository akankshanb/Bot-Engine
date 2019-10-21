import os
from mattermostdriver import Driver

mm_url=os.getenv('MM_URL')
bot_token=os.getenv('PLOT_BOT_TOKEN')

def get_driver():
    my_driver = Driver({
    'url': mm_url,
    'token': bot_token,
    'scheme': 'http',
    'port': 8065,
    'basepath': '/api/v4',
    'debug': False})
    my_driver.login()
    return my_driver

def upload_file(channel_id,file_path):
    files={'files': (os.path.basename(file_path), open(file_path, 'rb'))}
    mm_file=get_driver().files.upload_file(channel_id,files)
    #mm_file=controller.files.get_file_metadata('bqgh91bhabd7ifm6ta4q7pu4bw')
    print(mm_file)
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

def create_outgoing_webhook(team_id,channel_id,display_name,url,words):
    get_driver().webhooks.create_outgoing_hook(options={
        'team_id': team_id,
        'channel_id': channel_id,
        'display_name': display_name,
        'trigger_words': words,
        'trigger_when': 0,
        'callback_urls': [url]
        })
