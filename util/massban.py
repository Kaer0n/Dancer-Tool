from py_compile import _get_default_invalidation_mode
import threading, queue, random
from requests_futures.sessions import FuturesSession
import discum

class banclass:
    def __init__(self, user, guild, channel):
        self.user = user
        self.guild = guild
        self.channel = channel
    
    def scrapeusers(self):
        guild_id = self.guild
        channel_id = self.channel
        user_token = self.user
        bot = discum.Client(token=user_token)
        def close_after_fetching(resp, guild_id):
            if bot.gateway.finishedMemberFetching(guild_id):
                lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
                print(str(lenmembersfetched) + ' members fetched')
                bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.close()

        def get_members(guild_id, channel_id):
            bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
            bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.run()
            bot.gateway.resetSession()
            return bot.gateway.session.guild(guild_id).members

        members = get_members(guild_id, channel_id)
        memberslist = []

        for memberID in members:
            memberslist.append(memberID)
            print(memberID)

        f = open('users.txt', "a")
        for element in memberslist:
            f.write(element + '\n')
        f.close()
        return self
    
        
    @staticmethod
    def ban_all(guild, bot):
        guild_id = 0
        guild_id = guild
        bot_token = 0
        bot_token = bot
        with open('users.txt') as mem:
          lines = mem.readlines()
        q = queue.Queue()

        def requestsender():
            try:
                while True:
                    req, url, headers = q.get()
                    s = req(url, headers=headers).result()
                    print(s.text)
                    q.task_done()
            except Exception:
                pass
            for a in range(50):
                requestsenderth = threading.Thread(target=requestsender, args=())
            requestsenderth.start()

        def massban_worker():   
            session = FuturesSession()
            for x in open("users.txt"):
                q.put((session.put, f"https://discord.com/api/v{random.randint(6, 9)}/guilds/{guild_id}/bans/{x}", headers))
            q.join()

        headers = {"Authorization": f"Bot {bot_token}"}

        if 1 == 1:
            for x in range(100):
                threading.Thread(target=requestsender, daemon=True).start()       
            massban_worker()
            for i in range(350):
                massban_workerth = threading.Thread(target=massban_worker, args=())
            massban_workerth.start()
        return self 

ob1 = banclass('1', '2', '3')
