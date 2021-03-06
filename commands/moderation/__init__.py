from .exclude import Exclude
from .nickname import Nickname
from .role import Role
from .silence import Silence


def setup(bot):
    bot.add_cog(Exclude(bot))
    bot.add_cog(Nickname(bot))
    bot.add_cog(Role(bot))
    bot.add_cog(Silence(bot))
