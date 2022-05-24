import numbers

import Thing
class Environment:
    """
    Abstract class representing an Environment.  'Real' Environment classes
    inherit from this.

    Environments typically need to implement:
        percept:        Define the percept the agent sees
        execute_action: Define the effects of executing an action.
                        Also update the agent.performance slot

    The environment keeps a list of .things and .agents (which is a subset of .things)
    Each agent has a .performance slot, initialized to 0.
    Each thing has a .location slot, even though some environments may not need this
    """

    def __init__(self):
        self.things = []
        self.agents = []

    def thing_classes(self):
        """
        Keep track of classes that are allowed in this environment
        :return: a list of classes allowed in this environment
        """
        return []

    def percept(self, agent):
        """
        Define what the agent sees at this point
        :param agent: an agent class instance
        :return: the percept that the agent sees at this point
        """
        # Implement this in the new environment class
        raise NotImplementedError

    def execute_action(self, agent, action):
        """
        Change the world to reflect this action
        :param agent: an agent class instance
        :param action:
        :return:
        """
        # Implement this in the new environment class
        raise NotImplementedError

    def default_location(self, thing):
        """
        Default location to place a new thing with unspecified location
        :param thing: an instance of a subclass of Thing
        :return: None
        """
        return None

    def exogenous_change(self):
        """
        If there is a spontaneous change in the world, override this.
        :return: None
        """
        return None

    def is_done(self):
        """
        By default the environment is done when no agent is alive.
        Should be True is no agent is alive
        :return: boolean
        """
        return not(any(agent.is_alive() for agent in self.agents))

    def step(self):
        """
        Run the environment for one time step.  If the actions and
        exogenous changes are independent, this method will do.
        If there are interactions between them, then this method
        must be overriden
        :return: None
        """

        if self.is_done():
            return
        actions = []
        for agent in self.agents:
            if agent.is_alive:
                actions.append(agent.program(self.percept(agent)))
            else:
                actions.append("")
        for (agent, action) in zip(self.agents, actions):
            self.execute_action(agent, action)
        self.exogenous_change()

    def run(self, steps=1000):
        """
        Run the environment for given number of time steps.
        :param steps: integer number of steps to take
        :return: None
        """

        for step in range(steps):
            if self.is_done():
                return
            self.step()

    def list_things_at(self, location, tclass=Thing):
        """
        Show all things at a specific location
        :param location:
        :param tclass:
        :return: list of all things exactly at a given location
        """

        if isinstance(location, numbers.Number):
            return [thing for thing in self.things
                    if thing.location == location and isinstance(thing, tclass)]
        return [thing for thing in self.things
                if all(x == y for x, y in zip(thing.location, location)) and isinstance(thing, tclass)]

    def some_things_at(self, location, tclass=Thing):
        """Return true if at least one of the things at location
        is an instance of class tclass (or a subclass)."""
        return self.list_things_at(location, tclass) != []

    def add_thing(self, thing, location=None):
        """Add a thing to the environment, setting its location. For
        convenience, if thing is an agent program we make a new agent
        for it. (Shouldn't need to override this.)"""
        if not isinstance(thing, Thing):
            thing = Agent(thing)
        if thing in self.things:
            print("Can't add the same thing twice")
        else:
            thing.location = location if location is not None else self.default_location(thing)
            self.things.append(thing)
            if isinstance(thing, Agent):
                thing.performance = 0
                self.agents.append(thing)

    def delete_thing(self, thing):
        """Remove a thing from the environment."""
        try:
            self.things.remove(thing)
        except ValueError as e:
            print(e)
            print("  in Environment delete_thing")
            print("  Thing to be removed: {} at {}".format(thing, thing.location))
            print("  from list: {}".format([(thing, thing.location) for thing in self.things]))
        if thing in self.agents:
            self.agents.remove(thing)