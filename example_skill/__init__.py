######################################################################
#   
#   postgres test skill
#   demonstration
#   
######################################################################
from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
from opsdroid.events import Message

class pgtestSkill(Skill):
    table_name=self.config.get('custom_table_name')

    @match_regex('^!put (?P<key>\w+) (?P<data>\w+)$')
    async def putter(self, message):
        await self.opsdroid.memory.put(
            message.entities['key']['value'],
            message.entities['data']['value'],
            table_name=
        )
        await message.respond(
            Message(
                text='ok, stored'
            )
        )

    @match_regex('^!get (?P<key>\w+)')
    async def getter(self, message):
        data = await self.opsdroid.memory.get(
            message.entities['key']['value'],
            table_name=self.config.get(self.table_name)
        )

        await message.respond(
            Message(
                text=str(data)
            )
        )

    @match_regex('^!delete (?P<key>\w+)')
    async def deleter(self, message):
        data = await self.opsdroid.memory.delete(
            message.entities['key']['value'],
            table_name=self.table_name
        )

        await message.respond(
            Message(
            text="OK! deleted"
            )
        )
