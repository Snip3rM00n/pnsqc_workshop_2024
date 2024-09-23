class CollectionHelpers:

    @staticmethod
    def first_or_none(collection, condition=None):
        """
        Gets the first instance of an object meeting a given condition or None if the condition is not satisfied.

        :param collection: The collection to search.
        :param condition: The condition to match (default: `_is_not_none`
        :return: The first object from the collection meeting the condition or None if the condition is not met.
        """
        if not callable(condition):
            condition = CollectionHelpers._is_not_none

        return next((item for item in collection if condition(item)), None)

    @staticmethod
    def _is_not_none(item):
        """
        Determines if an item is not none.

        :param item: The item to check.
        :return: A Boolean that determines whether the object is None or not.
        """
        return item is not None
