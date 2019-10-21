import mmutil as asd

channel_id = asd.get_driver().channels.get_channel_by_name_and_team_name('PlotBotTeam', 'YashBotTester')['id']

# # file_id=asd.upload_file(channel_id,"/Users/ykamdar/Documents/sample.png")
# # #file_id='q3p8bstfttrwur578sn7mdna7e'
# # asd.create_post_file(channel_id,'test msg',[file_id])
# #asd.create_post_url(channel_id,'test msg')

# asd.create_outgoing_webhook('PlotBotTeam',channel_id,'Auto hook')


print(channel_id)

#Create webhooks and slash commands
# controller.webhooks.create_outgoing_hook(options={

# })

#print(controller.webhooks.list_outgoing_hooks({}))

# foo.channels.create_outgoing_webhook(options={
#     'team_id': 'some_team_id',
#     'name': 'awesome-channel',
#     'display_name': 'awesome channel',
#     'type': 'O'
# })

#print(controller.users.get_users())

# controller.channels.create_channel(options={
#     'team_id': 'PlotBotTeam',
#     'name': 'YashBotTester',
#     'display_name': 'awesome channel',
#     'type': 'P'
# })
