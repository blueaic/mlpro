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
## --                                - new type EventId
## --                                - new classes EventMode, EventConfig
## -------------------------------------------------------------------------------------------------

"""
Ver. 2.0.0 (2026-10-05)

This module provides generic building blocks for event handling. Event identifiers are represented
by the type alias EventId. EventMode and EventConfig provide a lightweight configuration mechanism
that allows event-capable classes to enable or disable individual events.

The property class EventManager adds event handling functionality to child classes by inheritance.
It manages event-handler registration and dispatch. Concrete EventConfig child classes may define
arbitrary event switches. By convention, the name of an event switch should be identical to the
corresponding EventId. This convention is implemented and documented by the concrete event-capable
class; it is not enforced by EventManager.
"""

from datetime import datetime
from typing import TypeAlias
from dataclasses import dataclass
from enum import IntEnum

from mlpro.bf.various import Log, TStamp, TStampType, KWArgs



# Export list for public API
__all__ = [ 'EventId',
            'EventMode',
            'EventConfig',
            'Event',
            'EventManager' ]



EventId: TypeAlias = str



## -------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
class EventMode(IntEnum):
    """
    Defines the generic operating modes of an event.

    The mode is typically queried by an event-capable implementation before an :class:`Event`
    object is created. This allows disabled events to be skipped with minimal runtime overhead.

    Attributes
    ----------
    OFF : int
        Event is disabled.
    EVENT : int
        Event is enabled and may be raised.
    """

    OFF   = 0
    EVENT = 1




## -------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
@dataclass
class EventConfig:
    """
    Root class for event configurations.

    Concrete child classes define implementation-specific event switches as dataclass attributes.
    The type of a switch is typically :class:`EventMode` or a specialized derivative introduced
    by a higher-level MLPro package.

    By convention, the attribute name of an event switch should be identical to the corresponding
    :class:`EventId`. The concrete event-capable implementation is responsible for maintaining
    this relation; it is deliberately not enforced by MLPro.

    Notes
    -----
    The root class itself does not define any event switches.
    """

    pass    





## -------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
class Event (TStamp, KWArgs):
    """
    Root class for events. It is ready to use and transfers the raising object and further key/value
    data to the event handler.

    Parameters
    ----------
    p_raising_object
        Reference to the object that raises the event.
    p_tstamp : TStampType, optional
        Time stamp of the event. If omitted, the current date and time are used.
    **p_kwargs
        Additional event-specific data passed to registered handlers.
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
        """
        Returns the object that raised the event.

        Returns
        -------
        object
            Raising object.
        """

        return self._raising_object


## -------------------------------------------------------------------------------------------------
    def get_data(self):
        """
        Returns the event-specific key/value data.

        Returns
        -------
        dict
            Dictionary with event-specific data supplied at event creation.
        """

        return self.kwargs





## -------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
class EventManager:
    """
    Property class providing universal event management functionality.

    EventManager manages handler registration and dispatch for string-based :class:`EventId`
    values. An optional :class:`EventConfig` can be supplied to configure individual events.

    For backward compatibility, events that are not covered by a configuration are treated as
    :attr:`EventMode.EVENT`. Consequently, existing event-capable classes retain their previous
    behaviour unless they explicitly evaluate an event configuration and disable an event.

    Parameters
    ----------
    p_event_config : EventConfig, optional
        Event configuration used by the concrete event-capable implementation. If omitted,
        all events default to :attr:`EventMode.EVENT`.

    Notes
    -----
    Event configuration is intentionally evaluated through :meth:`_get_event_mode` by the concrete
    event-capable implementation before creating the corresponding :class:`Event` object.
    :meth:`_raise_event` only dispatches an already created event and does not evaluate the
    configuration itself.
    """

## -------------------------------------------------------------------------------------------------
    def __init__(self, p_event_config : EventConfig = None):

        self._registered_handlers = {}
        self._event_config        = p_event_config


## -------------------------------------------------------------------------------------------------
    def register_event_handler(self, p_event_id : EventId, p_event_handler):
        """
        Registers an event handler. 

        Parameters 
        ----------
        p_event_id : EventId
            Unique event identifier.
        p_event_handler
            Reference to an event handler callable accepting the named parameters `p_event_id`
            and `p_event_object`.
        """

        try:
            self._registered_handlers[p_event_id].append(p_event_handler)
        except:
            self._registered_handlers[p_event_id] = [ p_event_handler ]


## -------------------------------------------------------------------------------------------------
    def remove_event_handler(self, p_event_id : EventId, p_event_handler):
        """
        Removes an already registered event handler.

        Parameters 
        ----------
        p_event_id : EventId
            Unique event identifier.
        p_event_handler
            Reference to the registered event handler to be removed.
        """

        try:
            self._registered_handlers[p_event_id].remove(p_event_handler)
        except:
            pass


## -------------------------------------------------------------------------------------------------
    def _get_event_mode(self, p_event_id : EventId) -> EventMode:
        """
        Returns the configured mode of an event.

        This internal service method is intended to be called by the concrete event-capable
        implementation before creating an :class:`Event` object. This allows disabled events to be
        rejected early and avoids unnecessary event-object creation.

        Parameters
        ----------
        p_event_id : EventId
            Unique event identifier. By convention, the identifier matches the corresponding
            attribute name in the concrete :class:`EventConfig` child class.

        Returns
        -------
        EventMode
            Configured event mode. :attr:`EventMode.EVENT` is returned if no event configuration
            is supplied or if the given event identifier is not represented by the configuration.

        Notes
        -----
        The fallback to :attr:`EventMode.EVENT` preserves the behaviour of existing MLPro event
        implementations.
        """

        if self._event_config is None:
            return EventMode.EVENT

        return getattr(
            self._event_config,
            p_event_id,
            EventMode.EVENT,
        )        


## -------------------------------------------------------------------------------------------------
    def _raise_event(self, p_event_id : EventId, p_event_object:Event):
        """
        Raises an event and calls all registered handlers. To be used inside an event manager class.

        Parameters
        ----------
        p_event_id : EventId
            Unique event identifier.
        p_event_object : Event
            Event object carrying the event context.

        Notes
        -----
        This method does not evaluate the event configuration. The concrete implementation should
        call :meth:`_get_event_mode` before creating the event object and invoke this method only
        for events that are to be dispatched.
        """

        # 1 Check for registered event handlers
        handlers = self._registered_handlers.get(p_event_id)
        if not handlers: return


        # 2 Call all registered handlers
        for handler in handlers:
            handler( p_event_id=p_event_id,
                     p_event_object=p_event_object )   