import mmutil as mm

#Sample code to create the webhooks
team_id=mm.get_driver().teams.get_team_by_name('PlotBotTeam')['id']
print(team_id)
channel_id=mm.get_driver().channels.get_channel_by_name(team_id, 'YashBotTester')['id']
my_url='http://ec2-18-223-119-47.us-east-2.compute.amazonaws.com:5000/plotbot'
channel_id=''
mm.create_outgoing_webhook(team_id,channel_id,'Auto hook 1',my_url,['test1'])