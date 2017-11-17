from src.contextmanager import ContextManager


def main():
    contextManager: ContextManager = ContextManager(5)
    contextManager.addToContext("Do you know about Spain?")
    print(contextManager.getContext())
    contextManager.addToContext("That is a big place!")
    print(contextManager.getContext())
    contextManager.addToContext("What is the population there?")
    print(contextManager.getContext())
    contextManager.addToContext("Now what do you think about France and its problems with Spain")
    print(contextManager.getContext())
    contextManager.addToContext("Now what do you think about France and its problems with Spain")
    print(contextManager.getContext())


if __name__ == '__main__':
    main()
