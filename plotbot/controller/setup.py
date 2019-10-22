import os
import yaml
import controller.mmutil as mm

def load_config():
    mm.params['PLOT_BOT_TOKEN']=os.getenv('PLOT_BOT_TOKEN')
    if not mm.params['PLOT_BOT_TOKEN']:
        raise Exception('Please add the environment variables for the bot token (PLOT_BOT_TOKEN)')
    with open('../config.yml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        for entry in data: 
            mm.params[entry]=data[entry]
    mm.params['TEAM_ID']=mm.get_driver().teams.get_team_by_name(mm.params['TEAM_NAME'])['id']
       

def load():
    print('Setting up system...')
    load_config() 
    #Create primary bot webhook if not exist
    mm.save_outgoing_webhook(mm.params['TEAM_ID'],'','plotbot-hook',mm.params['HOOK_URL'],
                ['@plotbot','sample','plot','retrieve'])
    print('Setup complete...')
