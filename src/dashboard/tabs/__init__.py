"""
Módulos de tabs do dashboard
"""
from .overview import render_overview_tab
from .execution_time import render_execution_time_tab
from .comparisons import render_comparisons_tab
from .recursion import render_recursion_tab
from .complexity import render_complexity_tab
from .logic import render_logic_tab
from .conclusions import render_conclusions_tab

__all__ = [
    'render_overview_tab',
    'render_execution_time_tab',
    'render_comparisons_tab',
    'render_recursion_tab',
    'render_complexity_tab',
    'render_logic_tab',
    'render_conclusions_tab'
]
