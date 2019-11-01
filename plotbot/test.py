import controller.mmutil as mm
import controller.setup as setup
import framework.constants as constants
import os

def loadDataset(dsName,dsFileId,userId):
    if not userId in constants.userIDs:
        constants.userIDs[userId]={}
    constants.userIDs[userId][dsName]={}
    file_resp=mm.fetchFile(dsFileId)
    filename=basePath+userId+'/'+dsName+'/'+dsFileId
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'wb') as w:
        w.write(file_resp.content)

basePath='storage/'

if __name__ == "__main__":
    setup.load()
    loadDataset('test','7yprd67u1irtjxsqeqc1omyr8h','user1')