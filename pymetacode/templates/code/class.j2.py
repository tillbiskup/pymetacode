

class {{ class.name }}:
    """
    One sentence (on one line) describing the class.

    More description comes here...


    Attributes
    ----------
    attr : :class:`None`
        Short description

    Raises
    ------
    exception
        Short description when and why raised


    Examples
    --------
    It is always nice to give some examples how to use the class. Best to do
    that with code examples:

    .. code-block::

        obj = {{ class.name }}()
        ...

    {% if package.version != '0.1' %}
    .. versionadded:: {{ package.version }}
    {% endif %}

    """

    pass
