__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""description"""
__all__ = [
    "SIMPLE_TIMER_TEMPLATE",
]

# OnCalendar=*-*-* 06:00:00
# with the same unit prefix name
SIMPLE_TIMER_TEMPLATE = """
[Unit]
Description=Run {service} {interval}

[Timer]
OnCalendar={on_calendar}
Persistent=true

[Install]
WantedBy=timers.target
"""
