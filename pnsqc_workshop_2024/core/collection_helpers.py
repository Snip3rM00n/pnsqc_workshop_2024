class CollectionHelpers:

    @staticmethod
    def first_or_none(collection, condition=None):
        if not callable(condition):
            condition = CollectionHelpers._is_not_none

        return next((item for item in collection if condition(item)), None)

    @staticmethod
    def _is_not_none(item):
        return item is not None
