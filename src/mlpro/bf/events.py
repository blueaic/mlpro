## -------------------------------------------------------------------------------------------------
## -- Project : MLPro - The integrative middleware framework for standardized machine learning
## -- Package : mlpro.bf
## -- Module  : events
## -------------------------------------------------------------------------------------------------
## -- History :
## -- yyyy-mm-dd  Ver.      Auth.    Description
## -- 2022-08-21  1.0.0     DA       Creation/release
## -- 2022-10-06  1.1.0     DA       Specification of event id as string (for better observation and
## --                                to avoid collisions)
## -- 2023-03-25  1.1.1     DA       Class EventManager: correction in constructor
## -- 2023-11-17  1.2.0     DA       Class Event: new time stamp functionality
## -- 2023-11-18  1.2.1     DA       Class Event: time stamp is set to now() if not provided
## -- 2024-05-23  1.3.0     DA       Method EventManger._raise_event(): reduction to TypeError   
## -- 2025-05-27  1.4.0     DA       Class Event: new parent class KWArgs
## -- 2025-07-18  1.5.0     DA       Refactoring
## -- 2026-10-05  2.0.0     DA       Refactoring: 
## --                                - logging removed from EventManager
## --                                - tuned method EventManager._raise_event
## -------------------------------------------------------------------------------------------------

"""
Ver. 2.0.0 (2026-10-05)

This module provides classes for event handling. To this regard, the property class Eventmanager is
provided to add event functionality to child classes by inheritence.
"""

from datetime import datetime
from mlpro.bf.various import Log, TStamp, TStampType, KWArgs
from mlpro.bf.exceptions import *



# Export list for public API
__all__ = [ 'Event',
            'EventManager' ]



## -------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
class Event (TStamp, KWArgs):
    """
    Root class for events. It is ready to use and transfers the raising object and further key/value
    data to the event handler.

    Parameters
    ----------
    p_raising_object
        Reference to object that raised the event.
    **p_kwargs 
        List of named parameters
    """

## -------------------------------------------------------------------------------------------------
    def __init__(self, p_raising_object, p_tstamp:TStampType = None, **p_kwargs):
        self._raising_object = p_raising_object

        if p_tstamp is None:
            TStamp.__init__(self, p_tstamp = datetime.now())
        else:
            TStamp.__init__(self, p_tstamp = p_tstamp)

        KWArgs.__init__(self, **p_kwargs)


## -------------------------------------------------------------------------------------------------
    def get_raising_object(self):
        return self._raising_object


## -------------------------------------------------------------------------------------------------
    def get_data(self):
        return self.kwargs





## -------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
class EventManager:
    """
    This property class provides universal event management functionalities to be inherited to child
    classes.
    """

## -------------------------------------------------------------------------------------------------
    def __init__(self):
        self._registered_handlers = {}


## -------------------------------------------------------------------------------------------------
    def register_event_handler(self, p_event_id:str, p_event_handler):
        """
        Registers an event handler. 

        Parameters 
        ----------
        p_event_id : str
            Unique event id
        p_event_handler
            Reference to an event handler method with parameters p_event_id and p_event_object:Event
        """

        try:
            self._registered_handlers[p_event_id].append(p_event_handler)
        except:
            self._registered_handlers[p_event_id] = [ p_event_handler ]


## -------------------------------------------------------------------------------------------------
    def remove_event_handler(self, p_event_id:str, p_event_handler):
        """
        Removes an already registered event handler.

        Parameters 
        ----------
        p_event_id 
            Unique event id
        p_event_handler
            Reference to an event handler method.
        """

        try:
            self._registered_handlers[p_event_id].remove(p_event_handler)
        except:
            pass


## -------------------------------------------------------------------------------------------------
    def _raise_event(self, p_event_id:str, p_event_object:Event):
        """
        Raises an event and calls all registered handlers. To be used inside an event manager class.

        Parameters
        ----------
        p_event_id : str
            Unique event id
        p_event_object : Event
            Event object with further context informations
        """

        handlers = self._registered_handlers.get(p_event_id)

        if not handlers: return

        for handler in handlers:
            handler( p_event_id=p_event_id,
                     p_event_object=p_event_object )   