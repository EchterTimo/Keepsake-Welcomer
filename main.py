from os import getenv
from dotenv import load_dotenv
from interactions.api.events import MemberAdd
from interactions import (
    Client,
    Intents,
    listen,
    Activity,
    ActivityType,
    AllowedMentions
)
from people import is_keepsake_employee

load_dotenv()

__version__ = "1.0.2"
ROLE_TO_GIVE = getenv("ROLE_TO_GIVE")
CHANNEL_TO_ANNOUNCE = getenv("CHANNEL_TO_ANNOUNCE")

client = Client(
    activity=Activity(
        name="for Keepsake Games Employees",
        state=f"v{__version__}",
        type=ActivityType.WATCHING
    ),
    delete_unused_application_cmds=False,
    disable_dm_commands=True,
    send_command_tracebacks=False,  # todo: remove in prod
    intents=Intents.new(
        default=True,
        guild_members=True
    ),
    token=getenv("DISCORD_TOKEN")
)


@listen(MemberAdd)
async def on_member_add(event: MemberAdd):
    member_id = event.member.id
    if is_keepsake_employee(member_id):
        await event.member.add_role(ROLE_TO_GIVE, reason="the user is a Keepsake Games employee")
        channel = client.get_channel(CHANNEL_TO_ANNOUNCE)
        await channel.send(
            content=f":saluting_face: Keepsake Games Employee <@{member_id}> has joined the server and was given the role <@&{ROLE_TO_GIVE}>!",
            allowed_mentions=AllowedMentions(users=[member_id])
        )

if __name__ == '__main__':
    print("Running bot with version", __version__)
    client.start()
