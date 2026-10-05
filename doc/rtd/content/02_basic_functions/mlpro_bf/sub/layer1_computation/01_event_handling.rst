.. _target_bf_event:

Event handling
==============

Event handling is a fundamental mechanism in MLPro. It decouples the object that detects a state
transition from the objects that react to it. The generic implementation is provided by
``mlpro.bf.events`` and is reused by higher layers such as multitasking, stream processing, and
machine learning.

The central classes are ``Event``, ``EventManager``, ``EventConfig``, and ``EventMode``.
Event identifiers use the type alias ``EventId`` and are represented by strings.

Event ids and handlers
----------------------

An event-capable class derives from ``EventManager`` and raises events under a unique event id.
Handlers can register for a particular id and are called whenever the event is dispatched.

.. code-block:: python

    from mlpro.bf.events import Event, EventId, EventManager


    class Producer(EventManager):

        C_EVENT_CHANGED: EventId = 'CHANGED'

        def change(self):
            event = Event(p_raising_object=self)
            self._raise_event(
                p_event_id=self.C_EVENT_CHANGED,
                p_event_object=event,
            )


    def handler(p_event_id, p_event_object):
        print(p_event_id, p_event_object.get_raising_object())


    producer = Producer()
    producer.register_event_handler(
        p_event_id=Producer.C_EVENT_CHANGED,
        p_event_handler=handler,
    )
    producer.change()

The ``Event`` object transports the raising object, a time stamp, and optional event-specific
keyword data to all registered handlers.

Configurable events
-------------------

Event generation can be configured with ``EventConfig``. Concrete event-capable implementations
define their own child class and add one attribute per configurable event.

By convention, event ids and their corresponding configuration attributes are written in **upper
case** and are **identical**. This keeps the relationship transparent and allows an implementation
to query a mode directly by event id.

.. code-block:: python

    from dataclasses import dataclass

    from mlpro.bf.events import EventConfig, EventMode


    @dataclass
    class ProducerEvents(EventConfig):

        CHANGED: EventMode = EventMode.EVENT


    config = ProducerEvents(
        CHANGED=EventMode.OFF,
    )

The generic modes are:

``EventMode.OFF``
    The event is disabled.

``EventMode.EVENT``
    The event is enabled and may be raised.

The configuration is optional. If no ``EventConfig`` object is supplied, MLPro preserves the
historic behavior and ``_get_event_mode()`` returns ``EventMode.EVENT`` for every queried event id.

If a configuration object is supplied, every queried event id must have a matching attribute.
A mismatch indicates an implementation error and raises ``ImplementationError``. The concrete
event-capable implementation is responsible for maintaining the convention between event ids and
configuration attributes.

Efficient event creation
------------------------

The event mode should be queried **before** creating the ``Event`` object. This is important for
events that may occur at high frequency: a disabled event should cause virtually no runtime overhead.

.. code-block:: python

    class Producer(EventManager):

        C_EVENT_CHANGED: EventId = 'CHANGED'

        def change(self):

            if self._get_event_mode(self.C_EVENT_CHANGED) == EventMode.OFF:
                return

            self._raise_event(
                p_event_id=self.C_EVENT_CHANGED,
                p_event_object=Event(p_raising_object=self),
            )

``_raise_event()`` deliberately does not evaluate the event configuration. At that point the event
object already exists. Its task is only to look up the registered handlers and dispatch the event.

The dispatcher is intentionally lightweight and silent. Event handling itself does not perform
routine logging.

Higher-level event modes
------------------------

Higher MLPro layers may extend the event-mode semantics without changing the generic event
infrastructure. In :ref:`Layer 4 - Machine Learning <target_bf_ml>`, for example,
``EventModeML`` adds the mode ``ADAPTATION``. This allows a concrete ML implementation to
distinguish between a normal event and an event that shall additionally count as a model adaptation.

The interpretation of such higher-level modes remains the responsibility of the concrete
implementation. ``EventManager`` itself only provides the generic event configuration, handler
registration, and event dispatch mechanisms.


**Cross reference**

- :ref:`Howto BF-EH-001: Event handling <Howto BF EH 001>`
- :ref:`BF-MT - Multitasking <target_bf_mt>`
- :ref:`Layer 4 - Machine Learning <target_bf_ml>`
- :ref:`API reference BF-EVENTS - Event handling <target_api_bf_event>`
