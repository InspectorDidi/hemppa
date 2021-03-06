class MatrixModule:
    async def matrix_message(self, bot, room, event):
        msg = 'This is Hemppa, a generic Matrix bot. Known commands:\n\n'

        for modulename, moduleobject in bot.modules.items():
            msg = msg + '!' + modulename
            try:
                msg = msg + ' - ' + moduleobject.help() + '\n'
            except AttributeError:
                pass
            msg + msg + '\n'
        msg = msg + "\nAdd your own commands at https://github.com/vranki/hemppa"
        await bot.send_text(room, msg)

    def help(self):
        return('Prints help on commands')
