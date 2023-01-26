from behavioral_patterns.command_pattern.sender import Invoker
from behavioral_patterns.command_pattern.command import *

if __name__ == '__main__':
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))
    receiver = Receiver()
    invoker.set_on_finish(
        ComplexCommand(receiver=receiver, a="Send email", b="Save report")
    )

    invoker.do_something_important()
